

from distutils.log import error


def run(name):
    
    try:
        if len(name) < 3: raise ValueError("No entiendo que estoy haciendo")
        newn = name[0:5]
        print(f'Hello you {newn}')
    except ValueError as ve:
        print(ve)
        

if __name__ == "__main__":
    run('Andrés')
    run('An')