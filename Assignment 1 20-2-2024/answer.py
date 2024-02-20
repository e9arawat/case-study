""" 
Modified TBn
"""
from datetime import datetime


def answer(date_price, n):
    """
    Modified TBn
    """

    tb2 = 0
    for _ in range(2):
        max_difference = 0
        top = {}
        bottom = {}
        for index, data in enumerate(date_price):
            temp = date_price[:index]
            if not temp:
                continue
            temp_b = min(temp, key=lambda x: x["price"])
            if data["price"] - temp_b["price"] > max_difference:
                max_difference = data["price"] - temp_b["price"]
                top = data
                bottom = temp_b

        if top == bottom:
            date_price.remove(top)
        else:
            date_price.remove(bottom)
            date_price.remove(top)
        tb2 += max_difference
    date_string = date_price[0]["date"]
    formatted_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S").strftime(
        "%Y-%m-%d"
    )
    return {
        "date": formatted_date,
        f"TB{n}": f"{tb2:.2f}",
    }
