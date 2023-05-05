# -*- coding:utf-8 -*-

import openai


def main():
   openai.api_key = "一定要换成你的api_key！"
   messages = []
   while True:
       msg = ""
       print("请输入你的问题：", end="")
       msg = input()
       messages.append(
           {"role": "user", "content": msg}
       )
       completion = openai.ChatCompletion.create(
         model="gpt-3.5-turbo",
         messages=messages
       )
       print(completion.choices[0].message.content)
       print('使用token：' + str(completion.usage.total_tokens))


if __name__ == '__main__':
   main() 作者：晓龙coding https://www.bilibili.com/read/cv22278818?from=search&spm_id_from=333.337.0.0 出处：bilibili
