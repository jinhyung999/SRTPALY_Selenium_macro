# SRTPALY_Selenium_macro
This is an open-source automation SRT macro program.  
오픈 소스 자동화 SRT매크로 프로그램 입니다.  

It uses Python to automatically control the SRT reservation site, srtplay  
파이썬을 이용하여  SRT예매사이트 srtplay를 자동 제어합니다.  

**Commercial use is prohibited**  
**상업적 목적으로 이용 불가**
### License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).  
You may use, share, and adapt the code, but only for non-commercial purposes. Attribution is required.  
For full license details, see the [LICENSE](LICENSE) file.

***

# How To Run
Python 3.x: Python must be installed. If it's not installed, please download and install it from the official Python website.  
Chromedriver: You need to download and install the Chrome WebDriver for Selenium, matching your system's version. You can download it from the Chromedriver download page.    
Install required libraries: Use the command below to install the necessary libraries.  

Python 3.x: Python이 설치되어 있어야 합니다. 설치가 되어 있지 않다면 Python 공식 사이트에서 다운로드하고 설치해 주세요. 
Chromedriver: Selenium에서 사용할 Chrome 웹드라이버를 다운로드하고, 본인의 시스템에 맞는 버전을 설치해야 합니다. Chromedriver 다운로드 페이지에서 다운로드할 수 있습니다.  
필요한 라이브러리 설치: 아래 명령어로 필요한 라이브러리를 설치하세요.  

 ```python
pip install selenium requests
```

Please download the info.py from the repository and fill in the required values.  
To use the KakaoTalk message sending feature, please follow steps 1 to 4 in the guide from [[python] use kakao API, send kakaoTalk message to me](https://choi-hee-yeon.tistory.com/163)  
If you do not need the feature to send messages via KakaoTalk, you do not need to provide the kakao_id, kakao_pw, and rest_api_key values.  
레포지터리에 있는 info.py를 다운받고 필요한 값들을 넣어주세요.  
카카오톡 메세지 보내기 기능을 사용하려면 링크 [[python] 카카오톡 API를 사용하여, 나에게 카카오톡 메시지 보내기](https://choi-hee-yeon.tistory.com/163) 에서 1. 부터 4.까지의 부분을 따라 세팅해주세요.  
카카오톡으로 메시지 보내기 기능이 필요하지 않으시면 kakao_id, kakao_pw, rest_api_key 값을 작성하지 않으셔도 됩니다.    

If you have completed the setup, please run srtplay.py to start the booking process! Note: Please place info.py, kakao_send.py, and srtplay.py in the same folder.  
세팅을 다하셨다면 srtplay.py를 실행시켜주시면 예매가 시작됩니다! 주의: info.py, kakao_send.py, srtplay.py를 같은 폴더에 넣어주세요.  

### License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).  
You may use, share, and adapt the code, but only for non-commercial purposes. Attribution is required.  
For full license details, see the [LICENSE](LICENSE) file.
