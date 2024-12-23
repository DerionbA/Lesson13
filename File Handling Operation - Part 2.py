file = open("Codingal.txt","r")
print("This file is in read mode ")
print(file.read())

file2 = open("codingal.txt","w")

file2.write("file is in write mode") 
file2.write("Hi im name is Derion and i am 13 year old")
file2.close()

file_append = open('Codingal.text', 'a')
#append in the file
file_append.write("\n File in append mode ....")
file_append.write("Hi! I am Penguin. I am !yr old")
file_append.close()


