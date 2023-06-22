def app():
    file = open('archivo.txt', 'w')
    file.write('Hola Mundo!\n')
    file.close()

    file = open('archivo.txt', 'r+')
    file.readline()
    file.write('Tarea de OpenBootCamp!\n')

    file.seek(0)

    for line in file:
        print(line)

    file.close()



if __name__ == '__main__':
    app()