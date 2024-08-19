import time
import uuid
import hashlib



print("LogLibary v.0.8.5")
print('')
basepath = r"C:\Users\ivan\Documents\My Python Projects\LogLibrary\Program files"




def hash_password(password):
    # uuid используется для генерации случайного числа
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


def reading(p2):
    with open(basepath+'\\'+p2, 'r', encoding='utf-8') as logfile:
        lfcontent = logfile.read()
    return lfcontent


def open4edit(p2):
    with open(basepath+'\\'+p2, 'r', encoding='utf-8') as logfiler:
        lfcontent = logfiler.read()
    print('Before editing version:')
    print(lfcontent)
    print('Your current version:')
    with open(basepath+'\\'+p2, 'w+', encoding='utf-8') as logfilew:
        lf = input()
        logfilew.write(lf)


def create(p2):
    with open(basepath+'\\'+p2, 'w+', encoding='utf-8') as logfile:
        logtext = input('Type your text: ')
        logfile.write(logtext)


def findnum():
    with open(basepath+"\\phone numbers.txt", 'r+', encoding='utf-8') as txtfile:
        contents = txtfile.read().split('\n')
        if contents == ['']:
            print("Your phone number's book is curently empty")
            return None
        phones = {}
        for i in contents:
            i = i.lower().split(':')
            print(i)
            phones[i[0]] = phones.get(i[0], []) + [i[1]]
        [print(key, *phones[key]) for key in phones.keys()]
        s = input().lower()
        print(phones.get(s, f"The '{s}' is not in the list"))


def addnum():
    with open(basepath+"\\phone numbers.txt", 'a', encoding='utf-8') as txtfile:
        print("type in new number in format <name>:<number>")
        while True:
            s = input()
            if ':' not in s:
                print('Wrong synthaxis. Try again.')
                continue
            else:
                break
        txtfile.write('\n'+s)



counter = 0
with open(basepath+"\\pass.txt", "r") as my_file:
    filec = my_file.read()    

if filec != "":
    while True:
        answer = input('Enter the password: ')
        if check_password(filec, answer):
            print('Password accepted. Welcome Mr. Robot!')
            break
        else:
            counter = counter + 1
            if counter == 3:
                print("You have 3 wrong attempts. Please try again in 5 minutes")
                time.sleep(300)
                continue
            print('Password is incorrect. Please try again')
else:
    answer = input('Enter the password: ')
    while True:
        answerlenth = len(answer)
        if answerlenth >= 6:
            break
        else:
            print('Password lenth should be not less than 6 symbols. Your password lenth:', answerlenth, 'symbols')
            answer = input()
    answer2 = input('Enter the password again to confirm: ')
    while True:
        if answer == answer2:
            print('Password accepted. Welcome Mr. Robot!')
            break
        else:
            print('Password is incorrect. Please try again')
            print('First enter:', answer) 
            print('Second enter:', answer2)  
            answer2 = input()

pw = answer
hash_pw = hash_password(pw)
with open(basepath+"\pass.txt", "w") as file:
    file.write(hash_pw)



print('')
print('====================================================')
print('The list of available commands:')
print("   Read - to read your .txt files")
print('   Edit - to edit your .txt files')
print('   Create file - to create new .txt files')
print('   Close - to close program')
print('   Find phone number - to find a phone number')
print('   Add new phone number - to add new phone number')
print('====================================================')
print('')



while True:
    in_com = input('Please enter a command to proced: ').lower()
    if in_com == 'read':
        p2 = input('Enter file name: ')
        if p2[-4:] != '.txt':
            p2 += '.txt'
        rp2 = reading(p2)
        print(rp2) 
        continue
    if in_com == 'edit':
        p2 = input('Enter file name: ')
        if p2[-4:] != '.txt':
            p2 += '.txt'
        open4edit(p2)
        continue
    if in_com == 'create file':
        p2 = input('Enter file name: ')
        if p2[-4:] != '.txt':
            p2 += '.txt'
        create(p2)
        continue
    if in_com == 'find phone number':
        findnum()
        continue
    if in_com == 'add new phone number':
        addnum()
        continue
    if in_com == 'close':
        quit()
    if in_com == 'credits':
        print("Made by Gorshenin Ivan in 2024")
    else:
        print(f"The '{in_com}' is not the valid command. Please try again")
