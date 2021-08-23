#what I have learned today
 - git add -> git status -> git commit -> git push origin master
 - 의 순서대로작업할 때 오류가 뜸.

 - 이유:
     1. 원격 저장소에 내가 작업한 코드가 업데이트 된 상태
     2. 데이터 유실 등에 문제될 수 있다
 - 해결 방법:

     1. 강제로 push
     - git commit -m
     - git push origin +master

     2. pull을 먼저 하고 push 하기
     - git pull <remote 저장소 이름><branch 이름>
     - git add 또는 git add <update할 파일>
     - git commit -m "commit message"
     - git push <remote 저장소 이름><branch 이름>

