def fib(n):
    result = []
    a,b = 0,1
    while b<n:
        result.append(b)
        a,b = b, a+b
    return ("your fibannachi number",result)
while True:
    try:
        f = fib(int(input()))
    except:
        print("please enter the number not letter!")
    else:
        break
print(f)