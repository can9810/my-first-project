pw=12345
print("請入密碼:")

if (int(input())==pw):
    print("歡迎!")
else:
    print("密碼錯誤!!!")
    for pw in range(1):
            print("請重新輸入密碼:")
    if (int(input())==pw):
            print("歡迎!")
    else:
            print("密碼錯誤!!!")
    for pw in range(1):
            print("請重新輸入密碼:")
    if (int(input())==pw):
            print("歡迎!")
    else:
            print("密碼錯誤!!!")
