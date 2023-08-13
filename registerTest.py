import requests as re
if __name__ == '__main__':
    true=True
    false=False
    null='null'
    header = {
        "cookie":"FROM_TYPE=weixin; v=5.5; Hm_lvt_7ecd21a13263a714793f376c18038a87=1691766975,1691851495; wechatSESS_ID=5dd45219472d53e965d102942361fd562669d29b8870847e; Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VySWQiOjI0OTc1MjUyLCJzY2hJZCI6MjAwNTgsImV4cGlyZUF0IjoxNjkxOTAzMDU0fQ.H4ip7F15HZkvIbvsFyNBO6Ruium3nYpMSh_WMEDlDE8xv_074NJO2B0ZvY51P81XcOhu8DlVcQ3eUolUIECOp3W8sxGct3-q4FvD6mK0_pUjs5rVPtFNm6ijDArF2-Zb51Y6kA12vHIqWgEFtue0WTdXWf34kwRDazQEJyWtVmLLl6fH4F8DMKs8qywPW5fY_JSBnJ_AdmWr0mDPNsf0Ocfg-wS-Tb14Hw03ufksDXfCvfu85OPPrceRA9MdeIlEVdKt36Qi8Q7_rzvs97nx8-Ct_gR3dJfw6efA9aRjd9wte57vjlA6BXKV0JSld25KEubaLnGvtFeakVp-WjZW3g; SERVERID=e3fa93b0fb9e2e6d4f53273540d4e924|1691895853|1691895850"
 }
    import asyncio
    import websockets


    async def hello(uri):
        async with websockets.connect(uri) as websocket:
            try:
                while (1):
                    await websocket.send(str({"ns": "prereserve/queue", "msg": ""}))
                    recv_text = await websocket.recv()
                    print(recv_text)
            except websockets.ConnectionClosed:
                print("closed")

#{"ns":"prereserve\/queue","msg":"\u6392\u961f\u6210\u529f\uff01\u8bf7\u57282\u5206\u949f\u5185\u9009\u62e9\u5ea7\u4f4d\uff0c\u5426\u5219\u9700\u8981\u91cd\u65b0\u6392\u961f\u3002","code":0,"data":0}
    # wechat.v2.traceint.com/ws?ns=prereserve/queue
    asyncio.get_event_loop().run_until_complete(
        hello('ws://wechat.v2.traceint.com/ws?ns=prereserve/queue'))
    date3={"operationName":"index","query":"query index($pos: String!, $param: [hash]) {\n userAuth {\n oftenseat {\n list {\n id\n info\n lib_id\n seat_key\n status\n }\n }\n message {\n new(from: \"system\") {\n has\n from_user\n title\n num\n }\n indexMsg {\n message_id\n title\n content\n isread\n isused\n from_user\n create_time\n }\n }\n reserve {\n reserve {\n token\n status\n user_id\n user_nick\n sch_name\n lib_id\n lib_name\n lib_floor\n seat_key\n seat_name\n date\n exp_date\n exp_date_str\n validate_date\n hold_date\n diff\n diff_str\n mark_source\n isRecordUser\n isChooseSeat\n isRecord\n mistakeNum\n openTime\n threshold\n daynum\n mistakeNum\n closeTime\n timerange\n forbidQrValid\n renewTimeNext\n forbidRenewTime\n forbidWechatCancle\n }\n getSToken\n }\n currentUser {\n user_id\n user_nick\n user_mobile\n user_sex\n user_sch_id\n user_sch\n user_last_login\n user_avatar(size: MIDDLE)\n user_adate\n user_student_no\n user_student_name\n area_name\n user_deny {\n deny_deadline\n }\n sch {\n sch_id\n sch_name\n activityUrl\n isShowCommon\n isBusy\n }\n }\n }\n ad(pos: $pos, param: $param) {\n name\n pic\n url\n }\n}","variables":{"pos":"App-首页"}}
    date2={"operationName":"save","query":"mutation save($key: String!, $libid: Int!, $captchaCode: String, $captcha: String) {\n userAuth {\n prereserve {\n save(key: $key, libId: $libid, captcha: $captcha, captchaCode: $captchaCode)\n }\n }\n}","variables":{"key":"43,16","libid":114240,"captchaCode":"","captcha":""}}
    date={"operationName":"prereserveCheckMsg","query":"query prereserveCheckMsg {\n userAuth {\n prereserve {\n prereserveCheckMsg\n }\n }\n}"}
    a = re.post(" https://wechat.v2.traceint.com/index.php/graphql/ ", headers=header, json=date3, verify=False)
    print(eval(a.text))
    a = re.post(" https://wechat.v2.traceint.com/index.php/graphql/ ", headers=header, json=date2, verify=False)
    #  print(a.text)https://wechat.v2.traceint.com/index.php/graphql/%20
    b = eval(a.text)
    print(b)
