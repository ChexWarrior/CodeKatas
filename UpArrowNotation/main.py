
def multiply(value, amount):
    if amount > 1:
        return multiply(value + value, amount - 1)
    
    return value

sample = multiply(2, 4)
print(sample)