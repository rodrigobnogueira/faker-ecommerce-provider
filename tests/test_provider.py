import pytest
from faker import Faker
from faker_ecommerce import EcommerceProvider


@pytest.fixture
def faker():
    fake = Faker()
    fake.add_provider(EcommerceProvider)
    return fake


class TestEcommerceProvider:
    def test_product_category(self, faker):
        for _ in range(100):
            result = faker.product_category()
            assert isinstance(result, str)
            assert result in EcommerceProvider.product_categories

    def test_product_name(self, faker):
        for _ in range(100):
            result = faker.product_name()
            assert isinstance(result, str)
            assert len(result.split()) >= 2

            # Test with brand included
            result_branded = faker.product_name(include_brand=True)
            assert isinstance(result_branded, str)
            assert len(result_branded.split()) >= 3
            
            # Check if any brand name is at the start of the result
            found_brand = False
            for brand in EcommerceProvider.brand_names:
                if result_branded.startswith(brand):
                    found_brand = True
                    break
            assert found_brand, f"Brand not found in {result_branded}"

    def test_brand_name(self, faker):
        for _ in range(100):
            result = faker.brand_name()
            assert isinstance(result, str)
            assert result in EcommerceProvider.brand_names

    def test_product_description(self, faker):
        for _ in range(100):
            result = faker.product_description()
            assert isinstance(result, str)
            assert result.startswith("A ")
            assert result.endswith(".")

    def test_shipping_carrier(self, faker):
        for _ in range(100):
            result = faker.shipping_carrier()
            assert isinstance(result, str)
            assert result in EcommerceProvider.shipping_carriers

    def test_payment_method(self, faker):
        for _ in range(100):
            result = faker.payment_method()
            assert isinstance(result, str)
            assert result in EcommerceProvider.payment_methods

    def test_order_status(self, faker):
        for _ in range(100):
            result = faker.order_status()
            assert isinstance(result, str)
            assert result in EcommerceProvider.order_statuses

    def test_customer_type(self, faker):
        for _ in range(100):
            result = faker.customer_type()
            assert isinstance(result, str)
            assert result in EcommerceProvider.customer_types

    def test_return_reason(self, faker):
        for _ in range(100):
            result = faker.return_reason()
            assert isinstance(result, str)
            assert result in EcommerceProvider.return_reasons

    def test_sku(self, faker):
        for _ in range(100):
            result = faker.sku()
            assert isinstance(result, str)
            assert "-" in result
            parts = result.split("-")
            assert len(parts) == 3

    def test_order_id(self, faker):
        for _ in range(100):
            result = faker.order_id()
            assert isinstance(result, str)
            assert result.startswith("ORD-")

    def test_tracking_number(self, faker):
        for _ in range(100):
            result = faker.tracking_number()
            assert isinstance(result, str)
            assert len(result) >= 10

        # Test carrier specific formats
        assert faker.tracking_number(carrier="UPS").startswith("1Z")
        assert faker.tracking_number(carrier="USPS").startswith("9400")
        assert faker.tracking_number(carrier="Correios").endswith("BR")

    def test_coupon_code(self, faker):
        for _ in range(100):
            result = faker.coupon_code()
            assert isinstance(result, str)
            assert len(result) >= 4

    def test_price(self, faker):
        for _ in range(100):
            result = faker.price()
            assert isinstance(result, str)
            assert result.startswith("$")
            assert "." in result
            
            # Test limits
            min_val = 10
            max_val = 50
            price_str = faker.price(min_dollars=min_val, max_dollars=max_val)
            price_val = float(price_str.replace("$", ""))
            assert min_val <= price_val < (max_val + 1)

    def test_discount_percentage(self, faker):
        for _ in range(100):
            result = faker.discount_percentage()
            assert isinstance(result, str)
            assert result.endswith("%")

    def test_review_rating(self, faker):
        for _ in range(100):
            result = faker.review_rating()
            assert isinstance(result, int)
            assert 1 <= result <= 5

    def test_full_order(self, faker):
        for _ in range(10):
            order = faker.full_order()
            assert isinstance(order, dict)
            assert "order_id" in order
            assert "product" in order
            assert "sku" in order
            assert "price" in order
            assert "payment_method" in order
            assert "customer_type" in order
            assert "status" in order
            assert "carrier" in order
            assert "tracking_number" in order
            assert "review_rating" in order
            
            # Check consistency between carrier and tracking number
            carrier = order["carrier"]
            tracking = order["tracking_number"]
            
            if carrier == "UPS":
                assert tracking.startswith("1Z")
            elif carrier == "USPS":
                assert tracking.startswith("9400")
            elif carrier in ("Correios", "Correos"):
                assert tracking.endswith("BR") or tracking[-2:].isalpha() # Correos might not end in BR but Correios does
                if carrier == "Correios":
                    assert tracking.endswith("BR")

    def test_uniqueness(self, faker):
        # Generate a batch of IDs and ensure they are unique
        ids = {faker.order_id() for _ in range(1000)}
        assert len(ids) == 1000, "Order IDs should be unique"
        
        skus = {faker.sku() for _ in range(1000)}
        assert len(skus) == 1000, "SKUs should be unique"
