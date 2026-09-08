# Module 2 - Exercise 2 - Remodeling Project Costs
# Alex Byrd

# Initialization
Hours = float(input("Enter number of hours for job: "))
Wholesale_cost = float(input("Enter the wholesale cost of material: "))

# Process Data
Labor_cost = Hours * 30.00
Material_cost = Wholesale_cost * 1.20
Total_cost = Labor_cost + Material_cost

# Output Information
print("Labor Cost: " + str(Labor_cost))
print("Material Cost: " + str(Material_cost))
print("Total Cost: " + str(Total_cost))
