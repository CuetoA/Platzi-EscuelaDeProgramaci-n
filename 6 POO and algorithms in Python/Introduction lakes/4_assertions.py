

from multiprocessing.dummy import Array


def firstLetter(words_array):
    new_list = []
    
    for word in words_array:
        
        try:
            assert type(word) == str, f'{word} is not a string'
            assert len(word) > 0, 'no empty strings allowed'    
            new_list.append(word[0])
        except AssertionError as e:
            print(e)    
            pass
        
    return new_list

if __name__ == "__main__":
    
    firstLetter(['hola', 3])