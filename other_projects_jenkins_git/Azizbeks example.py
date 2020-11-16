a=21346879654987863456879645168764687964 # find the result of the sum
res=(sum(list(map(lambda x: int(x), str(a))))) #sum each number
final=(sum(list(map(lambda x: int(x), str(res))))) # sum each number in res
print(final) 