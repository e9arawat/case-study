""" 
TBn
"""


def answer(date_price, n):
    """
    return tbn of a day
    """

    sorted_data = sorted(date_price, key=lambda x: x[1])

    top_n = bottom_n = 0

    for i in range(2):
        index = -(i + 1)
        top_n += float(sorted_data[index][1])
        bottom_n += float(sorted_data[i][1])

    return {"date": sorted_data[0][0], f"TB{n}": f"{(top_n- bottom_n):.2f}"}
