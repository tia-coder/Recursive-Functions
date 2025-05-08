def printGreeting(number):
    greeting = 0
    if number == 1:
        greeting = "Good Morning!"
    else:
        greeting = "Good Afternoon!"
    
    newGreeting = greeting * number
    print(newGreeting)
    
    
def computeResult(value) :
    print("value", value)
    result = 1
    if value > 1 :
        result = value * computeResult(value - 1)  
        printGreeting(result)
    return result

num = 5

print(computeResult(num))   
  