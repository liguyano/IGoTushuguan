import requests as re
import asyncio
import websockets
import websocket
import json
import sys

linid=12
seat=""
queHandle={}
queList=[]
def loadCookie() -> str:
    json_file_path = "./config/config1.json"
    # 读取 JSON 文件并将其解析为 JSON 对象
    with open(json_file_path, "r") as json_file:
        json_data = json.load(json_file)
        linid=json_data['data1']['variables']['libid']
        seat=json_data['data1']['variables']['key'][0:-1]
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
    while (ws.connected):
        ws.send(str({"ns": "prereserve/queue"}))
        a = ws.recv()
        print("ws:{} ".format(a))
    print("disconnect")

if __name__ == '__main__':
    true=True
    false=False
    null='null'
    header = {
        "Cookie": loadCookie()
    }

    extra_headers = [("Cookie",header['Cookie'])]
#     preQueList=[
#         {"operationName":"index","query":"query index($pos: String!, $param: [hash]) {\n userAuth {\n oftenseat {\n list {\n id\n info\n lib_id\n seat_key\n status\n }\n }\n message {\n new(from: \"system\") {\n has\n from_user\n title\n num\n }\n indexMsg {\n message_id\n title\n content\n isread\n isused\n from_user\n create_time\n }\n }\n reserve {\n reserve {\n token\n status\n user_id\n user_nick\n sch_name\n lib_id\n lib_name\n lib_floor\n seat_key\n seat_name\n date\n exp_date\n exp_date_str\n validate_date\n hold_date\n diff\n diff_str\n mark_source\n isRecordUser\n isChooseSeat\n isRecord\n mistakeNum\n openTime\n threshold\n daynum\n mistakeNum\n closeTime\n timerange\n forbidQrValid\n renewTimeNext\n forbidRenewTime\n forbidWechatCancle\n }\n getSToken\n }\n currentUser {\n user_id\n user_nick\n user_mobile\n user_sex\n user_sch_id\n user_sch\n user_last_login\n user_avatar(size: MIDDLE)\n user_adate\n user_student_no\n user_student_name\n area_name\n user_deny {\n deny_deadline\n }\n sch {\n sch_id\n sch_name\n activityUrl\n isShowCommon\n isBusy\n }\n }\n }\n ad(pos: $pos, param: $param) {\n name\n pic\n url\n }\n}","variables":{"pos":"App-首页"}}
#         ,{"operationName":"getUserCancleConfig","query":"query getUserCancleConfig {\n userAuth {\n user {\n holdValidate: getSchConfig(fields: \"hold_validate\", extra: true)\n }\n }\n}","variables":{}},
# {"operationName":"prereserveCheckMsg","query":"query prereserveCheckMsg {\n userAuth {\n prereserve {\n prereserveCheckMsg\n }\n }\n}"}
#
#     ]
#     for pre in preQueList:
#         a = re.post(" https://wechat.v2.traceint.com/index.php/graphql/ ", headers=header, json=pre, verify=False)
#         print(eval(a.text))
 #   don't need this'
#{"ns":"prereserve\/queue","msg":"\u6392\u961f\u6210\u529f\uff01\u8bf7\u57282\u5206\u949f\u5185\u9009\u62e9\u5ea7\u4f4d\uff0c\u5426\u5219\u9700\u8981\u91cd\u65b0\u6392\u961f\u3002","code":0,"data":0}
    # wechat.v2.traceint.com/ws?ns=prereserve/queue

    date4={"operationName":"prereserveCheckMsg","query":"query prereserveCheckMsg {\n userAuth {\n prereserve {\n prereserveCheckMsg\n }\n }\n}"}
    a=re.post(" https://wechat.v2.traceint.com/index.php/graphql/ ", headers=header, json=date4, verify=False)
    print(eval(a.text))
    date3={"operationName":"index","query":"query index($pos: String!, $param: [hash]) {\n userAuth {\n oftenseat {\n list {\n id\n info\n lib_id\n seat_key\n status\n }\n }\n message {\n new(from: \"system\") {\n has\n from_user\n title\n num\n }\n indexMsg {\n message_id\n title\n content\n isread\n isused\n from_user\n create_time\n }\n }\n reserve {\n reserve {\n token\n status\n user_id\n user_nick\n sch_name\n lib_id\n lib_name\n lib_floor\n seat_key\n seat_name\n date\n exp_date\n exp_date_str\n validate_date\n hold_date\n diff\n diff_str\n mark_source\n isRecordUser\n isChooseSeat\n isRecord\n mistakeNum\n openTime\n threshold\n daynum\n mistakeNum\n closeTime\n timerange\n forbidQrValid\n renewTimeNext\n forbidRenewTime\n forbidWechatCancle\n }\n getSToken\n }\n currentUser {\n user_id\n user_nick\n user_mobile\n user_sex\n user_sch_id\n user_sch\n user_last_login\n user_avatar(size: MIDDLE)\n user_adate\n user_student_no\n user_student_name\n area_name\n user_deny {\n deny_deadline\n }\n sch {\n sch_id\n sch_name\n activityUrl\n isShowCommon\n isBusy\n }\n }\n }\n ad(pos: $pos, param: $param) {\n name\n pic\n url\n }\n}","variables":{"pos":"App-首页"}}
    date2={"operationName":"save","query":"mutation save($key: String!, $libid: Int!, $captchaCode: String, $captcha: String) {\n userAuth {\n prereserve {\n save(key: $key, libId: $libid, captcha: $captcha, captchaCode: $captchaCode)\n }\n }\n}","variables":{"key":seat,"libid":linid,"captchaCode":"","captcha":""}}
    date={"operationName":"prereserveCheckMsg","query":"query prereserveCheckMsg {\n userAuth {\n prereserve {\n prereserveCheckMsg\n }\n }\n}"}
    a = re.post(" https://wechat.v2.traceint.com/index.php/graphql/ ", headers=header, json=date3, verify=False)
    print(eval(a.text))
    hello('wss://wechat.v2.traceint.com/ws?ns=prereserve/queue')
    a = re.post(" https://wechat.v2.traceint.com/index.php/graphql/ ", headers=header, json=date2, verify=False)
    #  print(a.text)https://wechat.v2.traceint.com/index.php/graphql/%20
    b = eval(a.text)
    print(b)
