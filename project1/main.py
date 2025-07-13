# 컴퓨터의 외부 및 내부 IP 확인하기
import socket
import requests # 사이트에 접속하기 위한 모듈 불러오기
import re # IP주소를 찾기 위한 정규식을 사용하기 위한 모듈

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443)) # https의 기본 접속 포트 : 443
print("내부 IP : ", in_addr.getsockname()[0])

req = requests.get("https://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',req.text)[1]
print("외부 IP: ", out_addr) #외부 IP 주소를 출력