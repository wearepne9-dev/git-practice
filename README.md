# git-practice

오픈소스 SW Lab 7을 위한 Git과 GitHub 실습 저장소입니다.

파일의 변경 사항을 스테이징하고, 커밋으로 기록한 뒤, GitHub 원격 저장소로
push하는 기본 흐름을 연습합니다.

실제 연구 자료를 Git으로 정리하는 예시로 SLAM 실험 설명과 결과표를 함께 제공합니다.

## 파일 구성

| 파일 | 역할 |
| --- | --- |
| `README.md` | 저장소 소개와 실행 방법 |
| `.gitignore` | 로컬 설정, 인증 정보, 생성 파일의 실수 업로드 방지 |
| `main.py` | Git 작업 흐름을 출력하는 간단한 Python 예제 |
| `commands.md` | 강의에서 다룬 Git 명령어 정리 |
| `learning-notes.md` | 파일 상태, 커밋, 원격 저장소의 핵심 개념 |
| [`docs/slam-benchmark.md`](docs/slam-benchmark.md) | 6종 SLAM 실험 설명, 평가 조건, 결과표와 해석 |
| [`data/slam-results.csv`](data/slam-results.csv) | 알고리즘별 APE·RPE 집계 수치 |

## SLAM 실험 자료

KISS-ICP, KISS-SLAM, FAST-LIO, LIO-SAM, R3LIVE, FAST-LIVO2의 기존 실험 기록을
정리했습니다. LiDAR, IMU, 카메라 구성에 따른 결과를 RTK Fixed 기준의
병진 APE RMSE와 10 m RPE RMSE로 비교합니다.

- [실험 설명과 결과표 읽기](docs/slam-benchmark.md)
- [CSV 결과 데이터 보기](data/slam-results.csv)

실험 조건과 해석의 한계, 자료 출처는 위 문서에 설명했습니다.
공개 자료에는 개인 식별 정보, 위치 좌표, 이동 궤적, 원본 로그를 포함하지 않습니다.
이 저장소의 Python 예제는 Git 작업 흐름을 출력하며, SLAM을 실행하는 프로그램은 아닙니다.

## 실행 방법

Python 3가 설치된 환경에서 실행합니다. 추가 패키지는 필요하지 않습니다.

```bash
python main.py
```

예상 출력:

```text
Hello, Git and GitHub!
1. Modify: Edit a file in the working directory.
2. Stage: Select changes with git add.
3. Commit: Record a snapshot with git commit.
4. Push: Upload local commits with git push.
```

## 커밋 구성

1. 저장소 소개 작성
2. `.gitignore` 추가
3. Python 예제 추가
4. Git 명령어 정리 추가
5. 핵심 개념과 실행 안내 추가
6. 개인정보와 위치 정보를 제외한 SLAM 실험 요약 및 결과표 추가

## 이력 확인

```bash
git status
git ls-files
git log --oneline --reverse
git rev-list --count HEAD
```

인증 정보와 개인 자료는 저장소에 포함하지 않습니다.
