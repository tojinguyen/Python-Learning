while True:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kg: "))
    
    bmi = weight / (height ** 2)
    
    print("\fHello, {}!".format(name))
    print("Your BMI is: {:.2f}".format(bmi))
    
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")
    
    print("\n")
    
    again = input("Do you want to calculate again? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Thank you for using the BMI calculator!")
        break
    print("\n")