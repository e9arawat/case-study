"""
rtm
"""
import csv
import os
from answer import answer


def solver():
    """
    Creates a csv file with TBn revenue
    """
    file_path = os.path.abspath("task_1.csv")
    with open(file_path, "r", encoding="utf-8-sig") as f:
        csv_reader = csv.DictReader(f)
        data = list(csv_reader)
        dam_data, rtm_data = [], []
        for x in data:
            dam_data.append({"date": x["date"], "price": float(x["dam"])})
            rtm_data.append({"date": x["date"], "price": float(x["rtm"])})
        dam_nb2, rtm_nb2 = [], []
        for index in range(0, len(dam_data), 24):
            dam_nb2.append(answer(dam_data[index : index + 24], 2))
            rtm_nb2.append(answer(rtm_data[index : index + 24], 2))
        with open("modified_dam_tb2.csv", "a", encoding="utf-8", newline="") as f:
            fieldnames = ["date", "TB2"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for row in dam_nb2:
                writer.writerow(row)


if __name__ == "__main__":
    solver()
