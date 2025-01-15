# user='bloody jaydeep'
# user='Fool jaydeep'.lower()
user='Fucd aydeep'.lower()
# user='Fusd aydeep'.lower()
if 'bloody' in user:
    print(user.lstrip('bloody'))
    
if 'bloody' in user:
    print(user.replace('bloody','@@'))  
elif 'fool' in user:
    print(user.replace('Fool','@@'))
elif 'fuc' in user:
    print(user.replace('fuc','@@'))
else:
    print(user)
    
# for loop in this to make short and also array 