# when we open the app, it welcome us.
print("🙏🙏🙏welcome to OLA cab🙏🙏🙏")
# here we have to put the location of the place from which we want to go.
pickup_location=input("enter your location:")
print()
# here we have entered the location of where we want to go.
destination=input("enter your destination:")
print()
# here we have made a list of available vehicle and its details.i.e, vehicle numbers or vehicle colours.
available_vehicles=["AUTO",'MINI','PRIME SEDAN','HOURLY RENTAL','BIKE']
vehicle_numbers=['MH12 AD-9731','MH12 WE-4756','MH12-2345','MH12 PH-9876','MH12 jk-4766']
vehicle_colours=['black-white','yellow','brown','black','red-black']
# here we have iterat the list using a for loop.
for i in range(len(available_vehicles)):
    print(i+1,available_vehicles[i])
    print(' ','vehicle_numbers:',vehicle_numbers[i])
    print(' ','vehicle_colours:',vehicle_colours[i])
print()
# here we have selected one vehicle from the list.
select_vehicle=int(input("select your vehicle:"))
print()
# here we have compiled a list of riders and their details. i.e phone number and rating
riders=['ram kumar','sanjay yadav','mohan singh','rampal','roshan singh']
phone_number=['9856542310','9067453280','9077542331','7754624312','8876542323']
rating=[8,9,9.1,7,6]
# here we have iterate all the list using for loop
for i in range(len(riders)):
    print(i+1,"riders:",riders[i])
    print(" ",'phone number:',phone_number[i])
    print(" ",'rating:',rating[i])
# here we have to selected one rider frome the given list.
select_riders=input("select riders:")
print()
# to generate random numbers for km we may use the random module of python.
# to use randome number genrators, we need to first import random module.
import random
km=random.randint(1,60)
# here we get randomly distance in km.
print("your location distance is:",km)
# here we have given the rate of each vehicle according to kilometer.
rate_per_km=[8,10,12,15,18]
# here 'distance' records user input of distance to be covered format 0.00
distance=int(input("please enter your location distance:"))
# 'passengers' record the number of passenger format in interger 1or 2 etc...
passengers=int(input("how many passengers:"))
# 'fare' records the first calculatinon of rate per passenger foermat integer
fare=1*passengers
# 'mileage'records distance covered * 1.5
mileage=distance*1.5
# 'finalfare' records the total amount charged i.e fare+mileage
finalfare=fare+mileage
# here we get total fare Rs
print('your total fare is Rs:',finalfare+km*rate_per_km[select_vehicle-1])
print()
# here we have made a list of payments. like how you have to pay money. online or cash on time.
payment_methodes=['UPI id','phone pay','google pay','cash on time']
# here we iterate the given list for each element of this list using loop.
i=0
lenght=3
while i<lenght:
    print(i,payment_methodes[i])
    i=i+1
# here we select one procees from the given list.
select_payment_mothodes=input("select payment method:")
# to generate random numbers for otp we may use the random module of python.
# to use randome number genrators, we need to first import random module.
import random
otp=random.randint(1000,9000)
print("this is your one time OLA otp:",otp)
otp=int(input("enter OLA otp:"))
print()
# here we take user input to ask user if they want to procced or not.
proccess=input("do you want proccee: 1.yes, 2.no:")
if proccess=="1":
    print(finalfare+km*rate_per_km[select_vehicle-1],"Rs successfully paid")
    print("your vehicle is successfully booked")
elif proccess=="2":
    print("you have to pay in cash on time")
else:
    print("your process is canceled")