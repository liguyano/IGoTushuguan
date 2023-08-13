import asyncio
import websockets
import logging

# 设置日志级别为DEBUG，即记录所有级别的日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# 创建一个 Formatter 对象
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# 创建一个 StreamHandler 对象，将日志输出到标准输出
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# 将 StreamHandler 添加到 Logger
logger.addHandler(stream_handler)

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        try:
            for i in range(5):  # Send and receive 5 messages
                message = f"Hello, WebSocket! Message {i + 1}"
                await websocket.send(message)
                response = await websocket.recv()
                logger.info(response)
                response = await websocket.recv()
                logger.info(response)
        except websockets.ConnectionClosed:
            print("closed")
        except Exception as e:
            print(str(e))
#wechat.v2.traceint.com/ws?ns=prereserve/queue
asyncio.get_event_loop().run_until_complete(
    #hello('ws://wechat.v2.traceint.com/ws?ns=prereserve/queue')
hello('ws://localhost:7001'))
asyncio.get_event_loop().run_until_complete(
hello('ws://wechat.v2.traceint.com/ws?ns=prereserve/queue')
)
