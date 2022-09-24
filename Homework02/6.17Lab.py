pwd_str = input()
new_pwd = ""
for i in pwd_str:
    if i == 'i':
        new_pwd = new_pwd + "!"
    elif i == 'a':
        new_pwd = new_pwd + "@"
    elif i == 'm':
        new_pwd = new_pwd + "M"
    elif i == 'B':
        new_pwd = new_pwd + "8"
    elif i == 'o':
        new_pwd = new_pwd + "."
    else:
        new_pwd = new_pwd + i
print(new_pwd+"q*s")
