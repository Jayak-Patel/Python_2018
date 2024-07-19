#import magic
def fib(x):
    if x==1:
        return 1
    if x<=0:
        return 0
    else:
        return fib(x-1)+fib(x-2)




for x in range(100):
    print(fib(x))

#print(fib(int(input("Type a number"))))
