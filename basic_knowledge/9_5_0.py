from collections import OrderedDict

favorite_languages=OrderedDict()

favorite_languages['jen']='python'
favorite_languages['mike']='c++'
favorite_languages['lucy']='ruby'
for name,language in favorite_languages.items():
    print(name.title()+" like "+language.title())