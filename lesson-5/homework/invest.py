def invest(amount, rate, years):
    for i in range(1, years+1):
        print(f'year {i}: {round(amount * (1 + rate)**i, 2)}')


print(invest(100, .05, 4))
