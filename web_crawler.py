import requests
from bs4 import BeautifulSoup
import json

json_str = """
[
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2330",
    "CommName": "台積電",
    "Type": "股票",
    "Weights": 47.01,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2317",
    "CommName": "鴻海",
    "Type": "股票",
    "Weights": 4.82,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2454",
    "CommName": "聯發科",
    "Type": "股票",
    "Weights": 4.32,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2308",
    "CommName": "台達電",
    "Type": "股票",
    "Weights": 2.54,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2303",
    "CommName": "聯電",
    "Type": "股票",
    "Weights": 2.15,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2412",
    "CommName": "中華電",
    "Type": "股票",
    "Weights": 1.67,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "1303",
    "CommName": "南亞",
    "Type": "股票",
    "Weights": 1.66,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2881",
    "CommName": "富邦金",
    "Type": "股票",
    "Weights": 1.64,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2891",
    "CommName": "中信金",
    "Type": "股票",
    "Weights": 1.56,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2002",
    "CommName": "中鋼",
    "Type": "股票",
    "Weights": 1.41,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2882",
    "CommName": "國泰金",
    "Type": "股票",
    "Weights": 1.39,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2886",
    "CommName": "兆豐金",
    "Type": "股票",
    "Weights": 1.35,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "1301",
    "CommName": "台塑",
    "Type": "股票",
    "Weights": 1.31,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "3711",
    "CommName": "日月光投控",
    "Type": "股票",
    "Weights": 1.3,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2884",
    "CommName": "玉山金",
    "Type": "股票",
    "Weights": 1.29,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "1216",
    "CommName": "統一",
    "Type": "股票",
    "Weights": 1.24,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2892",
    "CommName": "第一金",
    "Type": "股票",
    "Weights": 1.06,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "5880",
    "CommName": "合庫金",
    "Type": "股票",
    "Weights": 1.05,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "5871",
    "CommName": "中租-KY",
    "Type": "股票",
    "Weights": 1.03,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2885",
    "CommName": "元大金",
    "Type": "股票",
    "Weights": 1.01,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "1326",
    "CommName": "台化",
    "Type": "股票",
    "Weights": 0.99,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "3008",
    "CommName": "大立光",
    "Type": "股票",
    "Weights": 0.94,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2880",
    "CommName": "華南金",
    "Type": "股票",
    "Weights": 0.89,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2883",
    "CommName": "開發金",
    "Type": "股票",
    "Weights": 0.84,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "1101",
    "CommName": "台泥",
    "Type": "股票",
    "Weights": 0.8,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2207",
    "CommName": "和泰車",
    "Type": "股票",
    "Weights": 0.78,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "3037",
    "CommName": "欣興",
    "Type": "股票",
    "Weights": 0.78,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2382",
    "CommName": "廣達",
    "Type": "股票",
    "Weights": 0.76,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2357",
    "CommName": "華碩",
    "Type": "股票",
    "Weights": 0.73,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2327",
    "CommName": "國巨",
    "Type": "股票",
    "Weights": 0.72,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2890",
    "CommName": "永豐金",
    "Type": "股票",
    "Weights": 0.72,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "3034",
    "CommName": "聯詠",
    "Type": "股票",
    "Weights": 0.69,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2887",
    "CommName": "台新金",
    "Type": "股票",
    "Weights": 0.66,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "6415",
    "CommName": "矽力*-KY",
    "Type": "股票",
    "Weights": 0.66,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "3045",
    "CommName": "台灣大",
    "Type": "股票",
    "Weights": 0.65,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "5876",
    "CommName": "上海商銀",
    "Type": "股票",
    "Weights": 0.63,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2379",
    "CommName": "瑞昱",
    "Type": "股票",
    "Weights": 0.61,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2603",
    "CommName": "長榮",
    "Type": "股票",
    "Weights": 0.61,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2912",
    "CommName": "統一超",
    "Type": "股票",
    "Weights": 0.6,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "1590",
    "CommName": "亞德客-KY",
    "Type": "股票",
    "Weights": 0.53,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "202212TX",
    "CommName": "臺股期貨",
    "Type": "期貨",
    "Weights": 0.53,
    "Value": 0,
    "Unit": "口",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2395",
    "CommName": "研華",
    "Type": "股票",
    "Weights": 0.52,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2409",
    "CommName": "友達",
    "Type": "股票",
    "Weights": 0.47,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2801",
    "CommName": "彰銀",
    "Type": "股票",
    "Weights": 0.45,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "6505",
    "CommName": "台塑化",
    "Type": "股票",
    "Weights": 0.45,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2609",
    "CommName": "陽明",
    "Type": "股票",
    "Weights": 0.44,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "4904",
    "CommName": "遠傳",
    "Type": "股票",
    "Weights": 0.43,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2615",
    "CommName": "萬海",
    "Type": "股票",
    "Weights": 0.41,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "9910",
    "CommName": "豐泰",
    "Type": "股票",
    "Weights": 0.32,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "8046",
    "CommName": "南電",
    "Type": "股票",
    "Weights": 0.22,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "2408",
    "CommName": "南亞科",
    "Type": "股票",
    "Weights": 0.2,
    "Value": 0,
    "Unit": "股",
    "Amount": -2147483648,
    "Currency": ""
  },
  {
    "Date": "2022-11-18T00:00:00",
    "CommKey": "202212NYF",
    "CommName": "台灣50ETF股票期貨",
    "Type": "期貨",
    "Weights": 0.17,
    "Value": 0,
    "Unit": "口",
    "Amount": -2147483648,
    "Currency": ""
  }
]
"""
def get_stocks_0050():
    stocks_0050 = []
    json_dict = json.loads(json_str)
    for i in json_dict:
        stocks_0050.append(i['CommKey'])
    return stocks_0050