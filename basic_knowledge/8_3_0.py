def build_full_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name=first_name+' '+middle_name+' '+last_name
    else:
        full_name=first_name+' '+last_name
    return full_name.title()

musician=build_full_name('jimmy','cold')
print(musician)

musician=build_full_name('jimmy','cold','a')
print(musician)