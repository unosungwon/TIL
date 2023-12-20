# Git 선수 학습
> CLI 명령어

# Git
- `commit == 버전 == 스냅샷`

- 코드 관리 도구 (source code management tool)
  - git hub desktop 프로그램
  - Tortoise Git 프로그램 (윈도우에서만 사용 가능)
  - sourcetree 프로그램
  - git bash 프로그램 (GUI 없이 처리 가능)

- repository ?
  - 버전이 저장되어 있는 곳

- 소프트웨어 개발에서 버전 관리를 위해 사용되는 도구.
  - `버전관리` ? => 프로그램이나 소스코드를 만들 때, 여러번의 수정과 변경이 일어나는데, 이를 관리하고 추적하는 과정

![git 사진](https://static.packt-cdn.com/products/9781782168454/graphics/8454OS_01_4.jpg)


## Git ?
- Git 의 목적
  - version 관리 
  - backup 
  - collaborate (협업)

- 컴퓨터 프로그래밍 == 컴퓨터에게 무언가를 시키는 것
  

## SCM & VCS (버전잉을 하는 방식)
- SCM (source code management tool) : 코드 관리 도구
- VCS (Version control system) : 버전 관리 시스템


## Git 의 프로젝트 관리 단위
> Git의 코드 관리 단위 = 폴더

## 하위 폴더에서 add, commit, push 해도 가능
- 만약 test1 폴더 안에 test2, test3 폴더가 있고, 각각 a.txt, b.txt 가 존재.
- a.txt, b.txt 둘 다 내용 수정 후 저장.

1. 
```bash
 ~/test1
$ git init
Initialized empty Git repository in C:/Users/amyks/test1/.git/

 ~/test1 (master)
$ git remote add origin https://github.com/unosungwon/test.git

 ~/test1 (master)
$ git add .

 ~/test1 (master)
$ git commit -m "test 전체 폴더 업로드 실험"
[master (root-commit) b7cc006] test 전체 폴더 업로드 실험
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 test2/a.txt
 create mode 100644 test3/b.txt

 ~/test1 (master)
$ git push origin master
```

2. `상위 폴더`인 test1 에서 `수정된 파일 add 진행`

```bash
 ~/test1 (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   test2/a.txt

no changes added to commit (use "git add" and/or "git commit -a")

 ~/test1 (master)
$ git add test2/a.txt
```

3. `하위 폴더`인 (이미 github에 등록된 폴더) test3 폴더에서 `수정된 파일 add commit 진행`

```bash
 ~/test1/test3 (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   ../test2/a.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   b.txt


 ~/test1/test3 (master)
$ git add b.txt

 ~/test1/test3 (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   ../test2/a.txt
        modified:   b.txt


 ~/test1/test3 (master)
$ git commit -m "만약 하위 폴더에서 다른 폴더에 있는 수정사항도 한꺼번에 커밋이 가능한가?"
[master b8d54ea] 만약 하위 폴더에서 다른 폴더에 있는 수정사항도 한꺼번에 커밋이 가능한가?
 2 files changed, 8 insertions(+)
```

## 원격 저장소에서 파일 삭제하기

- git rm --cached [filename]
- 그리고 commit 후 push 까지 해야 원격저장소에서 삭제.

```bash
 ~/test1 (master)
$ git rm --cached -r mustremove/
rm 'mustremove/sdbs.txt'

 ~/test1 (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    mustremove/sdbs.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        mustremove/

 ~/test1 (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    mustremove/sdbs.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        mustremove/

 ~/test1 (master)
$ git commit -m "원격에서는 없어지는지"
[master 2cbe96a] 원격에서는 없어지는지
 1 file changed, 0 insertions(+), 0 deletions(-)
 delete mode 100644 mustremove/sdbs.txt

 ~/test1 (master)
$ git push origin master


```