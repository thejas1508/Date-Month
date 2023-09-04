Month = str(input("Enter the Month Name:"))
if (Month == "JAN" or Month == "MAR" or Month == "MAY" or Month == "JUL" or Month == "AUG" or       Month == "OCT" or Month == "DEC"):
      print("31 Days in This Month")
elif (Month == "APR" or Month == "JUN" or Month == "SEP" or Month == "NOV"):
      print("30 Days in This Month")
elif (Month == "FEB"):
      print("28 or 29 Days in This Month")
else:
      print("INVALID MONTH")


OUTPUT:
Enter the Month Name:AUG
31 Days in This Month
Enter the Month Name:SEP
30 Days in This Month
Enter the Month Name:FEB
28 or 29 Days in This Month

