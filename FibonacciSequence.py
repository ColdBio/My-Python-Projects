# Calculating Fibonacci Sequence
a = 0
b = 1
fib = [0, 1]
for x in range(15):
    fib.append(fib[a] + fib[b])
    a+=1
    b+=1

print(fib)
    
