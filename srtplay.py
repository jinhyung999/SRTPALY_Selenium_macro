from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.alert import Alert#팝업창 제어
from selenium.common import TimeoutException
# selenium라이브러리안에있는 service 임포트
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # 옵션 설정 (필요시)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import info #아이디비밀번호 파일


def setup_driver():
    # 웹드라이버 경로 설정
    # driver_path = r"C:\Users\ADMIN\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe"#노트북
    driver_path = info.driver_path  # PC
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
    driver.execute_script(f"document.querySelector('button[data-id=\"time-{departure_time[:2]}\"]').click();")
    calendar_select_button = driver.find_element(By.CSS_SELECTOR, "#calendarDiv > div > div.pop-footer.bg-light-gray > div.btn-wrap > button.btn-type1.st1")
    calendar_select_button.click()

def find_booking_elements(driver, deadline_time):
    # <li> 요소들을 찾기
    train_schedule_elements = driver.find_elements(By.CSS_SELECTOR, "li#trainScheduleListLi")
    # for문 종료를 위한 find_flag변수
    find_flag = False
    # 요소 순차적으로 확인
    for train_schedule in train_schedule_elements:
        # 버튼 클릭되면 flag=True가 되면서 for루프 종료
        if find_flag == True:
            break
        # 시간 확인 (start 클래스의 시간 추출)
        start_time_str = train_schedule.find_element(By.CSS_SELECTOR, ".start").text
        # 시간 비교를위해 datetime 객체로 형변환
        start_time = datetime.strptime(start_time_str, "%H:%M")

        # 시간 비교 (set_deadline_time보다 앞인지 확인)
        if start_time >= deadline_time:
            print("지정시간 초과 재탐색")
            break  # 다음 요소로 진행

        # 버튼 찾기 (class="btn btn-normal disabled"나 class="btn btn-sale disabled"이 아닌 버튼 찾기)
        buttons = train_schedule.find_elements(By.CSS_SELECTOR, "a.btn")
        # 버튼배열이 ['일반티켓버튼', '할인티켓버튼'] 이렇게 저장되므로 할인티켓을 먼저예매하기위해 reversed()사용
        for button in reversed(buttons):
            # 비활성화된 버튼은 건너뛰기
            if "disabled" in button.get_attribute("class"):
                continue
            # href의 속성값 받아오기
            href = button.get_attribute("href")
            if href:
                button.click()
                find_flag = True
                break

    return find_flag

def booking_loop(driver, set_time):
    while True:
        try:
            #li#trainScheduleListLi 요소 읽어올수있을때 까지 기다리기
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "li#trainScheduleListLi")))
            clicked = find_booking_elements(driver, set_time)
            if clicked:
                print("예매 성공!")
                break
            else:
                # print("예매 가능한 버튼이 없습니다. 페이지를 새로고침합니다.")
                # 새로고침
                driver.refresh()
                # 서버에 과부화를 주지않기위해 타임슬립
                time.sleep(1)
                continue

        except Exception as e:
            print(e)
            break

def done_booking(driver):
    # 'sale-ticket'을 가진 div 요소와 'normal-ticket'을 가진 div 요소 찾기
    sale_ticket_div = driver.find_element(By.CSS_SELECTOR, "div.fixed-footer-wrap[data-id='sale-ticket']")
    normal_ticket_div = driver.find_element(By.CSS_SELECTOR, "div.fixed-footer-wrap[data-id='normal-ticket']")
    #우선적으로 할인티켓을 먼저 클릭시도 만약 없으면 일반티켓 클릭
    try:
        # '티플승차권 예약하기' 버튼 클릭
        sale_button = sale_ticket_div.find_element(By.LINK_TEXT, "티플승차권 예약하기")
        sale_button.click()

    except Exception as e:
        # '일반승차권 예약하기' 버튼 클릭 (normal-ticket div)
        normal_button = normal_ticket_div.find_element(By.LINK_TEXT, "일반승차권 예약하기")
        normal_button.click()
    # 좌석 자동배정버튼 찾고 클릭가능해지면 클릭
    buy_seat = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='좌석 자동배정']"))
    )
    buy_seat.click()


def handle_alert(driver):
    try:
        # alert() 팝업이 나타날 경우 처리
        alert = Alert(driver)
        alert.accept()  # "확인" 버튼 클릭
        print("Alert 팝업이 닫혔습니다.")
        return True
    except Exception as e:
        # alert() 팝업이 없으면 예외 발생, None 반환
        return False

def main():
    if ':' not in info.set_deadline_time:  # 만약 ':'이 없다면
        if len(info.set_deadline_time) == 1:  # 한 자릿수 숫자인 경우
            set_deadline_time = "0" + info.set_deadline_time + ":00"  # 앞에 0을 추가하고 :00을 붙임
        else:
            info.set_deadline_time += ":00"
    set_deadline_time = datetime.strptime(info.set_deadline_time, "%H:%M")

    driver = setup_driver()
    login(driver, info.set_id, info.set_pwd)
    booking_page(driver)
    station_page(driver, info.set_departure_station, info.set_arrival_station)
    date_page(driver, info.set_departure_date, info.set_departure_time)
    driver.execute_script("document.getElementById('ticketSearchBtn').click();")#자바스크립트로 조회하기버튼 누르기
    booking_loop(driver, set_deadline_time)
    done_booking(driver)
    # 10초 동안 팝업이 나타나는지 확인
    start_time = time.time()
    while time.time() - start_time < 10:
        if handle_alert(driver):  # 팝업이 있으면 처리
            # 팝업이 닫힌 후, https://srtplay.com/ticket/reservation URL로 돌아올 때까지 대기
            while driver.current_url != "https://srtplay.com/ticket/reservation":
                time.sleep(1)  # 1초 대기 후 확인

            # 팝업이 나왔으면 station_page부터 다시 진행
            station_page(driver, info.set_departure_station, info.set_arrival_station)
            date_page(driver, info.set_departure_date, info.set_departure_time)
            driver.execute_script("document.getElementById('ticketSearchBtn').click();")  # 자바스크립트로 조회하기 버튼 누르기
            booking_loop(driver, set_deadline_time)
            done_booking(driver)
        else:
            break

if __name__ == "__main__":
    main()