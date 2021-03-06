promos = []


def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


@promotion
def fidelity(order):
    """为积分1000以上的提供5%的折扣"""
    return order.total() * 0.5 if order.customer.fidelity >= 1000 else 0


@promotion
def bulk_item(order):
    """单个20以上的商品10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total * 0.1
    return discount


@promotion
def large_order(order):
    """10个以上不同商品7%折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total * 0.07
    return 0


def best_promo(order):
    return max(promo(order) for promo in promos)
