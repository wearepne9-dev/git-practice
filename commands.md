# Git 명령어 정리

## 저장소 생성과 상태 확인

```bash
git init
git status
git diff
```

- `git init`: 현재 폴더에 로컬 Git 저장소를 만듭니다.
- `git status`: 추적 여부와 스테이징 상태를 확인합니다.
- `git diff`: 작업 폴더와 스테이징 영역 사이의 변경 사항을 확인합니다.

## 변경 사항 기록

```bash
git add README.md
git diff --staged
git commit -m "docs: update README"
git log --oneline
```

`add`는 다음 커밋에 포함할 내용을 선택하고, `commit`은 선택한 내용의
스냅샷을 로컬 저장소에 기록합니다. 커밋 메시지에는 변경 목적을 적습니다.

## 이름 변경, 추적 중단, 복구

아래 명령은 동작 설명을 위한 예시입니다. 해당 파일이 있는지 확인한 후 사용합니다.

| 명령어 | 동작 |
| --- | --- |
| `git mv old.txt new.txt` | 파일 이름을 바꾸고 변경을 스테이징합니다. |
| `git rm example.txt` | 파일을 디스크에서 삭제하고 삭제를 스테이징합니다. |
| `git rm --cached example.txt` | 로컬 파일은 남겨 두고 Git의 추적 대상에서 제거합니다. |
| `git restore --staged README.md` | 스테이징만 취소하고 작업 폴더의 수정은 유지합니다. |
| `git restore README.md` | 기본적으로 스테이징 영역의 내용으로 작업 파일을 복원합니다. 커밋하지 않은 수정이 사라질 수 있습니다. |

이미 추적 중인 파일은 `.gitignore`에 추가하는 것만으로 추적이 중단되지 않습니다.
또한 추적을 중단해도 이전 커밋에 기록된 파일 내용은 남아 있습니다.

## GitHub 원격 저장소 연결과 업로드

GitHub에서 비어 있는 `git-practice` 공개 저장소를 만든 뒤 실행하는 예시입니다.
`YOUR_USERNAME`을 자신의 GitHub 사용자 이름으로 바꿉니다.

```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/git-practice.git
git remote -v
git push -u origin main
```

`origin`은 원격 저장소의 별칭이고, `main`은 업로드할 브랜치입니다.
`-u`는 이후 `git push`에서 사용할 기본 추적 관계를 설정합니다.
비밀번호나 토큰을 파일, 커밋 메시지, 원격 저장소 URL에 넣지 않습니다.
