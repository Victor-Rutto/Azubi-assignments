# Victor_Rutto
charge = int(input("Please enter the charge for the food item you want to order "))
tip_charges = round(charge*0.18, 2)
sale_tax = round(charge*0.07, 2)

# print(f"The charge for the food: ${charge}")
print(f"Tip: ${tip_charges}")
print(f"Sales tax: ${sale_tax}")
grand_total = charge + tip_charges + sale_tax
print(f"Grand total: ${grand_total}")



