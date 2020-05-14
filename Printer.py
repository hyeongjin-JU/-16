a = list(map(int,input("작업 수를 입력하세요 : ")))
b = list(map(int,input("작업 번호를 입력하세요 : ")))
priority = list(map(int,input("우선순위를 입력하세요 : ").split()))

number = list(range(len(priority)))
printtime = 0

while True:
    if priority[0] == max(priority):
        printtime += 1
        if number[0] == b:
            print(printtime)
            break
        else:
            number.pop(0)
            priority.pop(0)
    else:
        number.append(number.pop(0))
        priority.append(priority.pop(0))         