def print_numbers(n):
    if n==0:
        return
    else:
        print_numbers(n-1)
        print(n)
n=6
print_numbers(n)