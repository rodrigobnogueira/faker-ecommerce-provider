# faker-ecommerce-provider

[![PyPI version](https://img.shields.io/pypi/v/faker-ecommerce-provider)](https://pypi.org/project/faker-ecommerce-provider/)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

Faker provider for generating realistic e-commerce fake data.

## Installation

```bash
pip install faker-ecommerce-provider
```

## Usage

```python
from faker import Faker
from faker_ecommerce import EcommerceProvider

fake = Faker()
fake.add_provider(EcommerceProvider)

# Basic usage
fake.product_name()  # 'Premium Leather Electronics Item'
fake.product_name(include_brand=True)  # 'Sony Modern Wireless Headphones'
fake.brand_name()  # 'Samsung'
fake.product_description()  # 'A modern headphones made with high-quality stainless steel.'
fake.sku()  # 'ABC-1234-XY'
fake.order_id()  # 'ORD-123456789'
fake.tracking_number()  # '1ZABCD1234567890'
fake.tracking_number(carrier="USPS")  # '9400100000000000000000'
fake.price()  # '$49.99'
fake.shipping_carrier()  # 'FedEx'
fake.payment_method()  # 'Apple Pay'

# Generate a complete order
order = fake.full_order()
print(order)
# {
#   'order_id': 'ORD-891234567',
#   'product': 'Apple Classic Aluminum Laptop',
#   'sku': 'DLL-4821-KP',
#   'price': '$899.99',
#   'payment_method': 'Credit Card',
#   'customer_type': 'Prime',
#   'status': 'Shipped',
#   'carrier': 'UPS',
#   'tracking_number': '1Z87654...',
#   'review_rating': 5
# }
```

💡 **Tip**: Run `python showcase.py` to see all available features and examples!

## Available Methods

| Method | Example |
|--------|---------|
| `product_name()` | Premium Leather Electronics Item |
| `product_name(include_brand=True)` | Samsung Modern Smartphone |
| `brand_name()` | Apple, Sony, Nike |
| `product_description()` | A modern laptop made with high-quality aluminum. |
| `product_category()` | Electronics, Clothing, Home & Garden |
| `sku()` | ABC-1234-XY |
| `order_id()` | ORD-123456789 |
| `tracking_number()` | 1ZABCD1234567890 |
| `price()` | $49.99 |
| `discount_percentage()` | 25% |
| `shipping_carrier()` | FedEx, UPS, DHL |
| `payment_method()` | Credit Card, PayPal, Apple Pay |
| `order_status()` | Pending, Shipped, Delivered |
| `customer_type()` | Guest, VIP, Prime |
| `return_reason()` | Wrong Size, Defective |
| `coupon_code()` | SAVE20 |
| `review_rating()` | 1-5 |
| `full_order()` | Dictionary with complete order details |

## Running Tests

To run the tests, install the dependencies and run pytest:

```bash
pip install .[dev]
pytest tests/
```

## License

MIT
