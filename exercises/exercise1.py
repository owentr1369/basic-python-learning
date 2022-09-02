Weight = input("Weight:")

Unit = input("(K)g or (L)bs:")

if (Unit.lower() == "k"):
    print(Weight + "kg")
elif (Unit.lower() == 'l'):
    print(str(float(Weight) * 0.45) + "lbs")
else:
    print("Please enter available unit (K or L)")
