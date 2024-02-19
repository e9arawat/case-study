""" 
TBn
"""
from datetime import datetime


def answer(date_price, n):
    """
    return tbn of a day
    """

    sorted_data = sorted(date_price, key=lambda x: x["price"])

    top_n, bottom_n = 0, 0

    for i in range(2):
        index = -(i + 1)
        top_n += float(sorted_data[index]["price"])
        bottom_n += float(sorted_data[i]["price"])
    date_string = sorted_data[0]["date"]
    formatted_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S").strftime(
        "%Y-%m-%d"
    )
    return {"date": formatted_date, f"TB{n}": f"{(top_n- bottom_n):.2f}"}
