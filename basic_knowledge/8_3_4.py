def build_full_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name=first_name+' '+middle_name+' '+last_name
    else:
        full_name=first_name+' '+last_name
    return full_name.title()

while True:
    print('\ntell me ur name:')
    print('(enter "q" to exit)')
    f_name=input('first name=')
    if f_name=='q':
        break
    l_name=input('last name=')
    if l_name=='q':
        break

    f_name=build_full_name(f_name,l_name)
    print('Hello,'+f_name+'!')