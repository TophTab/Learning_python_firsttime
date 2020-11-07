with open('programming.txt','a') as file_object:
    file_object.write("I also love finding\n")
    file_object.write('I love creating\n')
with open('programming.txt','r') as file_object:
    print(file_object.read())