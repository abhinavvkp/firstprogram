import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Name"       : ["Aman","Diya","Rahul","Sneha","Arjun"],
     "Department" : ["CS" , "IT" , "CS" , "ECE" , "IT"],
       "Marks"      : [78,92,85,67,74],
         "Attendance" : [85,90,88,75,80],
             "Grade"      : ["B" ,"A" , "A" ,"C" ,"B"]
}
df = pd.DataFrame(data)
print("\ndataset Information:")
print(df.info())
print("\n2.Statistical Summary:")
print(df.describe())
print("\n3.Student Names and Marks:")
print(df[["Name" , "Marks"]])
print("\n4.Student Scoring more than 80 Marks:")
print(df[df["Marks"]>80])
print("\n5.student Sorted by Marks:")
print(df.sort_values("Marks", ascending = False))
df["Bonus"] = 5
print("\n6.Dataset after Adding Bonus:")
print(df.to_string(index = False , justify = "center"))
