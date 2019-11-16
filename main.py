#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import websockets
import datetime
import random
import json

a1 = 20
a2 = -90
a3 = -10
articulaciones = [a1, a2, a3]
pinza = True


async def server(websocket, path):
    now = {
        "a_1": articulaciones[0],
        "a_2": articulaciones[1],
        "a_3": articulaciones[2],
        "pinza": pinza
    }
    await websocket.send(json.dumps(now, ensure_ascii=False))
    await asyncio.sleep(5 + random.random() * 5)

start_server = websockets.serve(server, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
