def apply_discount(price, discount):
    discounted_price = price*(1-discount)

    assert 0 <= discounted_price <= price

    return discounted_price


print(apply_discount(100, 0.2))

print(apply_discount(100, 2))
