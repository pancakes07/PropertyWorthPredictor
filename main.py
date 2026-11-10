from property_pkg import calculate_base_value, adjust_property_value, compare_price, generate_report

print("===== PROPERTY WORTH PREDICTOR =====")

area = float(input("Enter property area (sq.ft.): "))
rate = float(input("Enter locality rate per sq.ft.: "))

condition = input("Enter property condition (New/Good/Needs Renovation): ")

asking_price = float(input("Enter seller asking price: "))

base_value = calculate_base_value(area, rate)

estimated_value = adjust_property_value(base_value, condition)

difference, status = compare_price(estimated_value, asking_price)

generate_report(area, rate, condition, estimated_value, asking_price, difference, status)