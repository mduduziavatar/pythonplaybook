# access txt files using open() r+ is to read and write read only is r and a is to append 
 
countryFile = open("countries.txt", "r+")
countryFile.write("\nZimbabwe")
#check if file is readable
print(countryFile.readable())

# entire lines from txt file you can also look directly per index number
print(countryFile.readline())

# looping through the lines
for lines in countryFile.readlines():
    print(lines)

countryFile.close()    
