# BMI calculator - Kevin (11C)
# This is used for calculating the users BMI and indicate their body shape

# Defining functions
def calc_BMI(height: float, weight: float)->float:
    return weight/((height/100)**2)

# Main program
print("Hello, welcome to the BMI calculator")
h = float(input("Please input your height in cm:"))
w = float(input("Please input your weight in kg:"))

bmi = calc_BMI(h, w)
print(f"Your BMI is {bmi}")

if(bmi < 18.5):
  print("You are underweight!")
elif(bmi > 25):
  print("You are overweight!")
else:
  print("You are in normal range.")