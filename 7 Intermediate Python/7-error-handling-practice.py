

def test(num):    
    
    try:
        if type(num) == str: raise TypeError('helo error')
        assert num >= 0, "it is no bigger than 0"
        return 2 + int(num)
    except:
        print('something went wrong')
    finally:
        print('we are in finally')



if __name__ == "__main__":
    
    print( test(-1) )
    print( test('22') )