from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Service 임포트
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # 옵션 설정 (필요시)

# 웹드라이버 경로 설정
driver_path = r"C:\Users\ADMIN\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Service 객체로 WebDriver 설정
service = Service(executable_path=driver_path)

# 3. 브라우저 열기
driver = webdriver.Chrome(service=service)

# 1. srtplay login페이지 열기
url = "https://srtplay.com/user/idCheck"
driver.get(url)

# 5. 웹페이지 제목 출력
print("웹페이지 제목:", driver.title)

# 6. 페이지 로드 후 몇 초 기다리기
import time
time.sleep(5)  # 5초 대기

# 브라우저 종료를 원하지 않으면 이 코드를 생략
driver.quit()
