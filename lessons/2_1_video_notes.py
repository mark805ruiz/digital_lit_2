milesDriven = input("Enter miles driven:")
milesDriven = float(milesDriven)

gallonsUsed = input("Enter miles used:")
gallonsUsed = float(gallonsUsed)

mpg = milesDriven / gallonsUsed
print("Your mpg:" + str(mpg))
#last line could also be
#print("Your mpg:", mpg)
