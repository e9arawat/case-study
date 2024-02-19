"""
Task - 1
"""
import csv
from datetime import datetime


def answer():
    """
    Task - 1
    """
    with open("DAM_Prices_2022.csv", "r", encoding="utf-8-sig") as f:
        csv_reader = csv.DictReader(f)
        dam_data = []
        for row in csv_reader:
            if row["Settlement Point"] == "HB_NORTH":
                dam_data.append(row)

    with open("RTM_Prices_2022.csv", "r", encoding="utf-8-sig") as f:
        csv_reader = csv.DictReader(f)
        rtm_data = []
        for row in csv_reader:
            if row["Settlement Point"] == "HB_NORTH":
                rtm_data.append(row)

    print(rtm_data[0]["Settlement Point Price"])

    with open("task_1.csv", "w", encoding="utf-8", newline="") as f:
        fieldnames = ["date", "dam", "rtm"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        index = 0
        for data in dam_data:
            date_obj = datetime.strptime(data["Delivery Date"], "%m/%d/%Y")
            formatted_date = (
                date_obj.strftime("%Y-%m-%d")
                + " "
                + str(int(data["Delivery Hour"]) - 1).zfill(2)
                + ":00:00"
            )
            rtm = 0
            for _ in range(4):
                rtm += float(rtm_data[index]["Settlement Point Price"])
                index += 1
            rtm /= 4
            dam = data["Settlement Point Price"]
            row_data = {
                "date": formatted_date,
                "dam": f"{float(dam):.2f}",
                "rtm": f"{float(rtm):.2f}",
            }
            writer.writerow(row_data)


if __name__ == "__main__":
    answer()
