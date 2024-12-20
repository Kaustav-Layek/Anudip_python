''' A transport company charges the fare according to following table:
Distance Charges
1-50 	8 Rs./Km
51-100 	10 Rs./Km
> 100 	12 Rs/Km

'''
#Taking the distance as an input

distance=float(input("Enter the distance travelled"))
if(distance>=1 and distance<=50):
    charge=distance*8
elif(distance>50 and distance<=100):
    charge=(50*8)+((distance-50)*10)
else:
    charge=(50*8)+(10*50)+((distance-100)*12)
print(f"The total charge = {charge}")