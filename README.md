# SRTPALY_Selenium_macro
This is an open-source automation SRT macro program.  
오픈 소스 자동화 SRT매크로 프로그램 입니다.  

It uses Python to automatically control the SRT reservation site, srtplay  
파이썬을 이용하여  SRT예매사이트 srtplay를 자동 제어합니다.  

## How To Run
Python 3.x: Python must be installed. If it's not installed, please download and install it from the official Python website.  
Chromedriver: You need to download and install the Chrome WebDriver for Selenium, matching your system's version. You can download it from the Chromedriver download page.  
Install required libraries: Use the command below to install the necessary libraries.  

Python 3.x: Python이 설치되어 있어야 합니다. 설치가 되어 있지 않다면 Python 공식 사이트에서 다운로드하고 설치해 주세요. 
Chromedriver: Selenium에서 사용할 Chrome 웹드라이버를 다운로드하고, 본인의 시스템에 맞는 버전을 설치해야 합니다. Chromedriver 다운로드 페이지에서 다운로드할 수 있습니다.  
필요한 라이브러리 설치: 아래 명령어로 필요한 라이브러리를 설치하세요.  

**pip install selenium requests**

Please download the info.py from the repository and fill in the required values.
If you do not need the feature to send messages via KakaoTalk, you do not need to provide the kakao_id, kakao_pw, and rest_api_key values.  
레포지터리에 있는 info.py를 다운받고 필요한 값들을 넣어주세요.  
카카오톡으로 메시지 보내기 기능이 필요하지 않으시면 kakao_id, kakao_pw, rest_api_key 값을 작성하지 않으셔도 됩니다.  

### License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).  
You may use, share, and adapt the code, but only for non-commercial purposes. Attribution is required.  
For full license details, see the [LICENSE](LICENSE) file.
