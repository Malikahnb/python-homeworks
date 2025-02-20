def convert_cel_to_far(cel):
    return cel * 9/5 + 32


def convert_far_to_cel(far):
    return (far - 32) * 5/9


far = int(input("Enter the temperature in Fahrenheit: "))
print(f'{far} degrees F = {round(convert_far_to_cel(far), 2)} degrees C')

cel = int(input("Enter the temperature in Celsius: "))
print(f'{cel} degrees C = {round(convert_cel_to_far(cel), 2)} degrees F')
