import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(create):
    """Создает продукт в страйпе"""

    product_name = create.course if create.course else create.lesson
    if not product_name:
        raise ValueError("Продукт не найден")
    product = stripe.Product.create(name=product_name)
    return product


def create_stripe_price(total_sum, product_id):
    """Создает цену в страйпе"""

    amount = int(total_sum * 100)
    price = stripe.Price.create(
        currency="rub",
        unit_amount=amount,
        product=product_id,
    )
    return price


def create_stripe_session(price):
    """Создает сессию на оплату в страйпе"""

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
