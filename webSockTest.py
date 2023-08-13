import asyncio
import websockets

a="\u6392\u961f\u6210\u529f\uff01\u8bf7\u57282\u5206\u949f\u5185\u9009\u62e9\u5ea7\u4f4d\uff0c\u5426\u5219\u9700\u8981\u91cd\u65b0\u6392\u961f\u3002"
async def echo(websocket, path):
    async for message in websocket:
        message = "I got your message:  {}".format(message)
        print(message)
        await websocket.send(message)
        await websocket.send(a)
asyncio.get_event_loop().run_until_complete(websockets.serve(echo, 'localhost', 7001))
asyncio.get_event_loop().run_forever()
