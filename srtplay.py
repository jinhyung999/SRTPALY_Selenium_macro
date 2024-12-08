from selenium import webdriver
from selenium.common import TimeoutException
# selenium라이브러리안에있는 service 임포트
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # 옵션 설정 (필요시)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#import pyautogui #마우스, 키보드 자동제어 패키지
#import pyperclip #클립보드
import login_info #아이디비밀번호 파일

def setup_driver():
    # 웹드라이버 경로 설정
    # driver_path = r"C:\Users\ADMIN\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe"#노트북
    driver_path = r"C:\Users\User\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe"  # PC
    # Service 객체로 WebDriver 설정
    service = Service(executable_path=driver_path)
    #브라우저 닫힘방지 옵션
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    # driver를 chrome브라우저로 설정
    # driver = webdriver.Chrome(service=service)
    return driver

def login(driver, user_id, password):
    driver.get("https://srtplay.com/user/idCheck")
    # id_element = driver.find_element(By.CSS_SELECTOR, "#input-email")
    # id_element.send_keys(user_id) 두줄짜리를 한줄로 요약
    # 아디디 입력란에 입력
    driver.find_element(By.CSS_SELECTOR, "#input-email").send_keys(user_id)
    # next_btn = driver.find_element(By.CSS_SELECTOR, "body > div.outer-wrap > div > div > form > div > div.end-content > div > button > span")
    # next_btn.click() 두줄짜리 코드 한줄로 요약
    #다음버튼 클릭
    driver.find_element(By.CSS_SELECTOR,"body > div.outer-wrap > div > div > form > div > div.end-content > div > button > span").click()
    driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div.form-type-wrap > div:nth-child(2) > span > span").click()
    #비밀번호 입력란에 입력
    driver.find_element(By.CSS_SELECTOR, "#input-pw").send_keys(password)  # 실제 비밀번호 필드 CSS 선택자
    driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div.end-content > div > button").click()


def booking_page(driver):
    #팝업없을때를 위한 예외처리
    try:
        # WebDriverWait와 expected_conditions을 사용하여 요소가 로드될 때까지 대기하는 방식
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#popup-noti-0 > div.pop-wrap > div > div.pop-footer > div > div > button"))).click()
    except TimeoutException:
        print("x")
    #팝업버튼 요소찾고 클릭
    driver.find_element(By.CSS_SELECTOR, "body > div.outer-wrap > div > div.content > div > div.list-category.st3 > ul > li:nth-child(1) > a").click()

def station_page(driver, departure_station, arrival_station):
    #출발역 검색후 선택완료 누르기
    departure_station_button = driver.find_element(By.CSS_SELECTOR, "#station-start")
    departure_station_button.click()
    time.sleep(1)#타임슬립을 안넣으면 자동으로 닫히 왜?일까
    search_input = driver.find_element(By.CSS_SELECTOR, "#station-pos-input")
    search_input.send_keys(departure_station)
    time.sleep(1)
    select_button1 = driver.find_element(By.CSS_SELECTOR, "#stationListArea > li > label")
    select_button1.click()
    select_button2 = driver.find_element(By.CSS_SELECTOR, "#stationDiv > div > div.pop-footer > div > button")
    select_button2.click()

    # 도착역 검색후 선택완료 누르기
    arrival_station_button = driver.find_element(By.CSS_SELECTOR, "#station-arrive")
    arrival_station_button.click()
    time.sleep(1)
    search_input = driver.find_element(By.CSS_SELECTOR, "#station-pos-input")
    search_input.send_keys(arrival_station)
    time.sleep(1)
    select_button3 = driver.find_element(By.CSS_SELECTOR, "#stationListArea > li > label")
    select_button3.click()
    select_button4 = driver.find_element(By.CSS_SELECTOR, "#stationDiv > div > div.pop-footer > div > button")
    select_button4.click()

def date_page(driver, departure_date, departure_time):
    calendar_button = driver.find_element(By.CSS_SELECTOR, "#ticketMainDiv > div:nth-child(2) > div.desc > div")
    calendar_button.click()
    time.sleep(1)
    #자바스크립트를 사용하여 캘린더페이지 출발날짜,시간 적용하기
    driver.execute_script(f"document.querySelector('div[data-id=\"{departure_date}\"] button').click();")
    driver.execute_script(f"document.querySelector('button[data-id=\"time-{departure_time}\"]').click();")
    calendar_select_button = driver.find_element(By.CSS_SELECTOR, "#calendarDiv > div > div.pop-footer.bg-light-gray > div.btn-wrap > button.btn-type1.st1")
    calendar_select_button.click()

def main():
    # 기본세팅
    # set_id='아이디를 입력해주세요'
    # set_pwd='비밀번호를 입력해주세요'
    set_departure_station = "대전"
    set_arrival_station = "수서"
    set_departure_date = "2024-12-11"
    set_departure_time = "16"

    driver = setup_driver()
    #login(driver, set_id, set_pwd)
    login(driver, login_info.set_id, login_info.set_pwd)
    booking_page(driver)
    station_page(driver, set_departure_station, set_arrival_station)
    date_page(driver, set_departure_date, set_departure_time)
    #자바스크립트로 조회하기버튼 누르기
    driver.execute_script("document.getElementById('ticketSearchBtn').click();")


if __name__ == "__main__":
    main()


"""
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
"""
