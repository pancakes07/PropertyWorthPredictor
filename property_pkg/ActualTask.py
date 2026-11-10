def calculate_base_value(area, rate):
    if area <= 0:
        raise ValueError("Property area must be positive")

    if rate <= 0:
        raise ValueError("Property rate must be positive")

    return area * rate


def adjust_property_value(base_value, condition):
    adjustments = {
        "new": 0.05,
        "good": 0,
        "needs renovation": -0.10
    }

    condition = condition.lower()

    if condition not in adjustments:
        raise ValueError("Invalid property condition")

    return base_value * (1 + adjustments[condition])


def compare_price(estimated_value, asking_price):
    if estimated_value <= 0 or asking_price <= 0:
        raise ValueError("Prices must be positive")

    difference = ((asking_price - estimated_value) / estimated_value) * 100

    if difference > 10:
        status = "OVERPRICED"
    elif difference < -10:
        status = "UNDERVALUED"
    else:
        status = "FAIRLY PRICED"

    return difference, status


def generate_report(area, rate, condition, estimated_value, asking_price, difference, status):

    print("\n========== PROPERTY VALUATION REPORT ==========")
    print("        PROPERTY WORTH PREDICTOR")

    print("Property Area:", area, "sq.ft.")
    print("Locality Rate: Rs.", rate, "per sq.ft.")
    print("Property Condition:", condition)

    print("-----------------------------------------------")

    print("Estimated Property Value: Rs. {:,.0f}".format(estimated_value))
    print("Seller Asking Price: Rs. {:,.0f}".format(asking_price))
    print("Price Difference: {:.2f}%".format(difference))

    print("-----------------------------------------------")

    print("FINAL ASSESSMENT:", status)

    print("================================================")