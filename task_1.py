"""
Task - 1
"""
import csv
from datetime import datetime


def get_merged_data(dam_data, avg_rtm):
    """
    return final data
    """
    final_data = []
    for dam_row in dam_data:
        if dam_row["Settlement Point"] == "HB_NORTH":
            date_str = dam_row["Delivery Date"]
            hour = int(dam_row["Delivery Hour"])
            dam_price = float(dam_row["Settlement Point Price"])
            if (date_str, hour) in avg_rtm:
                rtm_price = avg_rtm[(date_str, hour)]
                date_time = datetime.strptime(date_str + f" {hour - 1}", "%m/%d/%Y %H")
                date_formatted = date_time.strftime("%Y-%m-%d %H:%M:%S")
                row_data = {
                    "date": date_formatted,
                    "dam": f"{float(dam_price):.2f}",
                    "rtm": f"{float(rtm_price):.2f}",
                }
                final_data.append(row_data)
    return final_data


def answer():
    """
    Task - 1
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
                price = float(row["Settlement Point Price"])
                if (date, hour) not in rtm_data:
                    rtm_data[(date, hour)] = [price]
                else:
                    rtm_data[(date, hour)].append(price)

    avg_rtm = {}
    for k, v in rtm_data.items():
        date, hour = k
        hourly_price = sum(v) / 4
        avg_rtm[(date, hour)] = round(hourly_price, 2)

    final_data = get_merged_data(dam_data, avg_rtm)

    with open("task_1.csv", "w", encoding="utf-8", newline="") as f:
        fieldnames = ["date", "dam", "rtm"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in final_data:
            writer.writerow(row)


if __name__ == "__main__":
    answer()
