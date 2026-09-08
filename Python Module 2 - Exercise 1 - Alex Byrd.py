# Module 2 - Exercise 1 - Hazel's Housecleaning Service
# Alex Byrd

#Initialization
Last_name = input("Enter last name: ")
Num_bathrooms = float(input("Enter the number of bathrooms: "))
Num_other_rooms = float(input("Enter the number of other rooms: "))

#Process Data
Bathroom_cost = Num_bathrooms * 15.00
Other_rooms_cost = Num_other_rooms * 10.00
Total_cost = Bathroom_cost + Other_rooms_cost + 40.00

#Output Information
print("Customer: " + str(Last_name))
print("Bathrooms: " + str(Num_bathrooms) + " Cost: " + str(Bathroom_cost))
print("Other Rooms: " + str(Num_other_rooms) + " Cost: " + str(Other_rooms_cost))
print("Total Cost: " + str(Total_cost))
print("Program complete")
