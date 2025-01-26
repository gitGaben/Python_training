def greet():
    print("Hello from the greet function!")

print("This will always run when, even if the script is imported.")

if __name__ == "__main__":
    print("This runs only when the script is executed directly.")
    greet()