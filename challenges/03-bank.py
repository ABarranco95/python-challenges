# print("Welcome to Chase bank.")
# print("Have a nice day!")

balance = 4000
withdraw = ''
deposit = ''


def bank_transaction():
    answer = input("Hello, would you like to display balance, withdraw or deposit?\n ")

    string_answer = answer


    if string_answer:
        if string_answer == 'balance':
            print()
            return balance
        elif string_answer == 'withdraw':
            withdraw = input("How much would you like to withdraw?\n ")
            withdraw = int(withdraw)
            print((f'Your balance is now {balance - withdraw}'))
            finalize = input('Are you done?\n ')
            if finalize == 'yes':
                return 'Have a great day!'
            else:
                return answer
        elif string_answer == 'deposit':
            deposit = input("How much would you like to deposit?\n ")
            deposit = int(deposit)
            print((f'Your balance is now {balance + deposit}'))
            finalize = input('Are you done?\n ')
            if finalize == 'yes':
                return 'Have a great day!'
            else:
                return answer
        else:
            print('Have a great day!')


print(bank_transaction())



# num = input("what is your favorite number?\n ")
# num = int(num)

# print(num)
        

# check_answer = num == 11

# print(check_answer)






