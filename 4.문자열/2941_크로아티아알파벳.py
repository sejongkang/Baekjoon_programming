from sys import stdin

croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0
s_in = stdin.readline().strip()
for s in croa:
    count += s_in.count(s)
    s_in = s_in.replace(s, ' ')
print(len(s_in.replace(' ', '')) + count)
