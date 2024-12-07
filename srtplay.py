from selenium import webdriver
# selenium라이브러리안에있는 service 임포트
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # 옵션 설정 (필요시)
import time
import pyautogui #마우스, 키보드 자동제어 패키지
import pyperclip #클립보드
import login_info #아이디비밀번호 파일

#기본세팅
#set_id='아이디를 입력해주세요'
#set_pwd='비밀번호를 입력해주세요'

# 웹드라이버 경로 설정
#driver_path = r"C:\Users\ADMIN\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe"#노트북
driver_path = r"C:\Users\User\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe"#PC

#Chrome 옵션설정
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)#브라우저 닫힘방지 옵션
# Service 객체로 WebDriver 설정
service = Service(executable_path=driver_path)

# driver를 chrome브라우저로 설정
driver = webdriver.Chrome(service=service)

# 1. driver.get()메서드 이용하여 srtplay login페이지 열기
url = "https://srtplay.com/user/idCheck"
driver.get(url)

#아이디 입력창찾기 및 입력
id = driver.find_element(By.CSS_SELECTOR,"#input-email")
id.click()
id.send_keys(login_info.set_id)
btn1 = driver.find_element(By.CSS_SELECTOR,"body > div.outer-wrap > div > div > form > div > div.end-content > div > button > span")#btn1 다음버튼
btn1.click()

#비밀번호 입력창찾기 및 입력
pwd = driver.find_element(By.CSS_SELECTOR,"#loginForm > div > div.form-type-wrap > div:nth-child(2) > span > span")
pwd.click()
time.sleep(2)#클릭이 잘될때까지 대기
#이유가 왜인지는 모르겠지만 패스워드를 바로 때려넣으면 입력이안됨 짐작으로는 너무빨리 작성하여서 그런것?
#해결책으로 패스워드를 클립보드에 카피하여 붙여넣기... 성공
pyperclip.copy(login_info.set_pwd)
pyautogui.hotkey("ctrl", "v")
btn2 = driver.find_element(By.CSS_SELECTOR,"#loginForm > div > div.end-content > div > button")#btn2 로그인버튼
btn2.click()
time.sleep(2)
#팝업창 클릭
btn3 = driver.find_element(By.CSS_SELECTOR,"#popup-noti-0 > div.pop-wrap > div > div.pop-footer > div > div > button")
btn3.click()
time.sleep(2)
#승차권 예매 페이지(btn4) 클릭
btn4 = driver.find_element(By.CSS_SELECTOR,"body > div.outer-wrap > div > div.content > div > div.list-category.st3 > ul > li:nth-child(1) > a")
btn4.click()
time.sleep(2)

time.sleep(5)
driver.quit()
