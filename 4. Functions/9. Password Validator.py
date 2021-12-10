
def check_password_long(password):
    if not 6 <= len(password)  <= 10:
        return False
    return True
def check_letters_and_digits(password):
    if not password.isalnum():
        return False
    return True
def check_number_digits(password):
    digit_sum = 0
    for digit in password:
        if digit.isnumeric():
            digit_sum += 1
    if  digit_sum < 2:
        return False
    return True

given_password = input()
result = [check_password_long(given_password),check_letters_and_digits(given_password), check_number_digits(given_password)]
if all(result):
    print("Password is valid")
else:
    if result[0] == False:
        print("Password must be between 6 and 10 characters")
    if result[1] == False:
        print("Password must consist only of letters and digits")
    if result[2] == False:
        print("Password must have at least 2 digits")