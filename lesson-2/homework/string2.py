# Extract car names from this text: txt = 'LMaasleitbtui'
txt = 'LMaasleitbtui'

car1 = []
car2 = []
for i in txt:
    if i % 2 == 0:
        car1.append(i)
    else:
        car2.append(i)


print(''.join(car1))
print(''.join(car2))