code=[2,5,6,2,4,0,2,5,1,3,6,1]
months={"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
date=int(input("Enter the date : "))
month=input("Enter the first three letters of the month with first letter being capital : ")
weeks=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

print("The provided date lies on " + weeks[(date+code[months[month]-1])%7])