import json

number=[2,3,5,7,11,13]
with open('numbers.json','w') as f_obj:
    json.dump(number,f_obj)