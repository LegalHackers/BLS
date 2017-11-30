'''
This is a comment, when the code runs, it will ignore whatever is inside the triple-quotes.
These sections are to describe a bit about the code.

REMINDERS:
To mess around with python, just open up terminal and type "python" to try what you want and see the results

Save this file on your desktop as 'program.py', the name doesn't really matter but I will assume it is program.py
To run a program from a file, open up terminal.
Type 'ls' and hit enter to see the directories you can go to.
Type 'cd' and type the name of the directory you want to go to (in this case, type 'cd desktop')
Then type 'python' and the name of your program (in this case, 'python program.py'), hit enter!
'''

'''
Lines 22-25 creates a FUNCTION, called printHelloALot.
A function is basically a list of instructions,
and at the end of the list you return to where
you were previously. The tab from the left hand side indicates it is part of the list.
When you write a statement to EXECUTE that function, such as in line 36
the progam jumps up to the list, executes those statements,
then comes back to line 36.
'''
def printHelloALot():
    print("hello")
    print("hello")
    print("hello")

'''
Each of these lines executes a FUNCTION
In this case, we go to the list, run down the list, come back
go to the list again, again run down the list and come back
then print 5
then go to the list one final time, and again run down the list and come back.
Since the code goes from top to bottom, we will print "hello" 6 times
then print the 5, and then follow up with the final 3 "hello"s
'''
printHelloALot()
printHelloALot()
print(5)
printHelloALot()

'''
We also covered variables, which look like this
'''
x = 6
'''
This sets the variable 'x' to the value 6, now we can use it
however we want, and even reset it to another value if we want to.
Consider these:
'''
print(x + 7) ''' 13 '''
print(x * 2) ''' 12 '''
print(x * x) ''' 36 '''
x = 7
print(x * x) ''' x is now 7, so this is 49 '''
