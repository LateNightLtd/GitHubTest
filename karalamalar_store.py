import stores
import products


def default_inventory() -> list:
    """To Test default items would be added to the store"""
    items_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                  products.Product("Bose QuietComfort Earbuds",
                                   price=250, quantity=500),
                  products.Product("Google Pixel 7",
                                   price=500, quantity=250),
                  ]
    store = stores.Store(items_list)
    # Adding one more item
    phone = products.Product("Samsung S10",
                             price=100, quantity=100)
    store.add_product(phone)
    return items_list


def validate_user_answer():
    questions = ["Which product # do you want? ", "What amount do you want? "]
    basket = []
    while True:
        answers = []
        for question in questions:
            answer = input(question)
            if answer.isnumeric():
                answer = int(answer)
            answers.append(answer)
        is_any_not_int = any(not isinstance(item, int) for item in answers)
        if is_any_not_int:
            break
        basket.append(answers)
    return basket


def make_an_order(store) -> None:
    products_cost = 0
    available_products = store.get_all_products()  # list of object
    available_products_string_list = [
        str(product) for product in store.get_all_products()]
    availables_str = ("\n".join(f"{count}. {item}" for count, item in enumerate(
        available_products_string_list, start=1)))
    make_order_view = """{line}
{items}
{line}\n""".format(line="-"*6, items=availables_str)
    print(make_order_view)
    chosen_products = validate_user_answer()
    # list of lists, lists first value is index, second value quantity of request
    if chosen_products:
        for item in chosen_products:
            item_index = item[0] - 1
            item_requested_quantity = item[1]
            product = available_products[item_index]
            product_cost = product.price * item_requested_quantity
            products_cost += product_cost

    print(f"Order made! Total payment: ${products_cost}")


urunler = default_inventory()
TEMP = stores.Store(urunler)
make_an_order(TEMP)
