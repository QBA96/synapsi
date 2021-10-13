def reverse(N):
  rem = 0
  while N > 0:
    rem = (10*rem) + N%10
    N = N // 10
  return rem

def reverse_str_method(N):
    if "-" in str(N):
        return 0
    else:
        return int(str(N)[::-1])

numbers = [123, 15, 52, 321 -512, 1024, -5, -4, 13]

for n in numbers:
    print(f"Number: {n} First method: {reverse(n)} Second method: {reverse_str_method(n)}")