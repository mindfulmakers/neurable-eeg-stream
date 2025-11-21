# This file is just for reference on how to stream data from the Neurable side.

import asyncio
import json
import time

import websockets

clients = set()


async def handle_client(ws):
    clients.add(ws)
    try:
        async for _ in ws:  # producer sends data but we ignore input
            pass
    finally:
        clients.remove(ws)


async def broadcast_queue(queue):
    while True:
        msg = await queue.get()
        if clients:
            await asyncio.gather(*[c.send(msg) for c in clients])


async def producer(queue):
    while True:
        eeg_sample = {
            "timestamp": time.time(),
            "channels": [0.1, -0.2, 0.35, 0.0],
        }
        msg = json.dumps(eeg_sample)
        await queue.put(msg)
        await asyncio.sleep(0.01)  # 100 Hz example


async def main():
    queue = asyncio.Queue()

    # Start WebSocket server
    server = websockets.serve(handle_client, "0.0.0.0", 8765)

    await asyncio.gather(
        server,
        broadcast_queue(queue),
        producer(queue),
    )


if __name__ == "__main__":
    asyncio.run(main())
