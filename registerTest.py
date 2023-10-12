import time

import requests as re
import asyncio
import websockets
import websocket
import json
import sys
import threading
linid=12
seat=""
queHandle={}
queList=[]
def loadCookie() -> str:
    json_file_path = "./config/config1.json"
    global linid
    global seat
    # 读取 JSON 文件并将其解析为 JSON 对象
    with open(json_file_path, "r") as json_file:
        json_data = json.load(json_file)
        linid=json_data['data1']['variables']['libid']
        seat=json_data['data1']['variables']['key']
        queHandle=json_data['queue_header']
        print(type(queHandle))
        for key in queHandle.keys():
            queList.append("{0}:{1}".format(key,queHandle[key]))
        print(queList)
        return json_data['header']['Cookie']

def hello(uri):
    ws=websocket.WebSocket()
    ws.connect(url=uri,header=queList)
    if (ws.connected):
        print("connected")
   # ws.connect(url=uri)
        try:
            while (ws.connected):
                ws.send('{"ns": "prereserve/queue"}')
                a = ws.recv()
                if (str(eval(a)).find("成功")>-1):
                    print("seikou")
                    break
                print("ws:{} ".format(eval(a)))
        except Exception as e:
            print(e)
    print("disconnect")
def send(date) -> str:
    a = re.post(" https://wechat.v2.traceint.com/index.php/graphql/ ", headers=header, json=date, verify=False)
    return a.text

def registerSeat():
    true = True
    false = False
    null = 'null'
    extra_headers = [("Cookie", header['Cookie'])]
    date4 = {"operationName": "prereserveCheckMsg",
             "query": "query prereserveCheckMsg {\n userAuth {\n prereserve {\n prereserveCheckMsg\n }\n }\n}"}
    a = re.post(" https://wechat.v2.traceint.com/index.php/graphql/ ", headers=header, json=date4, verify=False)
    print(eval(a.text))
    date3 = {"operationName": "index",
             "query": "query index($pos: String!, $param: [hash]) {\n userAuth {\n oftenseat {\n list {\n id\n info\n lib_id\n seat_key\n status\n }\n }\n message {\n new(from: \"system\") {\n has\n from_user\n title\n num\n }\n indexMsg {\n message_id\n title\n content\n isread\n isused\n from_user\n create_time\n }\n }\n reserve {\n reserve {\n token\n status\n user_id\n user_nick\n sch_name\n lib_id\n lib_name\n lib_floor\n seat_key\n seat_name\n date\n exp_date\n exp_date_str\n validate_date\n hold_date\n diff\n diff_str\n mark_source\n isRecordUser\n isChooseSeat\n isRecord\n mistakeNum\n openTime\n threshold\n daynum\n mistakeNum\n closeTime\n timerange\n forbidQrValid\n renewTimeNext\n forbidRenewTime\n forbidWechatCancle\n }\n getSToken\n }\n currentUser {\n user_id\n user_nick\n user_mobile\n user_sex\n user_sch_id\n user_sch\n user_last_login\n user_avatar(size: MIDDLE)\n user_adate\n user_student_no\n user_student_name\n area_name\n user_deny {\n deny_deadline\n }\n sch {\n sch_id\n sch_name\n activityUrl\n isShowCommon\n isBusy\n }\n }\n }\n ad(pos: $pos, param: $param) {\n name\n pic\n url\n }\n}",
             "variables": {"pos": "App-首页"}}
    date2 = {"operationName": "save",
             "query": "mutation save($key: String!, $libid: Int!, $captchaCode: String, $captcha: String) {\n userAuth {\n prereserve {\n save(key: $key, libId: $libid, captcha: $captcha, captchaCode: $captchaCode)\n }\n }\n}",
             "variables": {"key": seat, "libid": linid, "captchaCode": "", "captcha": ""}}
    print(eval(send(date3)))
    hello('wss://wechat.v2.traceint.com/ws?ns=prereserve/queue')
    saveStatueCheck = {"operationName": "prereserve",
                       "query": "query prereserve {\n userAuth {\n prereserve {\n prereserve {\n day\n lib_id\n seat_key\n seat_name\n is_used\n user_mobile\n id\n lib_name\n }\n }\n }\n}"}
    print(eval(send(saveStatueCheck)))
    liblist = {"operationName": "index",
               "query": "query index {\n userAuth {\n user {\n prereserveAuto: getSchConfig(extra: true, fields: \"prereserve.auto\")\n }\n currentUser {\n sch {\n isShowCommon\n }\n }\n prereserve {\n libs {\n is_open\n lib_floor\n lib_group_id\n lib_id\n lib_name\n num\n seats_total\n }\n }\n oftenseat {\n prereserveList {\n id\n info\n lib_id\n seat_key\n status\n }\n }\n }\n}"}
    print(eval(send(liblist)))
    libLayout = {"operationName": "libLayout",
                 "query": "query libLayout($libId: Int!) {\n userAuth {\n prereserve {\n libLayout(libId: $libId) {\n max_x\n max_y\n seats_booking\n seats_total\n seats_used\n seats {\n key\n name\n seat_status\n status\n type\n x\n y\n }\n }\n }\n }\n}",
                 "variables": {"libId": linid}}
    print(eval(send(libLayout)))
    saveSeat = {"operationName": "save",
                "query": "mutation save($key: String!, $libid: Int!, $captchaCode: String, $captcha: String) {\n userAuth {\n prereserve {\n save(key: $key, libId: $libid, captcha: $captcha, captchaCode: $captchaCode)\n }\n }\n}",
                "variables": {"key": seat, "libid": linid, "captchaCode": "", "captcha": ""}}
    print(eval(send(saveSeat)))



    saveSeat = {"operationName": "save",
                "query": "mutation save($key: String!, $libid: Int!, $captchaCode: String, $captcha: String) {\n userAuth {\n prereserve {\n save(key: $key, libId: $libid, captcha: $captcha, captchaCode: $captchaCode)\n }\n }\n}",
                "variables": {"key": "11,15.", "libid": 114222, "captchaCode": "", "captcha": ""}}
    print(eval(send(saveSeat)))

    a = re.post(" https://wechat.v2.traceint.com/index.php/graphql/ ", headers=header, json=date2, verify=False)
    #  print(a.text)https://wechat.v2.traceint.com/index.php/graphql/%20
    b = eval(a.text)
    print(b)
if __name__ == '__main__':
    startTime=time.time()
    header = {
        "Cookie": loadCookie()
    }
    extra_headers = [("Cookie", header['Cookie'])]
    while True:
        registerSeat()
        print(time.time()-startTime)
