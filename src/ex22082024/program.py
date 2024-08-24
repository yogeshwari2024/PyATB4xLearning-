user_type = input("enter the user type, admin, manager, guest\n")
user_type = user_type.lower()
match user_type:
    case "admin" | "manager":
        print("hello sir")
    case "guest":
        print("hello guest")
    case _:
        print("hello there")
