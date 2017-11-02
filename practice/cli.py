"""参数1 城市中文名 参数2 可选: 今天, 昨天, 预测"""
from pprint import pprint

import requests, sys

if __name__ == "__main__":
    # sys.argv 返回[] 0为命令 1开始为依次的参数
    try:
        city = sys.argv[1]
    # 接受错误 给出默认值
    except Exception:  # IndexError:
        city = "上海"
    try:
        day = sys.argv[2]
    except Exception:
        day = "今天"
    # requests自带直接解析json，返回一个{}
    # 1： %格式化
    # info = requests.get("http://www.sojson.com/open/api/weather/json.shtml?city=%s" % city).json()
    # 2： format格式化，推介这个
    info = requests.get("http://www.sojson.com/open/api/weather/json.shtml?city=%s".format(city)).json()
    # 3： format字符串， 版本3.60+
    # info = requests.get(f'http://www.sojson.com/open/api/weather/json.shtml?city={city}').json()
    if day == "今天":
        # pprint是格式化输出，有兴趣可以看看源码。
        pprint(info, depth=2)
    elif day == "昨天":
        pprint(info['data']['yesterday'])
    elif day == "预测":
        pprint(info['data']['forecast'])
    else:
        pprint("大熊你是想刁难我胖虎 ?_?")
