def fact(n):
    if n == 1:      # basic
        return 1
    else:           # inductive
        return n * fact(n-1)

print(fact(4))
