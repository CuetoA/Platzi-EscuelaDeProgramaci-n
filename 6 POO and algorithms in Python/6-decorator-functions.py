def decorate_function(function):
    def wrapper():
        print("This is the last message...")
        function()
        print("This is the first message...")
    return wrapper

@decorate_function
def zumbido():
    print('bzzzzzz')


zumbido()    
# zumbido = decorate_function(zumbido)
# zumbido()