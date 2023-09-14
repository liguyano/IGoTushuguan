import json
import sys

json_file_path = "config1.json"

# 读取 JSON 文件并将其解析为 JSON 对象
with open(json_file_path, "r") as json_file:
    json_data = json.load(json_file)
if len(sys.argv)>1:
    print(sys.argv[1])
    json_data['header']['Cookie']=sys.argv[1]
    json_data['queue_header']['Cookie']=sys.argv[1]
else:
    # 打印 JSON 对象
    print(json_data['header']['Cookie'])
with open(json_file_path, "w+") as json_file:
    json.dump(json_data, json_file, indent=4)
