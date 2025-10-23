import asyncio, os, json, logging, contextlib
from typing import Dict, Any
from fastapi import FastAPI
import httpx
from dotenv import load_dotenv

load_dotenv()

from agent import get_agent, ToolError

logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))
log = logging.getLogger("assistant-core")

SIGNAL_API_BASE   = os.getenv("SIGNAL_API_BASE", "http://signal-api:8080")
SIGNAL_NUMBER     = os.getenv("SIGNAL_NUMBER")
NOTIFY_URL        = os.getenv("NOTIFY_URL", "http://notifier-gateway:8787/notify")
GATEWAY_TOKEN     = os.getenv("GATEWAY_TOKEN")
POLL_TIMEOUT_SEC  = int(os.getenv("POLL_TIMEOUT_SEC", "60"))
DISABLE_RAG       = os.getenv("DISABLE_RAG", "true").lower() in ("1","true","yes")
ALLOW_SENDERS     = set(s.strip() for s in os.getenv("ALLOW_SENDERS", "").split(",") if s.strip())

if not SIGNAL_NUMBER or not GATEWAY_TOKEN:
    raise SystemExit("SIGNAL_NUMBER and GATEWAY_TOKEN are required")

app = FastAPI(title="assistant-core", version="0.1.0")
agent = get_agent(disable_rag=DISABLE_RAG)

async def send_signal(to: str, message: str):
    headers = {"Authorization": f"Bearer {GATEWAY_TOKEN}", "Content-Type": "application/json"}
    data = {"to": to, "message": message}
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.post(NOTIFY_URL, headers=headers, json=data)
        r.raise_for_status()

async def handle_incoming(envelope: Dict[str, Any]):
    sender = envelope.get("source")
    data_msg = envelope.get("dataMessage") or {}
    text = data_msg.get("message")
    if not sender or not text:
        return

    if ALLOW_SENDERS and sender not in ALLOW_SENDERS:
        log.warning("Rejecting message from non-allowed sender: %s", sender)
        return

    t = text.strip()
    if t == "/help":
        msg = ("Commands:\n"
               "/help – this menu\n"
               "/status – service heartbeat\n"
               "/weather [city] – quick weather\n"
               "/run <safe-cmd> – run whitelisted shell command")
        await send_signal(sender, msg); return

    if t == "/status":
        await send_signal(sender, "✅ assistant-core alive"); return

    try:
        reply = await agent.run(sender=sender, text=text)
    except ToolError as e:
        reply = f"Tool error: {e}"
    except Exception:
        log.exception("Agent failure")
        reply = "Sorry — something went wrong."

    await send_signal(sender, reply)

async def poll_loop():
    url = f"{SIGNAL_API_BASE}/v1/receive/{SIGNAL_NUMBER}"
    params = {"timeout": POLL_TIMEOUT_SEC}
    log.info("Starting receive poller: %s", url)

    while True:
        try:
            async with httpx.AsyncClient(timeout=POLL_TIMEOUT_SEC + 10) as client:
                r = await client.get(url, params=params)
                if r.status_code == 204:
                    continue
                r.raise_for_status()
                payload = r.json()
                if isinstance(payload, list):
                    for env in payload:
                        try:
                            await handle_incoming(env)
                        except Exception:
                            log.exception("Error handling envelope")
        except (httpx.TimeoutException, httpx.ConnectError):
            await asyncio.sleep(2)
        except Exception:
            log.exception("Poller error")
            await asyncio.sleep(3)

@app.on_event("startup")
async def _startup():
    app.state.poll_task = asyncio.create_task(poll_loop())

@app.on_event("shutdown")
async def _shutdown():
    with contextlib.suppress(Exception):
        app.state.poll_task.cancel()

@app.get("/healthz")
def health():
    return {"ok": True}
