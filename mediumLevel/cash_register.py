products = [
    {"id": 1, "name": "Хлеб", "price": 40},
    {"id": 2, "name": "Сыр", "price": 150},
    {"id": 3, "name": "Торт", "price": 500},
    {"id": 4, "name": "Вода", "price": 39},
    {"id": 5, "name": "Чай", "price": 95},
]

cart = []

print("===КАССОВЫЙ АППАРАТ===")
print("Список товаров:")
for p in products:
    print(f"{p['id']}. {p['name']} - {p['price']} руб.")

print("\nВведите id и количество через пробел.")
print("Введите 0, что бы закончить пробитие.")

#Ввод товара

while True:
    user_input = input("Товар (id Количество): ")
    if user_input == "0":
        break

    try:
        prod_id, quantity = map(int, user_input.split())
    except ValueError:
        print("Неверный формат.")
        continue

    product = next((p for p in products if p["id"] == prod_id),None)
    if not product:
        print("Такого товара нет.")
        continue

    cart.append({"name": product["name"], "price": product["price"], "quantity": quantity})
    print(f"Добавлено: {product['name']} x{quantity}")

#Подсчет суммы.

total = sum(item["price"] * item["quantity"] for item in cart)
print(f"\nОбщая сумма покупки: {total} руб.")

#Ввод оплаты.

while True:
    try:
        paid = int(input("Сколько дал покупатель: "))
        if paid < total:
            print("Недостаточно! Покупатель дал меньше, чем нужно.")
        else:
            break
    except ValueError:
        print("Введите число.")

change = paid - total

#Вывод чека.

print("\n=== ЧЕК ===")
for item in cart:
    print(f"{item['name']} x{item['quantity']} = {item['price'] * item['quantity']} руб.")
print("----------------------------")
print(f"ИТОГО: {total} руб.")
print(f"Получено: {paid} руб.")
print(f"Сдача: {change} руб.")
print("============================")
print("Спасибо за покупку!")
