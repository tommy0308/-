# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
while True:
    a=input("請輸入數列的前四項並以空格分開,0≦首項≦20\n")
    numbers=a.split()
    numbers=list(map(int, numbers))
    d1=numbers[1]-numbers[0]
    d2=numbers[2]-numbers[1]
    d3=numbers[3]-numbers[2]
    if (numbers[0]<0):
        print("首項小於0。請重新輸入")
        continue
    elif(numbers[0]>20):
        print("首項大於20。請重新輸入")
        continue
    elif(d1 == d2 == d3):
        a5=numbers[3]+d1
        b=numbers.append(a5)
        print(numbers)
    else:
        if(numbers[0]==0):
            print("此數列不是等差或等比數列。請重新輸入")
            continue
        else:
            r1=numbers[1]/numbers[0]
            r2=numbers[2]/numbers[1]
            r3=numbers[3]/numbers[2]
            try:
                r1 == int(r1)
                r2 == int(r2)
                r3 == int(r3)
                if(r1 == r2 == r3):
                    a5=numbers[3]*r1
                    a5=int(a5)
                    b=numbers.append(a5)
                    print(numbers)
                else:
                    print("此數列不是等差或等比數列。請重新輸入")
                    continue
            except:
                print("此數列不是等差或公比為整數的等比數列。請重新輸入")
                continue
    line=input("是否還有作業?\n")
    NO=["不", "NO", "沒了", "否", "no", "No"]
    if line in NO:
        break
print("掰")