# Git 명령어
## code . 
- "내가 코드 에디터야. 해당 폴더를 vscode로 열어줘."

## git init
- 해당 폴더를 git으로 관리 시작하겠다.
- (master)
- .git/

```bash
amyks@SUNGWON MINGW64 ~/test
$ git init
Initialized empty Git repository in C:/Users/amyks/test/.git
```

## git status
- working tree & staging area의 상태를 보여줌. 

- 현재 작업 디렉토리의 상태를 보여줌
  - 어떤 파일이 추적, 수정, staging area에 있는지를 알 수 있음.

```bash
~/test (master)
$ git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
 # -> commit 할것도 없음 (파일을 만들거나 복사하고 git add 를 사용해서 추적해봐)
```


## a.txt 파일 생성 직후
```bash
 ~/test (master)
$ git status
On branch master

No commits yet

Untracked files:   # ->추적되지 않은 파일들이 있음
  (use "git add <file>..." to include in what will be committed)
        a.txt
  # -> git add 파일명을 써서 commit 될것에 포함시켜봐
nothing added to commit but untracked files present (use "git add" to track)
# -> commit 될것이  아직 add 되지 않았지만, 추적되지 않은 파일들이 있음
```

## git add a.txt 직후
- file을 중간 단계인 staging area 에 등록
- `git add .` => 현재 디렉토리에 있는 모든 파일을 add 한다. 
  
  - 꼭 파일명 하나하나를 지정할 필요 없음. 
  
  
```bash
 ~/test (master)
$ git status
On branch master

No commits yet

Changes to be committed:  # -> commit 될수 있는 변화가 있음
  (use "git rm --cached <file>..." to unstage)
        new file:   a.txt
 # -> git rm --cached file 을 써봐 (unstage 하려면)
```

```bash
 ~/test (master)
$ git status
On branch master
Untracked files:
# '추적되지 않은'
# git 에 한번도 commit 되지 않은 상태. 
  (use "git add <file>..." to include in what will be committed)
        b.txt

nothing added to commit but untracked files present (use "git add" to track)

 ~/test (master)
$ git add b.txt

 ~/test (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   b.txt

```

## git commit -m "메세지"
- staging area 에 있는 파일을 commit log 에 커밋(버전) 시켰다! 
  
  == `create version`

- `git commit -am "message"` 
  - add, commit 까지 한번에 가능.
  - 하지만, `untracked` 인 경우엔 `사용 못함`.


```bash
[실패의 경우]
Author identity unknown  # -> 작성자 신원 미상

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com" 
  git config --global user.name "Your Name"

to set your account's default identity.  # -> 너의 계정 기본 신원을 설정
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'amyks@SUNGWON.(none)')

```

```bash
[성공된 경우]
 ~/test (master)
$ git commit -m "First commit"
[master (root-commit) 5bd3c7d] First commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a.txt
```

```bash
 ~/test (master)
$ git commit -m "Add b.txt"
[master aa25c1a] Add b.txt
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 b.txt
```


## 파일 수정 후 git status
```bash
 ~/test (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   a.txt
# commit 되어있고, 수정된 기존 파일은 '수정되었지만 commit 되지 않았다' 라고 뜨고,

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        z.txt
# commit 되지 않은 새 파일은 '추적되지 않은' 이라고 뜸 == 협업 불가능한 상태

no changes added to commit (use "git add" and/or "git commit -a")

```

## git config
- git config --global user.email : (전역) 사용자의 이메일 설정을 출력하는 명령어
- 나중에 변경 가능.

## git log / git log --oneline
- git commit의 목록을 출력
- `git log --oneline` => 목록을 한줄로 출력
- commit log를 보여준다. 
  - 저장소의 commit 히스토리를 보여주고, 
  - 각 커밋에 대한 정보(커밋해시, 작성자, 날짜, 커밋메세지) 제공. 
  
- 저장소의 변경 이력, 각 커밋 간의 관계 파악 가능

```bash
 ~/test (master)
$ git log
commit 5bd3c7d6656b5fc2d261a23744d07ffa0c2ea638 (HEAD -> master)
Author: SUNGWON <amyksw@naver.com>
Date:   Tue Dec 19 16:38:03 2023 +0900

    First commit
```

```bash
 ~/test (master)
$ git log
commit aa25c1a13d4c173b1f32cc22c99bcf243be66d8b (HEAD -> master)
Author: SUNGWON <amyksw@naver.com>
Date:   Tue Dec 19 16:47:10 2023 +0900

    Add b.txt

commit 5bd3c7d6656b5fc2d261a23744d07ffa0c2ea638
Author: SUNGWON <amyksw@naver.com>
Date:   Tue Dec 19 16:38:03 2023 +0900

    First commit
```

## git log --stat
- `commit 된 파일들`의 `내용` 보여줌.

## q
- git log 가 길어졌을때 빠져나오는 단축키

## git diff
- `working tree` 에 있는 modified 된 파일 내용의 `차이점`을 보여줌. 
- 마지막 버전 이후에 작업한 내용 파악에 용이

  = `마지막 버전과 working tree 사이의 차이점 검토 가능.`

## git reset --hard
- 마지막 버전 이후의 작업한 내용이 마음에 안들때 사용.
- working tree에 있는  modified 된 파일의 `수정사항을 없애버림.` 
- git status 하면, `'nothing to commit, working tree clean' `나옴.

## git reset --hard commit주소
- 해당 commit 은 삭제되고 그 다음 commit이 master 됨

## git checkout commit주소
- 원하는 commit 시점으로 바꿀수 있음. 
- head 위치가 변경

## git checkout master
- 다시 최신 commit 시점으로 돌아감.

## head ?
- head = 포인터라고 생각

```bash
 ~/practice (master)
$ git log --oneline
0f15c8c (HEAD -> master) 이름 추가
8b277b6 First commit
```

```bash
HEAD is now at 8b277b6 First commit
```

## git remote
- 저장소 이름이 나옴

```bash
 ~/unosungwon (main)
$ git remote
origin
```

## git remote add [저장소이름][저장소주소]
- 만약 저장소이름이 안정해져 있다면,
- git remote add origin(내가 정하면 됨) https://github.com/unosungwon/practice.git(깃헙 repository 주소)

- 대부분 저장소이름을 origin 이라고 함

## git remote -v
- `원격저장소 정보` 알려줌

```bash
 ~/practice (master)
$ git remote -v
origin  https://github.com/unosungwon/practice.git (fetch)
origin  https://github.com/unosungwon/practice.git (push)
```

## git push [저장소이름] [branch 이름]

- local에 있는 폴더를 저장소에 `백업`

```bash
 ~/practice (master)
$ git push origin master
```

## git clone [저장소주소]

- 처음으로 저장소에서 local로 갖고 올때
- 홈에서 해야함 !!

```bash
 ~
$ git clone https://github.com/unosungwon/unosungwon.git
```
## git pull [저장소이름] [branch 이름]
- git pull origin master
- git 폴더에서 해야함.

## 
```bash
$ git log
commit 12d0cb7058f1168f4848deaf04e0c8361c5041a9 (HEAD -> master)
Author: SUNGWON <amyksw@naver.com>
Date:   Wed Dec 20 17:20:29 2023 +0900

    터미널 쿵쿵따

commit 5478ee574a84b34217c10b855f00328f19ad6101 (origin/master, origin/HEAD)
Author: Ik Tae Kwon <kwoniktae@gmail.com>
Date:   Wed Dec 20 16:52:30 2023 +0900

    Initial commit
```