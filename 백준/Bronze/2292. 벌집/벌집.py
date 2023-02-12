n = int(input())

startNum = 1
cnt = 1

while n > startNum:
    startNum += 6 * cnt
    cnt += 1
    
print(cnt)