def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return number < 0
    pass 

# Check your answer
print(is_negative(-123))
print(concise_is_negative(213))