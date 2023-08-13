import json

import requests as re
if __name__ == '__main__':
    #get the librarys
    header = {
        "cookie":"FROM_TYPE=weixin; v=5.5; wechatSESS_ID=5eacd640c8e3b4cf11426675dab96d92d3ea318f42c5f456; Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VySWQiOjI0OTc1MjUyLCJzY2hJZCI6MjAwNTgsImV4cGlyZUF0IjoxNjkxNzcxODUzfQ.T_O6elg2d-YJ3_Thbm28idHoU4gaaktdhvUEWNxdv37MbRN7ejcbLtJAIs0lOGAY_-bS-WM-8AxV1BIjcsfvy3tJd8SZBVrGWCE8NcCGsKmIhrY-ONsYtiOGs0ENShs8SIum5io3Ul3R9fdvHEa5vX6EEdFvJJrIDIx0viqhrAYotv09YV9vssK6A55fh-4NCc9oF7JtjweXYq1_AHbc3V3n6gt5sFM2WE6lCJN7vjcq3Dxh_0oLf5zTho74UIwhmFz55Y_C4QAXLWCriz421DWVF8kmV5Wh3ojeFehgpIxcrksi0CnwzgtLEtTOYCqWlKwmscICSstxiOUevmNYFg; Hm_lvt_7ecd21a13263a714793f376c18038a87=1691712716,1691714289,1691720961,1691764652; Hm_lpvt_7ecd21a13263a714793f376c18038a87=1691764652; SERVERID=82967fec9605fac9a28c437e2a3ef1a4|1691764676|1691764649"
    }
    true=True
    false=False
    null='null'
    date={"operationName":"list","query":"query list {\n userAuth {\n reserve {\n libs(libType: -1) {\n lib_id\n lib_floor\n is_open\n lib_name\n lib_type\n lib_group_id\n lib_comment\n lib_rt {\n seats_total\n seats_used\n seats_booking\n seats_has\n reserve_ttl\n open_time\n open_time_str\n close_time\n close_time_str\n advance_booking\n }\n }\n libGroups {\n id\n group_name\n }\n reserve {\n isRecordUser\n }\n }\n record {\n libs {\n lib_id\n lib_floor\n is_open\n lib_name\n lib_type\n lib_group_id\n lib_comment\n lib_color_name\n lib_rt {\n seats_total\n seats_used\n seats_booking\n seats_has\n reserve_ttl\n open_time\n open_time_str\n close_time\n close_time_str\n advance_booking\n }\n }\n }\n rule {\n signRule\n }\n }\n}"}
    date2={"operationName":"libLayout","query":"query libLayout($libId: Int, $libType: Int) {\n userAuth {\n reserve {\n libs(libType: $libType, libId: $libId) {\n lib_id\n is_open\n lib_floor\n lib_name\n lib_type\n lib_layout {\n seats_total\n seats_booking\n seats_used\n max_x\n max_y\n seats {\n x\n y\n key\n type\n name\n seat_status\n status\n }\n }\n }\n }\n }\n}"}#"variables":{"libId":114243}
    date3={"operationName":"index","query":"query index($url: String!, $pos: String!, $param: [hash]) {\n userAuth {\n reserve {\n reserve {\n token\n status\n user_id\n user_nick\n sch_id\n sch_name\n lib_id\n lib_name\n lib_floor\n seat_name\n }\n qrUrl\n weixiao {\n isOpen\n url\n pic\n }\n }\n webSocket {\n url\n qrType\n protocol\n }\n config: user {\n notSign: getSchConfig(fields: \"reserve.notSign\")\n blueSignOpen: getSchConfig(fields: \"adm.blueSignOpen\")\n doorSignOpen: getSchConfig(fields: \"adm.doorSignOpen\")\n doorSignURL: getSchConfig(fields: \"adm.doorSignURL\")\n forbidQrValid: getSchConfig(fields: \"forbidQrValid\", extra: true)\n }\n }\n wechatJSSDK(url: $url) {\n appId\n timestamp\n nonceStr\n signature\n }\n ad(pos: $pos, param: $param) {\n name\n pic\n url\n }\n}","variables":{"url":"https://web.traceint.com/web/index.html","pos":"047"}}
    date4={"operationName":"reserueSeat","query":"mutation reserueSeat($libId: Int!, $seatKey: String!, $captchaCode: String, $captcha: String!) {\n userAuth {\n reserve {\n reserueSeat(\n libId: $libId\n seatKey: $seatKey\n captchaCode: $captchaCode\n captcha: $captcha\n )\n }\n }\n}","variables":{"seatKey":"20,31","libId":114240,"captchaCode":"","captcha":""}}
    a=re.post(" https://wechat.v2.traceint.com/index.php/graphql/ ",headers=header,json=date2,verify=False)
  #  print(a.text)https://wechat.v2.traceint.com/index.php/graphql/%20
    b=eval(a.text)
#    print(b)
    libs=b['data']['userAuth']['reserve']['libs']
    for li in libs:
        if (li['is_open']==True):
            print(li['lib_id'], end=',')
            print(li['lib_name'], end=',')
            print(li['lib_type'])
            seats=li['lib_layout']['seats']
            with open(li['lib_name']+".txt",'w+') as file:
                for se in seats:
                    print(se['key'], end=':')
                    print(se['name'], end='\t')
                    file.write(se['key'])
                    file.write(":")
                    file.write(se['name'])
                    file.write(":")
                    file.write(str(se['seat_status']))
                    file.write("\n")
            print(seats)

    with open("a.json",'w+') as file:
        file.write(str(libs[8]).replace('\'','\"'))

    a=re.post(" https://wechat.v2.traceint.com/index.php/graphql/ ",headers=header,json=date4,verify=False)
    print(eval(a.text))
    a = re.post(" https://wechat.v2.traceint.com/index.php/graphql/ ", headers=header, json=date3, verify=False)
    print(eval(a.text))
