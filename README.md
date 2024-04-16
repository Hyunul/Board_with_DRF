# drf_prac
개인적으로 Django와 DRF를 학습하기 위해서 제작한 게시판 프로젝트입니다.

## 👨‍🏫 프로젝트 소개
구현된 기능은 다음과 같습니다.

- ModelViewSet 기반의 API Spec(HTTP Method, Status Code)을 만족하는 Rest API 개발
- 쿠키 기반으로 개발된 조회 수 카운트 기능을 Redis 기반으로 변경하여 성능 향상 도모
  - 응답 시간이 22ms에서 4ms으로 줄어들어 약 82%의 성능이 개선
- 33만 건의 게시글 테스트 데이터를 기반으로 API 성능 테스트
  - 100개 단위로 LimitOffsetPagination을 진행하여 서버의 과부하 예방
  - 조회 성능 개선을 위한 DB 인덱스 생성
- TestCase 라이브러리를 이용한 단위테스트 구성
---
위의 기능을 토대로 다음과 같은 API 테스트가 가능합니다.

- GET<br>
post/  :  게시글 확인 (100개 단위 페이징)
post/:id/  :  게시글 자세히 확인

- POST<br>
user/register  :  회원가입<br>
user/login/  :  인증을 통해 JWT 발급<br>
user/logout/  :  JWT 삭제<br>
post/  :  글 생성<br>

- PUT<br>
post/  :  글 수정

- DELETE<br>
post/  :  글 삭제

## 🕐 개발 기간
- 2024.02.25 ~ 2024.03.22
