total=0
print("expense tracker ")
while True:
    expense=input("enter the expense amount (or type 'done' to quit): ")

    if expense.lower() == 'done':
        break
    total=total + float(expense)

    
print(f"total expenses so far: {total}")