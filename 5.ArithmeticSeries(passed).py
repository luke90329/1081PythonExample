for i in range(eval(input())):
    a,b,c = map(int,input().split()) 
    print(int((a + a + b*(c-1))*c/2))