'''
Check if the given number is valid by using a statemachine.
'''

class STATE:
    START, INTEGER, DECIMAL, FRACTION, UNKNOWN = range(5)

def getCurrentState(currentState, c):
    if (currentState == STATE.START):
        if c >= '0' and c <= '9':
            return STATE.INTEGER
        elif c == '.':
            return STATE.DECIMAL
        else:
            return STATE.UNKNOWN
    
    if (currentState == STATE.DECIMAL):    
        if c >= '0' and c <= '9':
            return STATE.DECIMAL
        elif c == '/':
            return STATE.FRACTION
        elif c == '.':
            return STATE.UNKNOWN
        else:
            return STATE.UNKNOWN
            
    if (currentState == STATE.INTEGER):
        if c >= '0' and c <= '9':
            return STATE.DECIMAL
        elif c == '/':
            return STATE.FRACTION
        elif c == '.':
            return STATE.DECIMAL
        else:
            return STATE.UNKNOWN
     
    if (currentState == STATE.FRACTION):
        if c >= '0' and c <= '9':
            return STATE.FRACTION
        elif c == '/':
            return STATE.UNKNOWN
        elif c == '.':
            return STATE.FRACTION
        else:
            return STATE.UNKNOWN


def isNumberValid(str):
    i = 0
    if str[i] == '+' or str[i] == '-':
        i = i + 1
    
    currentState = STATE.START
    for c in str[i:]:
        currentState = getCurrentState(currentState, c)
        if currentState == STATE.UNKNOWN:
            return False
    
    return True    
    
def main():
        
        print("===================================================")
        print("============== Number Validity Test ===============")
        print("===================================================\n\n\n\n\n")

        num = input("Please enter a number/String which can be checked for validity: ")
        validity = isNumberValid(num)
        validString = None
        if validity:
            validString = "Valid"
        else:
            validString = "Not Valid"
        print("The entered number/String {0} is {1}".format(num, validString))    
        
if __name__ == "__main__":
    main()        
    
