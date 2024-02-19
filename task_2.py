""" 
Task - 2
"""
import csv
from datetime import datetime, timedelta


def get_final_data(dam_data, rtm_data):
    """
    return the mergerd data
    """
    final_data = []
    for dam_row in dam_data:
        if dam_row["Settlement Point"] == "HB_NORTH":
            date_str = dam_row["Delivery Date"]
            hour = int(dam_row["Delivery Hour"])
            dam_price = float(dam_row["Settlement Point Price"])
            date_time = datetime.strptime(date_str, "%m/%d/%Y")
            for interval in range(1, 5):
                rtm_price = rtm_data[(date_str, hour)][interval]
                time = (hour - 1) * 60 + (interval - 1) * 15
                date_time_interval = date_time + timedelta(minutes=time)
                date_formatted = date_time_interval.strftime("%Y-%m-%d %H:%M:%S")
                row_data = {
                    "date": date_formatted,
                    "dam": f"{float(dam_price) : .2f}",
                    "rtm": f"{float(rtm_price) : .2f}",
                }
                final_data.append(row_data)
    return final_data


def answer():
    """
    Task - 2
    """
    with open("DAM_Prices_2022.csv", "r", encoding="utf-8-sig") as f:
        csv_reader = csv.DictReader(f)
        dam_data = list(csv_reader)

    rtm_data = {}
    with open("RTM_Prices_2022.csv", "r", encoding="utf-8-sig") as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            if row["Settlement Point"] == "HB_NORTH":
                date = row["Delivery Date"]
                hour = int(row["Delivery Hour"])
                interval = int(row["Delivery Interval"])
                price = float(row["Settlement Point Price"])
                if (date, hour) not in rtm_data:
                    rtm_data[(date, hour)] = {1: 0, 2: 0, 3: 0, 4: 0}
                rtm_data[(date, hour)][interval] = price

    final_data = get_final_data(dam_data, rtm_data)

    with open("task_2.csv", "w", encoding="utf-8-sig", newline="") as output_file:
        fieldnames = ["date", "dam", "rtm"]
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in final_data:
            writer.writerow(row)


if __name__ == "__main__":
    answer()
