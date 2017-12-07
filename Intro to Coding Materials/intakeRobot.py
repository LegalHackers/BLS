print("Welcome!")
print("Press 1 for copyright help.")
print("Press 2 for patent help.")
print("Press 3 for trademark help.")      
userInput = int(input("How can I help you today? "))

#if user hits 1 then ask if you are being sued.
#if user hits 2 then call Chris
#if user hits 3 then say "ok we can help"
#if none of the above then say you're sorry

def firstQuestion (response):
    if response == 1:
        print("Are you being sued?")
    elif response == 2:
        print("Call Chris")
    elif response == 3:
        print("OK we can help!")
    else: 
        print("We're sorry!")
        
firstQuestion (userInput)        