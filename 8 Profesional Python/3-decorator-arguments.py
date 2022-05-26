

def decoratorTest(func):
    def wrapper():
        print('I am from wrapper')
        func()
    return wrapper
   
@decoratorTest
def notDecorator():
    print('I am not from wrapper')
    
    
def notDecorator2():
    print('Me neither')
    
    

if __name__=="__main__":
    
    notDecorator()
    
    notDecorator2()
    
    
    
    
    