
## ✅ 위코드 2차 팀 프로젝트 Refactoring (개인)
<img src="https://media.vlpt.us/images/ifyouseeksoomi/post/4b22b35f-9aed-443c-9b0c-6dceeb45a3e4/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-08-19%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%209.44.50.png">

위코드에서 2차 프로젝트로 진행했던 이탈리안 코스메틱 브랜드 getsuperfluid(https://getsuperfluid.com/) 홈페이지 클론 프로젝트를 개인적으로 다시 리팩토링하였습니다. 
<br>
(위코드에서의 클론 프로젝트는 기획과 디자인적 요소만 차용하고 코드는 수료생 본인이 직접 작성합니다.)<br><br>
Frontend: 김신영, 박예진, 최운정 <br>
Backend: 안솔, 황수미 <br>
- 실제 프로젝트 시 작성했던 앱: User 앱 API 전체, Product 앱 중 ProductList API
- 리팩토링 시 작성한 앱: User 앱 API 전체, Product 앱 API 전체, Order 앱 API 전체


## Detail
- User: 함수형 Decorator을 사용한 유저 검증
- Product: 상품 리스트 뷰에서 Filtering 시, QueryString과 Q객체를 이용한 쿼리 개선
- select_related와 prefetch_related를 이용한 캐싱을 통한 DB 접근 횟수 최소화
- refactoring 시 작성한 TIL post: https://velog.io/@ifyouseeksoomi/series/wecode-mecode-TIL-ProjectRebuild

## Built With
- Python
- Django (pure)

## API Document
https://documenter.getpostman.com/view/11973877/TVK8Zf1i#2ce01edb-f198-4b4d-a1b1-f1332d48fc46


