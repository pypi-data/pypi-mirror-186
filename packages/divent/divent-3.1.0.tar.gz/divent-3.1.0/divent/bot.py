import json
import logging
from datetime import datetime, timedelta
from functools import wraps
from os import getenv, path
from typing import Dict, Optional

from disnake import Client, Guild
from dotenv import load_dotenv
from ics import Calendar, ContentLine, Event
from ics.alarm import DisplayAlarm
from oauthlib.oauth2 import TokenExpiredError
from quart import Quart, redirect, render_template, request, session, url_for
from requests_oauthlib import OAuth2Session  # type: ignore
import sentry_sdk
from sentry_sdk.integrations.quart import QuartIntegration
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware  # type: ignore


load_dotenv()

DISCORD_TOKEN = getenv("DISCORD_TOKEN")
OAUTH2_CLIENT_ID = getenv("OAUTH2_CLIENT_ID")
OAUTH2_CLIENT_SECRET = getenv("OAUTH2_CLIENT_SECRET")
if not DISCORD_TOKEN:
    raise Exception("Missing DISCORD_TOKEN")
if not OAUTH2_CLIENT_ID:
    raise Exception("Missing OAUTH2_CLIENT_ID")
if not OAUTH2_CLIENT_SECRET:
    raise Exception("Missing OAUTH2_CLIENT_SECRET")

QUART_DEBUG = getenv("QUART_DEBUG", False)
if QUART_DEBUG:
    logging.basicConfig(level=logging.DEBUG)

SENTRY_DSN = getenv("SENTRY_DSN")
if SENTRY_DSN:
    sentry_sdk.init(SENTRY_DSN, integrations=[QuartIntegration()])

API_BASE_URL = getenv("API_BASE_URL", "https://discordapp.com/api")
AUTHORIZATION_BASE_URL = f"{API_BASE_URL}/oauth2/authorize"
TOKEN_URL = f"{API_BASE_URL}/oauth2/token"


class Discord(Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!", flush=True)


client = Discord()
app = Quart(__name__)
app.config["SECRET_KEY"] = OAUTH2_CLIENT_SECRET
app.asgi_app = ProxyHeadersMiddleware(app.asgi_app, "*")  # type: ignore


def get_guild_by_id(guild_id: str) -> Optional[Guild]:
    if guild_id:
        for guild in client.guilds:
            if str(guild.id) == guild_id or guild.vanity_url_code == guild_id:
                return guild
    return None


CATALOG_CACHE = {}


@app.errorhandler(500)
async def errorhandler(error: Exception):
    print(f"\33[31m{error}\33[m", flush=True)
    return await render_template("error.html.j2", error=str(error)), 500


@app.errorhandler(404)
async def not_found(error: Exception):
    return await render_template("error.html.j2", error=str(error)), 404


def token_updater(token: str):
    session["oauth2_token"] = token


def make_session(
    token: Optional[Dict[str, str]] = None, state: Optional[str] = None
) -> OAuth2Session:
    return OAuth2Session(
        client_id=OAUTH2_CLIENT_ID,
        token=token,
        state=state,
        scope=["identify", "guilds"],
        redirect_uri=f"{request.host_url}callback",
        auto_refresh_kwargs={
            "client_id": OAUTH2_CLIENT_ID,
            "client_secret": OAUTH2_CLIENT_SECRET,
        },
        auto_refresh_url=TOKEN_URL,
        token_updater=token_updater,
    )


def i18n(str: str) -> str:
    lang = request.accept_languages.best_match(["en", "fr"])

    if lang not in CATALOG_CACHE:
        catalog_file = f"{path.dirname(__file__)}/translations/{lang}.json"
        if path.exists(catalog_file):
            with open(catalog_file) as catalog_json:
                catalog = json.load(catalog_json)
                CATALOG_CACHE[lang] = catalog

    if lang in CATALOG_CACHE and str in CATALOG_CACHE[lang]:
        return CATALOG_CACHE[lang][str]

    return str


def days_before_failure() -> int:
    nextYear = datetime.today().year + 5 - ((datetime.today().year + 5) % 5)
    nextDate = datetime(year=nextYear, month=6, day=3)
    nextDelta = nextDate - datetime.now()

    return nextDelta.days


def cdn_avatar_url(user_id: int, hash: str) -> str:
    ext = "gif" if hash.startswith("a_") else "png"
    return f"https://cdn.discordapp.com/avatars/{user_id}/{hash}.{ext}"


@app.context_processor
def context_processor():
    return dict(
        _=i18n,
        client=client,
        cdn_avatar_url=cdn_avatar_url,
        days_before_failure=days_before_failure(),
    )


def login_required(fn):
    @wraps(fn)
    async def wrapper(*args, **kwargs):
        if session.get("oauth2_token"):
            return await fn(*args, **kwargs)

        session["redirect_url"] = request.path
        return redirect(url_for(".login"))

    return wrapper


@app.route("/")
async def index():
    return await render_template("index.html.j2")


@app.route("/login")
async def login():
    discord = make_session()
    authorization_url, state = discord.authorization_url(AUTHORIZATION_BASE_URL)
    session["oauth2_state"] = state
    return redirect(authorization_url)


@app.route("/callback")
async def callback():
    request_values = await request.values
    if request_values.get("error"):
        return errorhandler(request_values.get("error"))

    discord = make_session(state=session.get("oauth2_state"))
    token = discord.fetch_token(
        TOKEN_URL,
        client_secret=OAUTH2_CLIENT_SECRET,
        authorization_response=request.url,
    )
    token_updater(token)
    return redirect(session.pop("redirect_url", url_for(".guilds")))


@app.route("/guilds")
@login_required
async def guilds():
    guild = get_guild_by_id(request.args.get("guild"))

    if guild:
        return redirect(
            url_for(".subscribe", guild_id=guild.vanity_url_code or guild.id)
        )

    try:
        discord = make_session(token=session.get("oauth2_token"))
        user = discord.get(f"{API_BASE_URL}/users/@me").json()
        user_guilds = discord.get(f"{API_BASE_URL}/users/@me/guilds").json()
    except TokenExpiredError:
        return redirect(url_for(".login"))

    common_guilds = []
    for bot_guild in client.guilds:
        for user_guild in user_guilds:
            if str(bot_guild.id) == user_guild["id"]:
                common_guilds.append(bot_guild)

    return await render_template(
        "guilds.html.j2", user=user, common_guilds=common_guilds
    )


@app.route("/subscribe/<guild_id>")
@login_required
async def subscribe(guild_id: str):
    guild = get_guild_by_id(guild_id)
    if guild is None:
        return redirect(url_for(".login"))

    try:
        discord = make_session(token=session.get("oauth2_token"))
        user_guilds = discord.get(f"{API_BASE_URL}/users/@me/guilds").json()
    except TokenExpiredError:
        return redirect(url_for(".login"))

    if not any(str(guild.id) == user_guild["id"] for user_guild in user_guilds):
        return redirect(url_for(".login"))

    return await render_template("subscribe.html.j2", guild=guild)


@app.route("/<guild_id>.ics")
async def ical(guild_id: str):
    guild = get_guild_by_id(guild_id)
    if guild is None:
        return redirect(url_for(".login"))

    calendar = Calendar()

    calendar.extra.append(ContentLine(name="REFRESH-INTERVAL", value="PT1H"))
    calendar.extra.append(ContentLine(name="X-PUBLISHED-TTL", value="PT1H"))

    calendar.extra.append(ContentLine(name="NAME", value=guild.name))
    calendar.extra.append(ContentLine(name="X-WR-CALNAME", value=guild.name))

    if guild.description:
        calendar.extra.append(ContentLine(name="DESCRIPTION", value=guild.description))
        calendar.extra.append(ContentLine(name="X-WR-CALDESC", value=guild.description))

    for scheduled_event in guild.scheduled_events:
        event = Event()
        event.summary = scheduled_event.name
        event.begin = scheduled_event.scheduled_start_time
        event.end = scheduled_event.scheduled_end_time
        event.duration = timedelta(hours=2)
        event.uid = str(scheduled_event.id)
        event.description = scheduled_event.description
        event.url = f"https://discord.com/events/{guild_id}/{scheduled_event.id}"
        event.location = (
            scheduled_event.entity_metadata.location
            if scheduled_event.entity_metadata
            else None
        )

        alarm = DisplayAlarm()
        alarm.trigger = timedelta(hours=-1)
        event.alarms.append(alarm)

        calendar.events.append(event)

    return calendar.serialize()


def __main__():
    quart_task = client.loop.create_task(app.run_task("0.0.0.0"))
    quart_task.add_done_callback(lambda f: client.loop.stop())
    client.run(DISCORD_TOKEN)
