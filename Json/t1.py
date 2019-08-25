import json
import demjson
with open("Json/testjson.json", "r",encoding="utf-8") as f:
    txt = f.read()
    print(txt)
    # result = json.load(f)
    result = demjson.decode(txt)
    print(result)
    print(result["data"]["array"])
    f.close()