from sys import stdin

s_in = list(stdin.readline().strip())

sum = 0
for a in s_in:
    sum += (ord(a.upper()) - 64)
# print(sum)
is_prime = True
for i in range(2, sum):
    if sum % i == 0:
        is_prime = False

print('It is a prime word.') if is_prime else print('It is not a prime word.')
