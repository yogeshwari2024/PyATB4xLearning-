# Break concept : it break the code execution after break statement
# based on condition, exit the loop


for i in range(0, 10):
    print(i)
    if i == 5:
        break
##########

for i in range(0, 10, 1):
    if i == 6:
        print(i)
        # break
    else:
        print("no op")

## pass keyword : used to pass/ignore

print("\n")
for i in range(0, 10, 1):
    if i == 6:
        print(i)
    else:
        pass
