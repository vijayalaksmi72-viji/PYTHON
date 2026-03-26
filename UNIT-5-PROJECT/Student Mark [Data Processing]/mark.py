import csv

students = [
    {"Name": "Vinoth", "Tamil": 78, "English": 82, "Maths": 88, "Physics": 91, "Chemistry": 85, "Computer Science": 95},
    {"Name": "Ravi", "Tamil": 69, "English": 74, "Maths": 77, "Physics": 80, "Chemistry": 72, "Computer Science": 90},
    {"Name": "Nithiya", "Tamil": 55, "English": 60, "Maths": 58, "Physics": 62, "Chemistry": 57, "Computer Science": 85},
    {"Name": "Harish", "Tamil": 81, "English": 79, "Maths": 92, "Physics": 89, "Chemistry": 90, "Computer Science": 96},
    {"Name": "Radha", "Tamil": 72, "English": 68, "Maths": 75, "Physics": 78, "Chemistry": 74, "Computer Science": 91},
    {"Name": "Kumar", "Tamil": 50, "English": 55, "Maths": 60, "Physics": 58, "Chemistry": 54, "Computer Science": 80},
    {"Name": "Pavithra", "Tamil": 88, "English": 84, "Maths": 91, "Physics": 93, "Chemistry": 89, "Computer Science": 97},
    {"Name": "Joe", "Tamil": 67, "English": 70, "Maths": 73, "Physics": 75, "Chemistry": 71, "Computer Science": 89},
    {"Name": "Suji", "Tamil": 52, "English": 57, "Maths": 55, "Physics": 60, "Chemistry": 53, "Computer Science": 82},
    {"Name": "Ram", "Tamil": 85, "English": 80, "Maths": 94, "Physics": 90, "Chemistry": 92, "Computer Science": 98},
    {"Name": "Sita", "Tamil": 70, "English": 66, "Maths": 74, "Physics": 76, "Chemistry": 73, "Computer Science": 90},
    {"Name": "Mani", "Tamil": 48, "English": 52, "Maths": 50, "Physics": 55, "Chemistry": 49, "Computer Science": 78}
]

subjects = ["Tamil","English","Maths","Physics","Chemistry","Computer Science"]

for stu in students:
    total = sum(stu[sub] for sub in subjects)
    stu["Total"] = total
    stu["Average"] = round(total / 6, 2)

    if all(stu[sub] >= 35 for sub in subjects):
        stu["Result"] = "Pass"
    else:
        stu["Result"] = "Fail"

for stu in students:
    avg = stu["Average"]
    if avg >= 90:
        stu["Grade"] = "A+"
    elif avg >= 80:
        stu["Grade"] = "A"
    elif avg >= 70:
        stu["Grade"] = "B"
    elif avg >= 60:
        stu["Grade"] = "C"
    elif avg >= 50:
        stu["Grade"] = "D"
    else:
        stu["Grade"] = "F"

 with open("mark.csv", "w", newline="") as f:
    fieldnames = ["Name","Tamil","English","Maths","Physics","Chemistry","Computer Science",
                  "Total","Average","Grade","Result"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

print("12th Student Mark data saved successfully")

with open("mark.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)