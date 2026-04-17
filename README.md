#  Rust Server Search Discord Bot

현재 기본 기능을 중심으로 구현된 상태이며,
파이썬을 공부하며 진행하고 있습니다.

## 구현 내용 정리

Discord 봇을 통해 외부 API(BattleMetrics)를 활용하여  
Rust 서버 정보를 조회하는 기능을 구현했습니다.


## 주요 기능

### 1. 서버 검색 (`/검색어`)

사용자가 입력한 키워드를 기반으로 서버 목록을 조회합니다.

#### 동작 흐름

1. BattleMetrics API 호출
2. 전체 서버 데이터 조회
3. 서버 이름 기준 필터링
4. 최대 10개 결과 출력

#### 핵심 로직

```python
if keyword.lower() in name.lower():
    results.append(server)
```

####  추후 개선할 부분 및 작업 예정

- 검색 결과 페이징 처리
- 상세 조회 연결 방식 개선
- 공식 / 비공식, PvP / PvE 등 필터 기능 추가
- 정렬 기능 추가 (플레이어 수, 핑 등)
- 자동완성 기능 적용
- API 호출 최적화 및 캐싱 검토
- 코드 구조 분리 및 리팩토링
