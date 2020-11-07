try:
    with open('alice.txt') as f_obj:
        contents=f_obj.read()
except FileNotFoundError:
    print("Sorry,the file "+'alice.txt'+" doesn't exist.")
else:
    words=contents.split()
    num_words=len(words)
    print("The file alice.txt has about "+str(num_words)+"words.")