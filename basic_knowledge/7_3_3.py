#爬山循环询问，输出最后汇总结果
the_place_to_climb={}
polling_process=True
while polling_process:
    name=input("what's your name?")
    the_place_to_climb[name]=input("which place would you like to climb?")
    verify_ifcontinue=input('continue?(type yes/no)')
    if verify_ifcontinue=='no':
        polling_process=False
print('research result:')
for name , the_place_to_climb in the_place_to_climb.items():
    print(name.title()+' prefer to climb '+the_place_to_climb.title()+'.')

