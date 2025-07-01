# 컴퓨터의 외부 및 내부 IP 확인하기
import requests # 사이트에 접속하기 위한 모듈 불러오기
import re # IP주소를 찾기 위한 정규식을 사용하기 위한 모듈

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443)) # https의 기본 접속 포트 : 443
print("내부 IP : ", in_addr.getsockname()[0])

req = requests.get("https://ipconfig.kr")