def build_profile(f_name,l_name,**info):
    profile={}
    profile['first name']=str(f_name)
    profile['last name']=str(l_name)
    for keyword,detail in info.items():
        profile[keyword]=detail
    return profile
user_profile=build_profile('ablert','einsein',place='princetion',field='physics')
print(user_profile)