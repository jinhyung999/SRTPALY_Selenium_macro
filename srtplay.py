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
from datetime import datetime

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
        start_time = datetime.strptime(start_time_str, "%H:%M")

        # 시간 비교 (set_deadline_time보다 앞인지 확인)
        if start_time >= deadline_time:
            print("지정시간 초과 재탐색")
            break  # 다음 요소로 진행

        # 버튼 찾기 (class="btn btn-normal disabled"나 class="btn btn-sale disabled"이 아닌 버튼 찾기)
        buttons = train_schedule.find_elements(By.CSS_SELECTOR, "a.btn")

        for button in reversed(buttons):
            # 비활성화된 버튼은 건너뛰기
            if "disabled" in button.get_attribute("class"):
                continue
            # 버튼 클릭
            href = button.get_attribute("href")
            if href:
                button.click()
                find_flag = True
                break


    if find_flag:
        print("버튼 클릭 완료")
    else:
        print("버튼을 찾지 못했습니다.")
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
                print("예매 가능한 버튼이 없습니다. 페이지를 새로고침합니다.")
                driver.refresh()
                time.sleep(1)
                continue

        except Exception as e:
            print(f"오류 발생: {e}")
            break

def done_booking(driver):
    # 'sale-ticket'을 가진 div 요소 찾기
    sale_ticket_div = driver.find_element(By.CSS_SELECTOR, "div.fixed-footer-wrap[data-id='sale-ticket']")
    # 'normal-ticket'을 가진 div 요소 찾기
    normal_ticket_div = driver.find_element(By.CSS_SELECTOR, "div.fixed-footer-wrap[data-id='normal-ticket']")

    try:
        sale_button = sale_ticket_div.find_element(By.LINK_TEXT, "티플승차권 예약하기")
        sale_button.click()

    except Exception as e:
        # '일반승차권 예약하기' 버튼 클릭 (normal-ticket div)
        normal_button = normal_ticket_div.find_element(By.LINK_TEXT, "일반승차권 예약하기")
        normal_button.click()
    #좌석 자동배정버튼 찾고 클릭가능해지면 클릭
    buy_seat = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='좌석 자동배정']"))
    )
    buy_seat.click()

def main():
    # ------------- 기본세팅-----------------------
    # set_id='아이디를 입력해주세요'      #아이디
    # set_pwd='비밀번호를 입력해주세요'   #비밀번호
    set_departure_station = "대전"    #출발역
    set_arrival_station = "수서"      #도착역
    set_departure_date = "2024-12-14"#출발날짜
    set_departure_time = "23"        #기차출발시간
    set_deadline_time = "23:59"      # 예약 가능한 마지막 출발 시간
    # ------------- 기본세팅-----------------------

    if ':' not in set_deadline_time:  # 만약 ':'이 없다면
        if len(set_deadline_time) == 1:  # 한 자릿수 숫자인 경우
            set_deadline_time = "0" + set_deadline_time + ":00"  # 앞에 0을 추가하고 :00을 붙임
        else:
            set_deadline_time += ":00"
    set_deadline_time = datetime.strptime(set_deadline_time, "%H:%M")

    driver = setup_driver()
    #login(driver, set_id, set_pwd)
    login(driver, login_info.set_id, login_info.set_pwd)
    booking_page(driver)
    station_page(driver, set_departure_station, set_arrival_station)
    date_page(driver, set_departure_date, set_departure_time)
    driver.execute_script("document.getElementById('ticketSearchBtn').click();")#자바스크립트로 조회하기버튼 누르기
    booking_loop(driver, set_deadline_time)
    done_booking(driver)


    print("good")

if __name__ == "__main__":
    main()



# def find_and_click_button(driver, start_time, end_time):
#     script = """
#     function findAndClickButton(startTime, endTime) {
#         const buttons = Array.from(document.querySelectorAll('button[data-id]'));
#         for (const button of buttons) {
#             const timeAttr = button.getAttribute('data-id');
#             if (!timeAttr) continue;
#
#             const time = parseInt(timeAttr.replace('time-', ''), 10);
#             if (time >= startTime && time <= endTime && !button.disabled) {
#                 button.scrollIntoView({ behavior: 'smooth', block: 'center' });
#                 button.click();
#                 return true; // 버튼을 클릭하면 true 반환
#             }
#         }
#         return false; // 클릭 가능한 버튼이 없으면 false 반환
#     }
#     return findAndClickButton(arguments[0], arguments[1]);
#     """
#     return driver.execute_script(script, start_time, end_time)