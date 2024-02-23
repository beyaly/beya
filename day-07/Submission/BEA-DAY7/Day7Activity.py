file =  open('day-07/Submission/BEA-DAY7/user_info.txt', 'w')

user_input = input("What is your name? ")

file.write(user_input)

file.close()