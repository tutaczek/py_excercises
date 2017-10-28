tableData = [['jabłka', 'pomarańcze', 'wiśnie', 'banany'],
             ['Alicja', 'Bob', 'Karol', 'Dawid'],
             ['psy', 'koty', 'łosie', 'gęsi']]


def printTable():
    width = 15
    for col in range(0, 4):
        for row in range(0, 3):
            print(tableData[row][col].rjust(width), end = '')
        print('')

printTable()
    
    
    




    






      

    





    
