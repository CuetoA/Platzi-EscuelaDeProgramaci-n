def mayorFunction ():
    print('Mayor function')
    
    def nestedFunctionOne ():
        print('First nested function')
        
    def nestedFunctionTwo ():
        print('Second nested function')
        
    nestedFunctionOne()
    nestedFunctionTwo()
        
if __name__ == "__main__":
    mayorFunction()