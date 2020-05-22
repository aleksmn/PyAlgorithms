TAX_RATE = 1.1
SHIPPING_DEFAULT = 5

def calculateTotal(items, options = {'shipping': SHIPPING_DEFAULT, 'discount': None}):
    if (items is None or len(items) == 0): return 0
    total = 0
    for item in items:
        total += item.get('price') * item.get('quantity')
    discountRate = 1 - (options.get('discount') or 0)   
    return total * discountRate * TAX_RATE + options.get('shipping')


testItems = (
    {'price' : 15, 'quantity': 2},
    {'price' : 20, 'quantity': 1},
    {'price' : 5, 'quantity': 4}
)


print(calculateTotal(testItems))
print(calculateTotal(testItems, {'shipping': 0}))
print(calculateTotal(testItems, {'shipping': 10}))
