""" 
Modified TBn
"""
from datetime import datetime


def answer(date_price, n):
    """
    Modified TBn
    """
    # date_price = [
    #     {'hour': 1, 'price': 70},
    #     {'hour': 2, 'price': 30},
    #     {'hour': 3, 'price': 40},
    #     {'hour': 4, 'price': 20},
    #     {'hour': 5, 'price': 50},
    #     {'hour': 6, 'price': 30},
    #     {'hour': 7, 'price': 40},
    #     {'hour': 8, 'price': 20},
    # ]
    final_top, final_bottom = [], []

    for _ in range(n):
        extra_bottom = {}
        bottom = {}
        top = {}
        for data in date_price:
            if not top and not bottom:
                top, bottom, extra_bottom = data, data, data
            elif top == bottom and top["price"] > data["price"]:
                top, bottom, extra_bottom = data, data, data

            elif bottom["price"] > data["price"] and top["price"] > data["price"]:
                if extra_bottom["price"] > data["price"]:
                    extra_bottom = data
            elif top["price"] <= data["price"]:
                top = data
                bottom = extra_bottom

        final_top.append(top["price"])
        final_bottom.append(bottom["price"])
        if top == bottom:
            date_price.remove(top)
        else:
            date_price.remove(top)
            date_price.remove(bottom)

    print(final_top, final_bottom)
    date_string = date_price[0]["date"]
    formatted_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S").strftime(
        "%Y-%m-%d"
    )
    return {
        "date": formatted_date,
        f"TB{n}": f"{(sum(final_top) - sum(final_bottom)):.2f}",
    }
