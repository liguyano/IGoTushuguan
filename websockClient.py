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
header = {
    "Cookie":
        "FROM_TYPE=weixin; v=5.5; wechatSESS_ID=ddcc58baf2f4ddbeef1d7cd38818663df30cba2bd5ed45e3; Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VySWQiOjI0OTc1MjUyLCJzY2hJZCI6MjAwNTgsImV4cGlyZUF0IjoxNjkxOTQzNTQ4fQ.x1b5PgjwKq1WH_8PDDfGH9Ie3oM9uSzHDIwouB4bF-FxSgs6gO0lydw30yuhQsM1-UPrijA5yxg9U1EuUvRo_s9ZuziypiqJql2Y-sFpvS1ZYXD6lmQQhwdOnZzn0wr0rwGudAczQdXExBpTjX7YX8rwQs8Wr5mLsR08pXrFV-Ma0MAvxVzvG44F6c95ecx1oXa4VY1j0eRsp23T3NQZ8mMHOysaU2EZtHm_JMI7VAq1RN4EjFlkgt0I3UG1EctmH1LQH5RrEPgEXhHFbKLtAQbeJPcFCiHWNYh568KGnj7W6ETaXPdGsU_5vRW-OPIfVj3GJBUCI4Cpz8jDg22KZw; Hm_lvt_7ecd21a13263a714793f376c18038a87=1691766975,1691851495,1691895854,1691936349; Hm_lpvt_7ecd21a13263a714793f376c18038a87=1691938077; SERVERID=82967fec9605fac9a28c437e2a3ef1a4|1691938078|1691936345"
}
async def hello(uri):
    async with websockets.connect(uri) as websocket:
        try:
            await websocket.send('''
            GET https://wechat.v2.traceint.com/ws?ns=prereserve/queue HTTP/1.1
Host: wechat.v2.traceint.com
Connection: Upgrade
Pragma: no-cache
Cache-Control: no-cache
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue
Upgrade: websocket
Origin: https://web.traceint.com
Sec-WebSocket-Version: 13
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh
Cookie: FROM_TYPE=weixin; v=5.5; wechatSESS_ID=ddcc58baf2f4ddbeef1d7cd38818663df30cba2bd5ed45e3; Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VySWQiOjI0OTc1MjUyLCJzY2hJZCI6MjAwNTgsImV4cGlyZUF0IjoxNjkxOTQzNTQ4fQ.x1b5PgjwKq1WH_8PDDfGH9Ie3oM9uSzHDIwouB4bF-FxSgs6gO0lydw30yuhQsM1-UPrijA5yxg9U1EuUvRo_s9ZuziypiqJql2Y-sFpvS1ZYXD6lmQQhwdOnZzn0wr0rwGudAczQdXExBpTjX7YX8rwQs8Wr5mLsR08pXrFV-Ma0MAvxVzvG44F6c95ecx1oXa4VY1j0eRsp23T3NQZ8mMHOysaU2EZtHm_JMI7VAq1RN4EjFlkgt0I3UG1EctmH1LQH5RrEPgEXhHFbKLtAQbeJPcFCiHWNYh568KGnj7W6ETaXPdGsU_5vRW-OPIfVj3GJBUCI4Cpz8jDg22KZw; Hm_lvt_7ecd21a13263a714793f376c18038a87=1691766975,1691851495,1691895854,1691936349; Hm_lpvt_7ecd21a13263a714793f376c18038a87=1691937307; SERVERID=82967fec9605fac9a28c437e2a3ef1a4|1691937308|1691936345
Sec-WebSocket-Key: 5PmYDn6nGnLjp164iVSAbQ==
Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits''')
            for i in range(5):  # Send and receive 5 messages
                message = f"Hello, WebSocket! Message {i + 1}"
                await websocket.send(message)
                response = await websocket.recv()
                logger.info(response)
                # response = await websocket.recv()
                # logger.info(response)
        except websockets.ConnectionClosed:
            print("closed")
        except Exception as e:
            print(str(e))
#wechat.v2.traceint.com/ws?ns=prereserve/queue
# asyncio.get_event_loop().run_until_complete(
#     #hello('ws://wechat.v2.traceint.com/ws?ns=prereserve/queue')
# hello('ws://localhost:7001'))
asyncio.get_event_loop().run_until_complete(
hello('wss://wechat.v2.traceint.com/ws')
)
