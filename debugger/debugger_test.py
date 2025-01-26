def calculate_average(numbers):
    total = sum(numbers)  # Sum of numbers
    count = len(numbers)  # Number of items
    average = total / count  # Calculate average
    return average

def main():
    data = [10, 20, 30, 40, 50]
    print("Original data:", data)

    # Simulating an issue: Adding a string to the list
    data.append("sixty")  # Error: Adding a string instead of a number

    try:
        avg = calculate_average(data)  # This line will throw an error
        print(f"The average is: {avg}")
    except Exception as e:
        print("An error occurred:", e)

    # # Logic error: Checking for even numbers incorrectly
    # even_numbers = [x for x in data if x % 2 == 0]  # TypeError due to the string
    # print("Even numbers:", even_numbers)

if __name__ == "__main__":
    main()
