# Automated Tool
- 자동 문서작성 툴
# Journal
- 04 27 
    - 코드 리펙토링 필요, 반복되는 문장이 너무 많음
    - 우선 빠른 구현 먼저
- 04 29
    - 정확하게 모든 문서에서 작동하는지 확인필요
        - 음.. 테스트코드를 만들어야하는지 고민이다.
        - 테스트하는것보다 만드는것이 오래걸리는데..
    - bl 파싱 시작해야함
- 05 01
    - 파싱 위해 pdfreader 모듈 가져옴
        - 출처 코드: https://stackoverflow.com/questions/26494211/extracting-text-from-a-pdf-file-using-pdfminer-in-python
    - pdf 파일의 값을 어떻게 가져오냐가 문제
- 05 04
    - pdf 파일읽어와서 parsing 완료
    - re를 이용하여 찾아오는건 한줄인데, 실제로 정답은 한줄이 아닐 수 있다. 다양한 경우를 봐야한다.

