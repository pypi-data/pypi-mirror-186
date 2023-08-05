import asyncio
import os
from functools import wraps

import click
from nostr.client.client import NostrClient
from nostr.event import Event
from nostr.key import PublicKey

from cashu.core.settings import CASHU_DIR, MINT_URL
from cashu.wallet.wallet import Wallet as Wallet


async def init_wallet(wallet: Wallet):
    """Performs migrations and loads proofs from db."""
    await wallet.load_proofs()


@click.group()
def cli():
    wallet = Wallet(MINT_URL, os.path.join(CASHU_DIR, "wallet"))
    asyncio.run(init_wallet(wallet))


# https://github.com/pallets/click/issues/85#issuecomment-503464628
def coro(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper


@coro
async def main():
    pk = (
        input("Enter your privatekey: ")
        or "bfc6e7b0b998645d45aa451a3b9a3174bfe696fba78e86a86637a16f43e6c683"
    )

    client = NostrClient(privatekey_hex=pk)
    await asyncio.sleep(1)

    import threading

    def callback(event: Event, decrypted_content):
        print(f"From {event.public_key[:5]}...: {decrypted_content}")

    t = threading.Thread(
        target=client.get_dm,
        args=(
            client.public_key,
            callback,
        ),
    )
    t.start()

    to_pubk = (
        input("Enter other pubkey: ")
        or "13395e6d975825cb811549b4b6ba6695c7ea8f75e1f3658d6cee2bee243195c3"
    )

    while True:
        msg = input("\nEnter message: ")
        client.dm(msg, PublicKey(bytes.fromhex(to_pubk)))


asyncio.run(main())
