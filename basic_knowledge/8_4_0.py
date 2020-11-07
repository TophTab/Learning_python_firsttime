x=['iphone case','robot pendant','dodecahedron']
y=[]
z=[]
def process(x,y):
    while x:
        temp_x=x.pop()
        print(temp_x)
        y.append(temp_x)
    print(y)
process(x[:],y)
print(y)
print(x)