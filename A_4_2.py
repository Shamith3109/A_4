file1 = open ('output.txt', 'w')
a = file1.write(input('Enter text write to the file: ' )+ "\n")
print('Data successfully written to output.txt.\n')
file1.close()

file2 = open ('output.txt', 'a')
b = file2.write(input('Enter additional text to apppend: ' ))
print('Data successfully appended.\n')
file2.close()

file3 = open ('output.txt', 'r')
read_file = (file3.readlines())
x, y = read_file
print("Final content of output.txt: ")
print(x)
print(y)
file3.close()