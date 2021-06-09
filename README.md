# Automated Tool
## 1. About
-  텍스트 문서에 써있는것을 템플릿에 맞춰 엑셀문서로 바꿔주는 자동화 툴입니다.
-  본 프로젝트는 반복적인 업무의 간편화를 위해 만들어졌습니다.
-  특정 조건에만 동작하므로 범용적 사용은 불가능합니다.

- It is an automated tool that converts what is written in a text document into an Excel document according to the template.
- This repository was created to simplify repetitive tasks.
- It is not possible to use general purpose that operates only under specific conditions.
# 2. How To Use?
```bash
git clone https://github.com/kimSooHyun950921/automatedTool.git
python3 parsing_credint.py -f example.txt
```
## ChangeLog
- 04/27 update parsing branch: parsing text file
- 04/29 update creding parsing branch: need validation
- 05/01 update parsing branch: add pdf reader module
- 05/04 update parsing branch: parsing pdf file
- 05/04 merge parsing branch, left branch
- 05/04 update excel branch: make two files
- 05/10 update parsing branch: test and validation code
- 05/20 merge parsing branch
- 05/21 add write invoice packing list
- 05/27 add gui
- 06/09 release v0.1


## parsing branch ChangeLog
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
- 05 10
    - 검증 중
    - 생각보다 너무 많은 예외상황이 있어 이경우 처리해주는 것이 필요해보인다.
- 06 09
    - 릴리즈 버전 0.1 실행
    - 바뀌어진 폴더에대하여 수정 필요
    - 요구사항에 따라 코드 변경필요
        - Date Picker
        - Error 처리
        - 기본 단어처리
        - 클릭 -> 찾아보기 변경
        - hypen 갯수줄이기