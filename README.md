# 33-1st-crowsSeven-backend
김민정, 박상연

# 33기 1차 프로젝트 크로우즈세븐

<br/>

## 🌼 프로젝트 소개 🌼


* 그릇과 같은 식기를 판매하는 사이트입니다. 
* 짧은 기간동안 개발에 집중할 수 있도록 디자인과 기획 일부를 [그로우캐년](https://crowcanyon.co.kr)를 참조하여 학습목적으로 만들었습니다.
* 실무 수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
* 이 프로젝트에서 사용하고 있는 로고와 배너는 해당 프로젝트 팀원 소유이므로 해당 프로젝트 외부인이 사용할 수 없습니다.

<br/>

## 🌼 시연영상 🌼
https://youtu.be/--gfsEindSE
<br/>

## 🌼 프로젝트 관련 DB 🌼
<img width="756" alt="image" src="https://user-images.githubusercontent.com/96784345/172043745-f33c57ea-9c47-42bb-9bbf-04518fb2629b.png">

<br/>

## 🌼 개발 인원 및 기간 🌼
**개발기간** : 2022/05/24~2022/06/03

<br/>

**개발인원 및 파트** : 
#### Frontend
김완영, 박슬기, 유하은, 신윤지, 염종은

#### Backend
김민정, 박상연

<br/>

## 🌼 기술 🌼
**Back-End** : Python, Django web framework, Bcrypt, MySQL, pyjwt
<br/>
**Common** : Git-Hub, slack, trello, AWS

<br/>

## 🌼 페이지별 구현 사항 중 본인 구현 기능 🌼

### Users APP
-유저별 구매한 기록 
READ :
  GET메소드를 활용,

### Products APP
제품 상세페이지
READ :
  GET메소드를 활용, pathparameter활용,
  DB 구조상 한 제품 내 옵션 유무에 따라, 옵션 종류에 따라 다른 데이터를 받을 수 있게 구현

### Orders APP
CREATE :
  주문 작성: POST메소드 활용, 전체주문과 선택주문 모두 가능하게 구현, 예외처리, 트랜잭션활용 관련 장바구니까지 삭제할 수 있도록 구현

### Reviews APP
CREATE :
    리뷰 작성: POST메소드 활용, 사용자별 이미 리뷰가 완료된 제품에 대한 예외처리
    댓글 작성 : POST메소드 활용
READ :
    전체리뷰페이지 -GET 메소드 활용, 
    상세리뷰페이지 - GET 메소드 활용, 상세리뷰페이지에 해당되는 댓글, 관련 리뷰까지 보일 수 있게 구현, 조회 수 관련 기능 추가
    리뷰검색     - GET 메소드 활용, 패킹언패킹 개념활용하고 2가지 기준으로 필터를 적용해 리뷰 검색
UPDATE : PATCH메소드 활용, pathparameter에서 주는 review_id와 token을 이용한 user_id를 이용해 DB조회후 json데이터로 보내준 리뷰내용으로 수정, 예외처리
DELETE : DELETE메소드 활용, token에서 받은 user_id, pathparameter로 받은 review_id를 이용해 DB조회하여 delete메소드 활용해서 삭제 예외처리


### Carts APP
READ : GET메소드 활용, userid로 조회, user_id는 token을 이용하여 획득, 카트에 담긴 물건이 24시간이 지난 이후에는 자동삭제될 수 있도록 구현
CREATE : POST메소드 활용, body에서 json형식으로 제품id와 수량을 받고 token을 이용해 id값을 추가해 DB에 저장, get_or_create 메소드를 활용 존재하지않을땐 생성하고, 이미 존재할땐 수량만 업데이트
UPDATE : PATCH메소드 활용, pathparameter에서 주는 cart_id와 token을 이용한 user_id를 이용해 DB조회후 json데이터로 보내준 제품수량 수정, 재고 관련 예외처리
DELETE : DELETE메소드 활용, token에서 받은 user_id, pathparameter로 받은 cart_id를 이용해 DB조회하여 delete메소드 활용해서 삭제, 예외처리

## 🌼 AWS EC2, RDS 활용 배포🌼


<br/>

## 🌼 프로젝트 진행 과정 🌼
||Trello|
|------|---|
|협업 방식|매일 아침 30분동안 진행사항과 오늘 할 작업 내용 공유|
|IMG|![image](<img width="1440" alt="image" src="https://user-images.githubusercontent.com/96784345/172043293-53c651d4-0a74-495c-979f-1a68ac747220.png">|
