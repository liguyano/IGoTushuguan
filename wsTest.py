import websocket
# websocket.enableTrace(True)   # 打开日志, 将详细输出通讯过程
ws = websocket.WebSocket()
ws.connect("ws://echo.websocket.org")
a=ws.send("Hello Server")
print(a)
b=ws.recv()
print(b)
ws.close()
