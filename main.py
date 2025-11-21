import asyncio
import json

import websockets

EEG_SOURCE_URL = "wss://fill-me-in-after-signing-nda"


async def main():
    print(f"Connecting to {EEG_SOURCE_URL}")
    async with websockets.connect(EEG_SOURCE_URL) as ws:
        async for msg in ws:
            eeg = json.loads(msg)
            print(eeg)


asyncio.run(main())
