while True:
    marital_status = input("What is your relationship status? (Single or Married):").lower().strip()

    if marital_status == "single":
        tax_percentage = "50"
    elif marital_status == "married":
        tax_percentage = "80"

    try:
        print("Congrats on being {}! Your tax percentage is {}".format(marital_status, tax_percentage))
            
        while True:
            try:
                annual_salary = int(input("What is your annual salary? (in USD):" ))

                print("TODO: Do some math using Tax Percentage {}% and Salary ${}".format(tax_percentage, annual_salary))
                break

            except ValueError:
                print("Error! This is not a number. Try again.")
        break
    
    except UnboundLocalError:
        print("Invalid input, let's try that again...")
