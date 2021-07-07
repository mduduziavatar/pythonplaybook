try:
    x =int(input('Enter a number:' ))
    print(x)
except ValueError: #inbuilt function to look up required value
    print('Please enter a number')    
finally: # unsures program gets to end if no found errors
    print("Its all good!!")    