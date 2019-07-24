"""Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. For example, if the limit is 3, it should print:
0 EVEN
1 ODD
2 EVEN
3 ODD """


def showNumbers(r1, r2):
    a = list(range(r1, r2+1))
    for i in a:
        if(i%2==0):
            print(str(i) + 'Even')
        else:
            print(str(i) + 'Odd')

r1=0
r2=int(input("Enter range for list : "))
ls=showNumbers(r1,r2)