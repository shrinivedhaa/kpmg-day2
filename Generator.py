def gen_numbers(n):
    for i in range(n):
        yield i

k=gen_numbers(5)
for num in k:
    print(num)