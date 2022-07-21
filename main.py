import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

# Jsonファイルを読み込む
file = open('info.json', 'r')
info =  json.load(file)

# CHANNNEL_ACCESS_TOKENを読み込む
CHANNNEL_ACCESS_TOKEN =  info['CHANNNEL_ACCESS_TOKEN']

# インスタンス化
line_bot_api = LineBotApi(CHANNNEL_ACCESS_TOKEN)

def main():
    USER_ID =  info['USER_ID']
    messages = TextSendMessage(text='おはよう〜 \n今日も君の事を考えるだけで濡れちゃう♡')
    line_bot_api.push_message(USER_ID, messages=messages)

if __name__ ==  '__main__':
    main()