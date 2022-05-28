

def decoratorTest(func):
    def wrapper(*args, **kwargs):
        print('\n---\n')
        func(*args, **kwargs)
    return wrapper
   
@decoratorTest
def notDecorator(name):
    print(f'Hi I am {name}')
    
@decoratorTest
def notDecorator2(name, adjective):
    print(f'Hi My girls name is {name} and she is {adjective}')
    
    

if __name__=="__main__":
    
    notDecorator('Andrés')
    
    notDecorator2('Scarlette', 'OLD')
    
    
    
    
    