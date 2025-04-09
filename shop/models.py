from django.db import models
from django.core.mail import send_mail

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, default="")
    subcategory = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='images/', max_length=250, null=True, blank=True)
    image_secondary = models.ImageField(upload_to='images/', max_length=250, null=True, blank=True)
    description = models.TextField()
    is_on_sale = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.product.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Admin ko email
        subject = "🛒 New Order Received"
        message = (
            f"🛍️ New order placed!\n\n"
            f"Product: {self.product.name}\n"
            f"Customer Name: {self.customer_name}\n"
            f"Email: {self.customer_email}\n"
            f"Phone: {self.phone}\n"
            f"Address: {self.address}, {self.city} - {self.postal_code}"
        )

        send_mail(
            subject=subject,
            message=message,
            from_email="sandeeppal8471@gmail.com",  # Gmail ka email
            recipient_list=["sandeepppal8471@gmail.com"],  # Admin email
            fail_silently=False,
        )
