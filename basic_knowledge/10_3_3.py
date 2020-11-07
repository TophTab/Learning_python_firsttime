print('first number/second number,Dont use 0 as second number')
print("use 'q' to exit")
while True:
    first_number=input("\nFirst number:")

    second_number=input("second number:")
    if first_number=='q' or second_number=='q':
        break
    try:
        answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("Dont use 0 as second number")
    else:
        print(answer)
