def add():
    while True:
        try:
            int(input('Please provide the number:'))
        except:
            print('please prolvide the number not a word')
            continue
        else:
            print('there you go')
            break
        finally:
            print("end of try")
add()

