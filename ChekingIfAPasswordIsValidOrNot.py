# author : Sarvin Nami
password = input('Please enter your password here : ')
n = bool
def passwordConditions (word) :
    if(len(word) >= 8 and (not word.isnumeric()) and (not word.isalpha())) :
        n = False
    else :
        n = True
passwordConditions(password)
while True :
    if n == False :
        password = input('You didnt comply the password conditions. It should be at least 8 characters contains numbers and alphabets. Please enter again : ')
        passwordConditions(password)
    else :
        break
print(f'your password successfully arranged. It is {password}.')