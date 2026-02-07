from faker.providers import BaseProvider, ElementsType


class EcommerceProvider(BaseProvider):
    """Faker provider for generating e-commerce fake data."""

    product_categories: ElementsType[str] = (
        "Electronics",
        "Clothing",
        "Home & Garden",
        "Sports & Outdoors",
        "Health & Beauty",
        "Toys & Games",
        "Books",
        "Automotive",
        "Groceries",
        "Pet Supplies",
        "Office Supplies",
        "Jewelry",
        "Music & Movies",
        "Baby Products",
        "Tools & Hardware",
        "Kitchen & Dining",
        "Furniture",
        "Shoes",
        "Watches",
        "Computers & Tablets",
        "Smartphones",
        "Cameras & Photography",
        "Video Games",
        "Arts & Crafts",
        "Musical Instruments",
    )

    product_adjectives: ElementsType[str] = (
        "Premium",
        "Professional",
        "Deluxe",
        "Ultra",
        "Classic",
        "Modern",
        "Vintage",
        "Eco-Friendly",
        "Organic",
        "Wireless",
        "Portable",
        "Compact",
        "Heavy-Duty",
        "Lightweight",
        "Waterproof",
        "Smart",
        "Ergonomic",
        "High-Performance",
        "Limited Edition",
        "Handcrafted",
    )

    brand_names: ElementsType[str] = (
        "Apple",
        "Samsung",
        "Sony",
        "Nike",
        "Adidas",
        "Amazon Basics",
        "Bose",
        "LG",
        "Dell",
        "HP",
        "Lenovo",
        "Logitech",
        "JBL",
        "Canon",
        "Philips",
        "Panasonic",
        "Dyson",
        "KitchenAid",
        "Cuisinart",
        "Levi's",
    )

    product_types: ElementsType[str] = (
        "Headphones",
        "Laptop",
        "Smartphone",
        "Tablet",
        "Smartwatch",
        "Speaker",
        "Camera",
        "Monitor",
        "Keyboard",
        "Mouse",
        "Backpack",
        "Sneakers",
        "Jacket",
        "Blender",
        "Coffee Maker",
        "Vacuum Cleaner",
        "Air Purifier",
        "Water Bottle",
        "Fitness Tracker",
        "Gaming Chair",
    )

    product_materials: ElementsType[str] = (
        "Cotton",
        "Leather",
        "Stainless Steel",
        "Bamboo",
        "Silicone",
        "Aluminum",
        "Titanium",
        "Carbon Fiber",
        "Ceramic",
        "Glass",
        "Wood",
        "Polyester",
        "Nylon",
        "Wool",
        "Cashmere",
        "Recycled Plastic",
    )

    shipping_carriers: ElementsType[str] = (
        "UPS",
        "FedEx",
        "USPS",
        "DHL",
        "Amazon Logistics",
        "Royal Mail",
        "Canada Post",
        "Australia Post",
        "China Post",
        "Japan Post",
        "Deutsche Post",
        "La Poste",
        "Correos",
        "PostNL",
        "Hermes",
        "GLS",
        "TNT",
        "Purolator",
        "OnTrac",
        "LaserShip",
        "Correios",
    )

    payment_methods: ElementsType[str] = (
        "Credit Card",
        "Debit Card",
        "PayPal",
        "Apple Pay",
        "Google Pay",
        "Amazon Pay",
        "Stripe",
        "Klarna",
        "Afterpay",
        "Affirm",
        "Venmo",
        "Bank Transfer",
        "Cash on Delivery",
        "Cryptocurrency",
        "Gift Card",
        "Store Credit",
        "Buy Now Pay Later",
        "Shop Pay",
        "Zip",
        "Sezzle",
    )

    order_statuses: ElementsType[str] = (
        "Pending",
        "Processing",
        "Confirmed",
        "Shipped",
        "In Transit",
        "Out for Delivery",
        "Delivered",
        "Cancelled",
        "Refunded",
        "Returned",
        "On Hold",
        "Backordered",
        "Partially Shipped",
        "Awaiting Payment",
        "Payment Failed",
    )

    customer_types: ElementsType[str] = (
        "Guest",
        "Registered",
        "VIP",
        "Gold Member",
        "Platinum Member",
        "Prime",
        "Wholesale",
        "Business",
        "Loyalty Member",
        "First-Time Buyer",
        "Returning Customer",
        "Subscriber",
    )

    return_reasons: ElementsType[str] = (
        "Defective",
        "Wrong Size",
        "Wrong Color",
        "Changed Mind",
        "Not as Described",
        "Arrived Too Late",
        "Better Price Found",
        "Duplicate Order",
        "Wrong Item Received",
        "Quality Not as Expected",
        "Missing Parts",
        "Damaged in Shipping",
        "No Longer Needed",
        "Ordered by Mistake",
        "Gift Return",
    )

    coupon_prefixes: ElementsType[str] = (
        "SAVE",
        "DEAL",
        "PROMO",
        "DISCOUNT",
        "SUMMER",
        "WINTER",
        "SPRING",
        "FALL",
        "FLASH",
        "VIP",
        "WELCOME",
        "FREESHIP",
        "EXTRA",
        "HOLIDAY",
        "SALE",
        "BLACK",
        "CYBER",
        "NEW",
        "FIRST",
        "LUCKY",
    )

    def product_category(self) -> str:
        return self.random_element(self.product_categories)

    def brand_name(self) -> str:
        return self.random_element(self.brand_names)

    def product_name(self, include_brand: bool = False) -> str:
        adjective = self.random_element(self.product_adjectives)
        product_type = self.random_element(self.product_types)
        if include_brand:
            brand = self.random_element(self.brand_names)
            return f"{brand} {adjective} {product_type}"
        return f"{adjective} {product_type}"

    def product_description(self) -> str:
        adjective = self.random_element(self.product_adjectives)
        material = self.random_element(self.product_materials)
        product_type = self.random_element(self.product_types)
        return f"A {adjective.lower()} {product_type.lower()} made with high-quality {material.lower()}."

    def shipping_carrier(self) -> str:
        return self.random_element(self.shipping_carriers)

    def payment_method(self) -> str:
        return self.random_element(self.payment_methods)

    def order_status(self) -> str:
        return self.random_element(self.order_statuses)

    def customer_type(self) -> str:
        return self.random_element(self.customer_types)

    def return_reason(self) -> str:
        return self.random_element(self.return_reasons)

    def sku(self) -> str:
        letters = "".join(self.random_uppercase_letter() for _ in range(3))
        numbers = str(self.random_int(min=1000, max=9999))
        suffix = "".join(self.random_uppercase_letter() for _ in range(2))
        return f"{letters}-{numbers}-{suffix}"

    def order_id(self) -> str:
        return f"ORD-{self.random_int(min=100000000, max=999999999)}"

    def tracking_number(self, carrier: str | None = None) -> str:
        carrier = carrier or self.random_element(self.shipping_carriers)
        if carrier == "UPS":
            alpha = "".join(self.random_uppercase_letter() for _ in range(4))
            return f"1Z{alpha}{self.random_int(min=1000000000, max=9999999999)}"
        if carrier == "FedEx":
            return str(self.random_int(min=100000000000, max=999999999999))
        if carrier == "USPS":
            return f"9400{self.random_int(min=1000000000000000, max=9999999999999999)}"
        if carrier in ("Correios", "Correos"):
            alpha = "".join(self.random_uppercase_letter() for _ in range(2))
            return f"{alpha}{self.random_int(min=100000000, max=999999999)}BR"
        if carrier == "DHL":
            return str(self.random_int(min=1000000000, max=9999999999))
        alpha = "".join(self.random_uppercase_letter() for _ in range(4))
        return f"{alpha}{self.random_int(min=1000000000, max=9999999999)}"

    def coupon_code(self) -> str:
        prefix = self.random_element(self.coupon_prefixes)
        suffix = str(self.random_int(min=10, max=99))
        return f"{prefix}{suffix}"

    def price(self, min_dollars: int = 1, max_dollars: int = 999) -> str:
        dollars = self.random_int(min=min_dollars, max=max_dollars)
        cents = self.random_int(min=0, max=99)
        return f"${dollars}.{cents:02d}"

    def discount_percentage(self) -> str:
        return f"{self.random_int(min=5, max=75)}%"

    def review_rating(self) -> int:
        return self.random_int(min=1, max=5)

    def full_order(self) -> dict[str, str | int]:
        carrier = self.shipping_carrier()
        return {
            "order_id": self.order_id(),
            "product": self.product_name(include_brand=True),
            "sku": self.sku(),
            "price": self.price(),
            "payment_method": self.payment_method(),
            "customer_type": self.customer_type(),
            "status": self.order_status(),
            "carrier": carrier,
            "tracking_number": self.tracking_number(carrier=carrier),
            "review_rating": self.review_rating(),
        }
