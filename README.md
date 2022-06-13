# scriptlang

1. noti.py
- 용도: 봇 서버와 통신
- getStr 함수: 문자열 내용이 있을 때 사용
- getData 함수: 텔레그램에서 입력된 카테고리에 따라 얻어온 Open API의 데이터를 리턴
- sendMessage 함수: 메시지 전송

2. teller.py
- 용도: 사용자 입력에 대응 (메인 모듈)
- replyData 함수: noti에서 받아온 데이터를 응답 메시지로 전송
- handle 함수: 사용자 입력 내용을 구분하여 받아오고 도움말 메시지를 전송

3. graph.py
- 용도: 그래프 출력과 연관된 함수
- drawGraph 함수: 그래프를 프로그램 상에 그리는 함수

4. image.py
- 용도: 이미지 설정 클래스
- ImageLabel 클래스: 입력된 이미지를 라벨로 출력, 카테고리에 따라 변경되는 이미지 구현에 사용
- ImageButton 클래스: 입력된 이미지를 버튼으로 출력, 검색/이메일/지도 버튼 구현에 사용

5. internet.py
- 용도: Open API 연동과 연관된 함수
- getStr 함수: 문자열 내용이 있을 때 사용
- connectOpenAPIServer 함수: 서버를 연결하는 함수
- userURIBuilder 함수: 사용자가 입력한 내용에 맞는 uri를 생성하는 함수, '시' 포함 여부 판단 및 수정
- getHospitalDataFromXml 함수: 카테고리에 따라 다른 uri를 생성, Open API의 데이터를 읽어와 리턴
- getData 함수: 전체 카테고리에 따른 시설의 개수를 출력해야 하는 그래프에서 모든 Open API 데이터를 읽어오기 위한 함수, 가져온 데이터에서 시설의 개수를 센 후 해당 내용을 리턴

6. project.py
- 용도: Tkinter 환경 세팅 (메인 모듈)
- onEmailInput 함수: 이메일로 보낼 내용을 html 형식으로 덧붙인 후 전송하는 함수
- onEmailPopup 함수: 이메일 버튼을 클릭했을 때 메일을 받을 주소를 입력하는 창을 띄우는 함수
- sendMail 함수: 주소 입력 후 확인 버튼을 눌렀을 때 실행되는 함수, 메일을 전송할 아이디에 로그인
- Pressed 함수: 지도 버튼을 눌렀을 때 실행되는 함수, 클릭한 시설의 값을 받아온 후 해당 시설의 위치를 새 창에서 지도로 표현
- onSearch 함수: 검색 버튼을 눌렀을 때 실행되는 함수, 시설 검색 함수와 그래프 그리기 함수 호출 및 카테고리에 따른 이미지 변경 담당
- SearchHospital 함수: 리턴된 Open API 데이터를 읽어 리스트 박스에 입력하는 함수
- InitScreen 함수: Tkinter 화면에 출력될 내용을 설정해둔 함수

7. setup.py
- 용도: 배포 시 세팅

8. spammodule.c
- 용도: 항목 개수 세기, 문자열 출력
- spam_result 함수: 리스트 박스에 출력되는 문자열 중 result: 부분을 담당
- spam_num 함수: 출력된 시설의 개수를 센 후 리턴