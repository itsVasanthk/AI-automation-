import csv

with open("leads.csv", "r") as file:

    reader = csv.reader(file)

    next(reader)

    with open("lead_report.txt", "w") as report:

        report.write("Lead Report\n")
        report.write("--------------------\n\n")

        for row in reader:

            name = row[0]
            email = row[1]
            company = row[2]
            phone = row[3]

            report.write(
                f"Name: {name}\n"
            )

            report.write(
                f"Email: {email}\n"
            )

            report.write(
                f"Company: {company}\n"
            )

            report.write(
                f"Phone: {phone}\n"
            )

            report.write(
                "\n-----------------\n\n"
            )

print("Report generated successfully")