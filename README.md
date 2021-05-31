# 🔍 notion-scrum-analytics

- `notion-scrum-analytics`는 Notion의 스크럼 보드 기능을 확장해주는 Python 애플리케이션입니다.

## 미리보기

![번다운 차트](burnchart.png)

_Notion의 스크럼 보드에 기록된 태스크 카드들의 진행 현황을 자동으로 기록하고, 이를 기반으로 조직의 스프린트 별 태스크 진행 현황을 보기 쉽게 확인할 수 있습니다._

## 지원되는 기능

`notion-scrum-analytics` 에서 현재 지원하는 기능은 다음과 같습니다.

### 일간 자동화

- [x] 매일 자정에 DOING 상태의 카드를 TODO로 이동시킵니다.
- [x] 매일 자정에 DOING 상태와 DONE 상태의 카드의 진행 기간을 기록합니다.

### 주간 자동화

- [x] 매주 월요일 자정에 BACKLOG 상태의 카드를 자동으로 TODO로 이동시킵니다.
- [x] 매주 일요일 자정에 DONE 상태의 카드를 자동으로 ARCHIVE로 이동시킵니다.
- [x] 스프린트 기간동안 태스크 진행 현황을 [번 다운 차트](https://ko.wikipedia.org/wiki/%EB%B2%88_%EB%8B%A4%EC%9A%B4_%EC%B0%A8%ED%8A%B8)로 나타낸 후, 팀의 슬랙으로 전송할 수 있습니다.
