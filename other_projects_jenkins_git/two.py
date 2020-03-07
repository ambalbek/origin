
def moy(aziz):
    def wrapper():
        print("print something for begining:")
        aziz()
        print("end with this:")
    return wrapper()
@moy
def moya():
    print("print main thing what you wanna say:")
