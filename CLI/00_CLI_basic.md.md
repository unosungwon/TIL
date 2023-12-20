
## CLI vs GUI
- `CLI` -> 명령어 기반 인터페이스
- `GUI` -> 그래픽 기반 인터페이스

## 기초 명령어 

> https://hanamon.kr/linux-cli-%EA%B8%B0%EB%B3%B8-%EB%AA%85%EB%A0%B9%EC%96%B4/
>
> Linux CLI 기본명령어 참고  

### (1) pwd
- `pwd` (print working directory) : 현재 폴더의 경로 
- `~` (home directory) : 홈 디렉토리(git bash 처음 열면 나오는 기본 폴더)
- `.` : 현재 폴더
- `..` : 상위 폴더
- `/` : 천장 폴더 (root dir)


### (2) ls
- `ls` (list) : 내용물을 출력
- `ls -a` : 숨긴 폴더까지 다 보임

### (3) cd 파일명
- `cd` (change directory) : 폴더를 변경
- `cd . . `: 상위 폴더로 이동
- `cd .` : 현재 폴더로 이동
  
### (4) touch 파일명
- 파일 생성
- `.파일명` : 숨김 파일 생성 가능
  
### (5) rm 파일명
- 파일 삭제 
- rm a.txt

### (6) mkdir 폴더명
- mkdir (nake directory) : 폴더 생성
  
### (7) rm -r 폴더명
- `-r` (recursively) : 폴더 삭제
- `rm -rf` => f ; force (강제로)

### (8) cp 파일명 위치
- `cp` (copy) : 파일 복사

### (9) cp -r 폴더명 위치
- 폴더 복사

### (10) mv 파일/폴더명 바꿀파일/폴더명
- 파일/ 폴더명 변경
- `mv 파일/폴더명 위치` : 파일/폴더를 이동
- 파일 이동 및 이름바꾸기
    - `mv` 파일장소/파일이름 옮길장소
```cli
mv file1 file2    -> 파일명 변경
mv file1 folder   -> file1 을 folder 디렉토리로 이동
mv /a/b/c/aa.txt /a/d   -> a/b/c 디렉토리의 aa.txt 파일을 /a/d 디렉토리로 이동
```
