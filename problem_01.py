def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

def get_numbers():
    numbers_str = input("Enter numbers separated by spaces: ")
    try:
        numbers = numbers_str.split()
        numbers = [int(num) for num in numbers]
        return numbers
    except ValueError:  # verifica input 
        print("Invalid value")
        return []

def main():
    numbers = get_numbers()
    if numbers:  #verifica valor de numbers para fazer o cálculo
        print("Average:", calculate_average(numbers))
        print("Maximum:", find_max(numbers))
    else:
        print("Invalid values")
        

if __name__ == "__main__":
    main()