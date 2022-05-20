# Decoradores:      Añaden funcionalidades a una función
# Metaprogramación: Cambiar el código mientras de ejecuta


def decorate_function(function):
    def wrapper():
        print("This is the last message...")
        function()
        print("This is the first message...")
    return wrapper

# Forma 2
@decorate_function
def zumbido():
    print('bzzzzzz')

zumbido() 


# Forma 1
# zumbido = decorate_function(zumbido)
# zumbido()   