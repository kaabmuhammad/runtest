def Fib(n):
    if n == str:
        raise TypeError(f'Please enter a number not a string')
    if n == 0: return 0
    elif n == 1: return 1
    else: return Fib(n-1)+Fib(n-2)

print(Fib(11))