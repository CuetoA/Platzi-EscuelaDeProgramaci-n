
def returning_strings(x):
    
    def repeat(string):        
        for i in range(x):
            print(string)
    
    
    return repeat
        

if __name__ == "__main__":
    repeat3 = returning_strings(3)
    repeat5 = returning_strings(5)
    
    del(returning_strings)
    
    repeat3('Hey Oh!')
    repeat5('oh ')
    