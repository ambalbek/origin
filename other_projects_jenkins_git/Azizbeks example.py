from functools import reduce
a=21346879654987863456879645168764687964 # find the result of the sum
res=(sum(list(map(lambda x: int(x), str(a))))) #sum each number
final=(sum(list(map(lambda x: int(x), str(res))))) # sum each number in res
final2=reduce(lambda x,y: int(x)+int(y), list(map(lambda x: int(x), str(final))))
print(final2, res, final) 
  
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1]) # fibbonnacci sequence
print(fib(9)) 