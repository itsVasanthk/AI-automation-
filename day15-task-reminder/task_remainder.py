import csv
from datetime import datetime

task=input("Enter task: ")

date=input(
"Enter due date (YYYY-MM-DD): "
)

with open(
    "tasks.csv",
    "a",
    newline=""
) as file:

    writer=csv.writer(file)

    writer.writerow(
        [task,date]
    )

print(
"\nTask saved."
)

print("\nUpcoming Tasks:\n")

with open(
    "tasks.csv",
    "r"
) as file:

    reader=csv.reader(file)

    for row in reader:

        task=row[0]

        due=row[1]

        due_date=datetime.strptime(
            due,
            "%Y-%m-%d"
        )

        days_left=(
            due_date-datetime.now()
        ).days

        print(
            f"{task} → {days_left} days left"
        )