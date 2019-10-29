'''
author = Honza Bilek
'''

TEXTS = ['''
    Situated about 10 miles west of Kemmerer, 
    Fossil Butte is a ruggedly impressive 
    topographic feature that rises sharply 
    some 1000 feet above Twin Creek Valley 
    to an elevation of more than 7500 feet 
    above sea level. The butte is located just 
    north of US 30N and the Union Pacific Railroad, 
    which traverse the valley. ''',

    '''At the base of Fossil Butte are the bright 
    red, purple, yellow and gray beds of the Wasatch 
    Formation. Eroded portions of these horizontal 
    beds slope gradually upward from the valley floor 
    and steepen abruptly. Overlying them and extending 
    to the top of the butte are the much steeper 
    buff-to-white beds of the Green River Formation, 
    which are about 300 feet thick.''',

    '''The monument contains 8198 acres and protects 
    a portion of the largest deposit of freshwater fish 
    fossils in the world. The richest fossil fish deposits 
    are found in multiple limestone layers, which lie some 
    100 feet below the top of the butte. The fossils 
    represent several varieties of perch, as well as 
    other freshwater genera and herring similar to those 
    in modern oceans. Other fish such as paddlefish, 
    garpike and stingray are also present.'''
    ]

user_db = {'bob' : '123', 'ann' : 'pass123' ,
           'mike' : 'password123', 'liz' : 'pass123'
            }
delimiter = 50*'-'

# user authentication
name_check = 0
psw_check = 0

print('Welcome to my application. PLease use your credentials to log in: ')
while name_check < 1:
    name = input('Name: ')
    if name not in user_db.keys():
        print('User name does not exist, please try again.')
    else:
        name_check += 1
        while psw_check < 1:
            password = input('Password: ')
            if user_db[name] == password:
                print(f'Password correct, welcome, {name}!')
                psw_check += 1
            else:
                print(f'Incorrect password, {name}, please try again')

# user's choice of text
print(delimiter)
txt_num = int(input('''We have 3 texts to be analyzed.
Enter a number btw. 1 and 3 to select: '''))-1
print(delimiter)

# definition of variables
txt_splitted = TEXTS[txt_num].split()
total_words = len(txt_splitted)
first_capital_count = 0
lowercase_count = 0
uppercase_count = 0
numeric_count = 0
numeric_sum = 0
word_length_dict = {}
n = 0

# for each word (using while loop), check conditions defined
# if True, then add 1 to counter
while n < len(txt_splitted):
    first_capital = txt_splitted[n].istitle()
    if first_capital == True:
        first_capital_count += 1

    lowercase = txt_splitted[n].islower()
    if lowercase == True:
        lowercase_count += 1

    uppercase = txt_splitted[n].isupper()
    if uppercase == True:
        uppercase_count += 1

    numeric = txt_splitted[n].isnumeric()
    if numeric == True:
        numeric_count += 1
        numeric_sum += int(txt_splitted[n])

    # using a dictionary to load word lengths and occuerence
    word_length = len(txt_splitted[n])
    if word_length not in word_length_dict.keys():
        word_length_dict.setdefault(word_length,1)
    else:
        word_length_dict[word_length] += 1

    n +=1

# print out all the results
print(f'There are {total_words} word in the selected text.')
print(f'There are {first_capital_count} titlecase words.')
print(f'There are {uppercase_count} uppercase words.')
print(f'There are {lowercase_count} lowercase words.')
print(f'There are {numeric_count} lowercase words.')
print(delimiter)

# print out the keys and values to display word lenghts and occurence
for i in sorted(word_length_dict.keys()):
    print(i, '*'*word_length_dict[i],word_length_dict[i])
print(delimiter)

# print the last result
print(f'If we summed all the numbers in this text we would get {numeric_sum}')