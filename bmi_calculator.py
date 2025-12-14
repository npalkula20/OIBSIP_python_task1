def get_valid_input(prompt, min_value, max_value):
    while True:
        try:
            value = float(input(prompt))
            if value < min_value or value > max_value:
                print(f"Please enter a value between {min_value} and {max_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

weight = get_valid_input("Enter your weight in kilograms: ", 1, 300)
height = get_valid_input("Enter your height in meters: ", 0.5, 2.5)

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print("\n--- BMI Result ---")
print(f"Your BMI is: {bmi:.2f}")
print(f"Category: {category}")
