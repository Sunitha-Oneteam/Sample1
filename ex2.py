def square_generator(n):
    for i in range(n):
        yield i ** 2
gen = square_generator(5)
print(next(gen))
print(next(gen))
print(next(gen))
print("stop")
for value in gen:
    print(value)
