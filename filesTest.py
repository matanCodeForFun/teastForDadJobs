import pandas as pd

sheet_name = input("Enter the sheet name: ")
CATEGORY = input("Enter the category to search: ")
thing = input("What to find: ")


df = pd.read_excel('אקסל דיווח נתוני אשראי 2025.xlsx', sheet_name=sheet_name)

results = df[df[CATEGORY].str.contains(thing, na=False)]

print(results)