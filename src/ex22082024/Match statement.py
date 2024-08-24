# Match statement == switch in java
# match the op and execute

# syntax:
'''

match varaible:
    case pattern1:
        #code block
    case pattern2:
        #code block

'''

# write a program to ask the user which browser he wants to run automation

browser = input("Enter the browser name \n")
browser = browser.lower()  # due to this it will give the lower case chrome execute

match browser:
    case "firefox":
        print("execute the firefox code")
    case "chrome":
        print("execute the chrome code")
    case "edge":
        print("execute the edge code")
    case _:
        print("browser not found")
