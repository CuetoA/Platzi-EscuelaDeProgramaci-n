

def hello(name):
    return print(f'Hello {name}')

def letsGo(activity):
    return print(f"let\'s go {activity}")

def proppertySetter(functionToExecute , name):
    
    return functionToExecute(name)


if __name__== "__main__":
    
    proppertySetter(hello, 'Andrés')
    proppertySetter(letsGo, 'Andrés')