"""
Showcase for faker-ecommerce-provider library.

This script demonstrates the capabilities of the E-commerce Provider
for generating realistic e-commerce test data.
"""

from faker import Faker

from faker_ecommerce import EcommerceProvider


fake = Faker()
fake.add_provider(EcommerceProvider)


def print_header(title: str) -> None:
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print(f"{'=' * 70}")


def print_subheader(title: str) -> None:
    print(f"\n{title}")
    print("-" * 70)


def showcase_products() -> None:
    print_header("Products & Categories")

    print_subheader("Product Categories")
    for _ in range(5):
        print(f"  • {fake.product_category()}")

    print_subheader("Brand Names")
    for _ in range(5):
        print(f"  • {fake.brand_name()}")

    print_subheader("Product Names (without brand)")
    for _ in range(5):
        print(f"  • {fake.product_name()}")

    print_subheader("Product Names (with brand)")
    for _ in range(5):
        print(f"  • {fake.product_name(include_brand=True)}")

    print_subheader("Product Descriptions")
    for _ in range(3):
        print(f"  • {fake.product_description()}")


def showcase_orders() -> None:
    print_header("Orders & Tracking")

    print_subheader("Order IDs")
    for _ in range(5):
        print(f"  • {fake.order_id()}")

    print_subheader("SKUs")
    for _ in range(5):
        print(f"  • {fake.sku()}")

    print_subheader("Order Statuses")
    for _ in range(5):
        print(f"  • {fake.order_status()}")


def showcase_shipping() -> None:
    print_header("Shipping & Carriers")

    print_subheader("Shipping Carriers")
    for _ in range(5):
        print(f"  • {fake.shipping_carrier()}")

    print_subheader("Carrier-Specific Tracking Numbers")
    carriers = ["UPS", "FedEx", "USPS", "DHL", "Correios"]
    for carrier in carriers:
        tracking = fake.tracking_number(carrier=carrier)
        print(f"  • {carrier:<10} → {tracking}")


def showcase_payments() -> None:
    print_header("Payments & Pricing")

    print_subheader("Payment Methods")
    for _ in range(5):
        print(f"  • {fake.payment_method()}")

    print_subheader("Prices")
    for _ in range(5):
        print(f"  • {fake.price()}")

    print_subheader("Discount Percentages")
    for _ in range(5):
        print(f"  • {fake.discount_percentage()}")

    print_subheader("Coupon Codes")
    for _ in range(5):
        print(f"  • {fake.coupon_code()}")


def showcase_customers() -> None:
    print_header("Customers & Reviews")

    print_subheader("Customer Types")
    for _ in range(5):
        print(f"  • {fake.customer_type()}")

    print_subheader("Return Reasons")
    for _ in range(5):
        print(f"  • {fake.return_reason()}")

    print_subheader("Review Ratings")
    for _ in range(5):
        print(f"  • {'⭐' * fake.review_rating()}")


def showcase_full_orders() -> None:
    print_header("Complete Order Scenarios")

    for i in range(3):
        print_subheader(f"Order #{i + 1}")
        order = fake.full_order()

        print(f"\nOrder ID:      {order['order_id']}")
        print(f"Product:       {order['product']}")
        print(f"SKU:           {order['sku']}")
        print(f"Price:         {order['price']}")
        print(f"Payment:       {order['payment_method']}")
        print(f"Customer:      {order['customer_type']}")
        print(f"Status:        {order['status']}")
        print(f"Carrier:       {order['carrier']}")
        print(f"Tracking:      {order['tracking_number']}")
        print(f"Review:        {'⭐' * order['review_rating']}")


def main() -> None:
    print("\n" + "=" * 70)
    print("  FAKER E-COMMERCE PROVIDER - CAPABILITIES SHOWCASE")
    print("=" * 70)
    print("\n🛒 Generating realistic e-commerce test data for development...")

    showcase_products()
    showcase_orders()
    showcase_shipping()
    showcase_payments()
    showcase_customers()
    showcase_full_orders()

    print("\n" + "=" * 70)
    print("  End of Showcase")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
