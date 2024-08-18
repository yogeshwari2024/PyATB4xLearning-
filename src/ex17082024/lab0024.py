# Literals - actuval values assigned , it can be numeric & non-numerice

# Escape sequence

print("Hello World")
print("Hello\nWorld")   # \n-> new line
print("Hello\tWorld")   # \t -> tabline
print("Hello\bWorld")   # \b -> backspace

#dir = 'C:\pramod\n.txt'  -- getting error in escape sequence
#dir = "C:\pramod\n.txt"  -- it will give the line with \n Newline


# where this r concept will be used?
# in Automation API, web Automation, file_path = r concept

# r means raw string

dir = r"C:\pramod\n.txt"
dir2 = r'C:\pramod\n.txt'
print(dir)
print(dir2)

# Excape seq -- single

name  = 'pramod\'utta'  # \n with new line as utta
name2 = "pramod'utta"
print(name)
print(name2)