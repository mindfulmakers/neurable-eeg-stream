import asyncio
import json
import ssl

import websockets

HUB_IP = (
    "stream1.mindfulmakers.xyz"  # OR stream2.mindfulmakers.xyz
)


async def main():
    print(f"Connecting to {HUB_IP}")
    # Disable SSL certificate verification (for testing only)
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    
    async with websockets.connect(f"wss://{HUB_IP}", ssl=ssl_context) as ws:
        async for msg in ws:
            eeg = json.loads(msg)
            # process eeg
            print(eeg)


asyncio.run(main())
