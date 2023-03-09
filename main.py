count = 0;   # 하얀칸 위에 말의 개수를 세는 변수
white = 0;  # 0/1토글 첫번째 줄은 짝수번 문자가 흰색, 두번째 줄은 홀수번 문자가 흰
"""
.F.F...F
F...F.F.
...F.F.F
F.F...F.
.F...F..
F...F.F.
.F.F.F.F
..FF..F.
"""
# 8번 표준 입력에서 문자열을 입력
for _ in range(8):  # _:0,1,2,3,4,5,6,7
  line = input()
  # 입력받은 문자열에서 8번 흰색 칸에 말이 있는지 검사한다
  for i in range(8):
    if line[i] == 'F' and i%2==white:
      count+=1
  white = (white+1)%2

print(count)
    