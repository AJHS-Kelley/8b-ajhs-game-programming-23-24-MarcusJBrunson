# This is a method for testing code and preventing crashes. 
# try -- except -- else -- finally 

try: # The code in this block is ALWAYS excuted.
    myVaraible = 1 
    print(myVaraibl)
except NameError: # This code will run if there is an error (exception)
    print("There is an incorrect variable name in your code.")
except:
    print("Something has gone wrong!") 
else: # This code runs if there are no ERRORS
    print("Code excuted correctly with no exceptions.\n")
finally: # This code always runs, it's like the TERMINATOR 
    print("I'll be back")