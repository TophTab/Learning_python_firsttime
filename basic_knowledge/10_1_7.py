with open('E:\code\pi_million_digits.txt') as file_object:
    lines=file_object.readlines()
pi_string=''
for line in lines:
    pi_string+=line.strip()

birthday=input("Enter your birthday,in the form mmddyy:")
if birthday in pi_string:
    print('your birthday appears in the first million digits of pi')
else:
    print("your birthday does not appear in the first million digits of pi")