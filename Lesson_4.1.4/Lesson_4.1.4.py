def palindr(str):
    revstr = str[::-1]
    if str == revstr:
        print(str,"is palindr")
    else:
        print(str,"is not palindr")

palindr(input())