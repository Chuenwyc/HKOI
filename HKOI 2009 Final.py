def Q0(a):
    for i in range(a):
        for j in range(a-i):
            if a-i-j != 1:
                print(a-i-j,end=' ')
            else:
                print(1,end=' ')
                for k in range(i):
                    print(k+2,end=' ')
        print()         
Q0(4)


