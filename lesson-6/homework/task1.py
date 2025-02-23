def check(func):
    def wrapper(a, b):
        if b == 0 :
            return "Denominator cannot be 0"
        return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b

print(div(2, 6))
print(div(6, 0))

