def ask():
    while True:
        try:
            result=int(input("please provide a number: "))
            
        except:
            print('whoops! this is not a number. try again')
            continue
        else:
            print("your number is squared",result**2)
            break
        finally:
            ("im going to ask you again")
ask()
input()
