def get_numbers():
    # This function prompts the user to enter a list of numbers and returns it.
    input_numbers = input("Enter a list of numbers separated by spaces: ")
    numbers = [float(num) for num in input_numbers.split()]
    return numbers

def square_numbers(numbers):
    # This function squares each number in the given list.
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2

def display_numbers(numbers):
    # This function displays the squared numbers.
    print("Squared numbers:")
    for num in numbers:
        print(num, end=' ')

def main():
    # Main function to orchestrate the process
    numbers = get_numbers()
    square_numbers(numbers)
    display_numbers(numbers)

if __name__ == "__main__":
    main()
