import pandas as pd
import os

sheet_name = input("Enter the sheet name: ")
CATEGORY = input("Enter the category to search: ")
thing = input("What to find: ")

file = os.chdir('C:/Users/Matan/Documents/אקסל דיווח נתוני אשראי 2025')
    
df = pd.read_excel(file, sheet_name=sheet_name)

results = df[df[CATEGORY].str.contains(thing, na=False)]

print(results)