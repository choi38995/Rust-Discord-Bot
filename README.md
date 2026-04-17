# Rust-Discord-Bot

한국 유저를 위한 Rust 서버 조회 봇


##  프로젝트 소개

Discord에서 Rust 서버를 검색할 수 있는 봇입니다.
간단하게 서버 이름을 검색하면 해당 서버 정보를 확인할 수 있도록 만들었습니다.

외부 API(BattleMetrics)를 활용해서 서버 데이터를 가져오고,
검색 결과를 Discord 채팅으로 보여주는 방식으로 구현했습니다.



##  주요 기능

###  서버 검색

* `/server` 명령어로 서버 검색
* 입력한 검색어를 기준으로 서버 목록 조회
* BattleMetrics API를 통해 데이터 가져오기



##  진행 중 기능

* 자동완성 기능 추가 예정
* 현재는 기본 검색 기능 위주로 구현된 상태



##  프로젝트 구조

```text
bot/
├─ main.py
├─ util/
│  └─ server_command.py
├─ service/
│  └─ rust_server_service.py
└─ ui/
   └─ server_view.py
```



##  동작 흐름

```text
/server 입력 → 검색어 입력 → 서버 조회 → 결과 출력
```



##  구현 내용

### 외부 API 연동

* BattleMetrics API를 사용해서 서버 정보 조회

### 데이터 처리

* API 응답에서 필요한 정보만 추려서 사용

### 구조 분리

* 명령어 처리 / API 호출 / 출력 부분을 나눠서 구현


##  사용 기술

* Python
* discord.py
* requests


##  느낀 점

* Discord 봇을 처음 만들어보면서 인터랙션 구조를 이해할 수 있었음
* 외부 API를 가져와서 사용하는 흐름을 경험함
* 기능을 추가할수록 구조를 나누는 게 중요하다는 걸 느낌


##  개선 예정

* 자동완성 기능 추가
* 서버 상세 조회 기능
* 출력 UI 개선
* 페이징 추가

## 테스트 현황
<img width="883" height="517" alt="image" src="https://github.com/user-attachments/assets/c02d3a9c-b5e7-4e56-894c-1517353596ba" />

