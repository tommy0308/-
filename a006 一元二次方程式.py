# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 18:19:14 2021

@author: Tommy
"""

while True:
    a=input("欲求一元二次方程式 ax^2+bx+c=0 的根，請輸入三個整係數 a,b,c 並以空白隔開。\n")
    coefficients=a.split()
    coefficients=list(map(int, coefficients))
    [a, b, c]=coefficients
    if(a==b==c==0):
        print("此方程式為0方程式")
    elif(a==b==0):
        print("此方程式無解。請重新輸入")
    else:
        if(a==0):
            r=-c/b
            if(r==int(r)):
                r=int(r)
                if(b==1):
                    if(c<0):
                        print("此方程式為一元一次方程式 x",c,"=0，且其根為",r)
                    else:
                        print("此方程式為一元一次方程式 x+",c,"=0，且其根為",r)
                else:                    
                    if(c<0):
                        print("此方程式為一元一次方程式 ",b,"x",c,"=0，且其根為",r)
                    else:
                        print("此方程式為一元一次方程式 ",b,"x+",c,"=0，且其根為",r)
            else:
                print("此方程式無整數解。請重新輸入")
        else:
            d=b**2-4*a*c
            if(d<0):
                print("此方程式無實數解。請重新輸入")
            elif(d**0.5!=int(d**0.5)):
                print("此方程式無有理數解。請重新輸入")
            else:
                r=[(-b+d**0.5)/(2*a),(-b-d**0.5)/(2*a)]
                if(r[0]!=int(r[0]) and r[1]!=(r[1])):
                    print("此方程式無整數解。請重新輸入")
                else:
                    if(r[0]==int(r[0])):
                        r[0]=int(r[0])
                        if(r[1]!=int(r[1])):
                            print("此函數只有一個整數解",r[0])
                        elif(r[0]!=r[1]):
                            r[1]=int(r[1])
                            print("此函數的兩根為",r[0],",",r[1])
                        else:
                            print("此函數有重根",r[0])
                    else:
                        r[1]=int(r[1])
                        print("此函數只有一個整數解",r[1])
    b=input("還有一元二次方程式要解嗎? ")
    YES=["是", "有", "YES", "Yes", "Y"]
    if b in YES:
        continue
    else:
        break
print("謝謝")