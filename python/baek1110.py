Num = int(input())
count = 0
Old = Num
while True:
    result = (Old // 10) + (Old % 10)
    New = (Old % 10)*10 + (result % 10)
    count = count + 1
    if Num == New:
        print(count)
        break
    else:
        Old = New
        continue