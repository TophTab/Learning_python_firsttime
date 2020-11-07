ages=[18,15,2,66]
for age in ages:
    if age>=18:
        print("adult")
    elif age<18 and age>12:
        print("teenager")
    else:
        print('kid')