try:
    file1 = open('sample.txt', 'r+')
    read_file = (file1.readlines())
    x, y = read_file
    print("Reading file content:")

    print('LINE 1: ', x)
    print('LINE 2: ', y)
    file1.close()
except FileNotFoundError:
    print("Error : The file 'sample.txt' was not found.")
#except NameError:
 #   print("Error : The file 'sample.txt' was not found.")
   
