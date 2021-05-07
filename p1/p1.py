import functools

numbers =[x for x in range(1,1000)]
val = functools.reduce(lambda a,x:a+x ,filter(lambda x: x%3==0 or x%5==0, numbers),0)
print("Result: " + str(val))

