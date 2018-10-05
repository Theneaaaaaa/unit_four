grade = int(input("What grade are you in?"))

if grade <= 5:
    print("You are in lower school.")
elif grade >= 6 and grade <= 8:
    print("You are in middle school.")
else:
    print("You are in upper school.")