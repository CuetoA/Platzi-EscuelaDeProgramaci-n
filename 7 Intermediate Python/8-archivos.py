def read():
    numbers = []
    with open("./7 Intermediate Python/archivos/numbers.txt", "r", encoding="utf-8") as f:
        print(f)
        
        for line in f:
            numbers.append(line)
    
    print(numbers)
    


def writte():
    names = ['Scar', 'Trujis', 'Maxbb', 'ivu']
    with open("./7 Intermediate Python/archivos/numbers.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(f"{name}\n")

    

def run():
    read()
    writte()


if __name__ == "__main__":
  run()  