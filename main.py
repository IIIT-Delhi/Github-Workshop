def greet(name, lastname):
    print(f"Hello, {name} {lastname}!")

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    user_last_name = input("Enter your last name")
    greet(user_name, user_last_name)