price_input = float(input())
item_count = 0
total_price = 0
price_list = []


while price_input != 0:
    item_count += 1
    total_price += price_input 
    price_list.append(price_input)
    price_input = float(input())


if item_count == 0:
    total_price = round(float(total_price), 1)
    print(f"Number of items: {item_count}\n"
          f"Total price: {total_price}")


elif item_count != 0:
    total_price = round(float(total_price), 1)
    min_price = min(price_list)
    print(f"Number of items: {item_count}\n"
          f"Total price: {total_price}\n"
          f"Lowest price: {min_price}")