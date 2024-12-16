from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from urllib.parse import urlparse, parse_qs
import requests
import json
import info
# 카카오 인증 정보
rest_api_key = "카카오 REST API 키"  # 카카오 REST API 키
redirect_uri = "https://example.com/oauth"  # 설정한 Redirect URI
authorize_url = f"https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={rest_api_key}&redirect_uri={redirect_uri}"
service = Service(info.driver_path)  # Chromedriver 경로
driver = webdriver.Chrome(service=service)

def get_kakao_auth_code():
    # 카카오 인증 페이지로 이동
    driver.get(authorize_url)

    driver.find_element(By.CSS_SELECTOR, "#loginId--1").send_keys(info.kakao_id)
    driver.find_element(By.CSS_SELECTOR, "#password--2").send_keys(info.kakao_pw)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#mainContent > div > div > form > div.confirm_btn > button.btn_g.highlight.submit").click()

    # Redirect URI로 리다이렉트될 때까지 대기
    WebDriverWait(driver, 10).until(EC.url_contains(redirect_uri))
    # 현재 URL에서 Authorization Code 추출
    current_url = driver.current_url
    parsed_url = urlparse(current_url)
    query_params = parse_qs(parsed_url.query)
    auth_code = query_params.get("code", [None])[0]

    if auth_code:
        print("Authorization Code 발급 성공:", auth_code)
        return auth_code
    else:
        print("Authorization Code 발급 실패")
        return None

def get_access_token(auth_code):
    token_url = "https://kauth.kakao.com/oauth/token"
    token_data = {
        "grant_type": "authorization_code",
        "client_id": rest_api_key,
        "redirect_uri": redirect_uri,
        "code": auth_code,
    }
    token_response = requests.post(token_url, data=token_data)
    token_json = token_response.json()

    if "access_token" in token_json:
        print("액세스 토큰 발급 성공!")
        return token_json["access_token"]
    else:
        print("액세스 토큰 발급 실패:", token_json)
        return None

def send_kakao_message(access_token, message):
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    data = {
        "template_object": json.dumps({
            "object_type": "text",
            "text": message,
            "link": {
                "web_url": "http://example.com",
                "mobile_web_url": "http://example.com"
            }
        }),
    }

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print("메시지 전송 성공!")
    else:
        print("메시지 전송 실패:", response.json())
