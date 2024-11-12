from django.db import models


class PropertyListing(models.Model):
    HOUSE_TYPE_CHOICES = [
        ('villa', '빌라/주택'),
        ('officetel', '오피스텔'),
        ('apartment', '아파트'),
        ('commercial', '상가/사무실'),
    ]

    TRANSACTION_TYPE_CHOICES = [
        ('monthly_rent', '월세'),
        ('jeonse', '전세'),
        ('sale', '매매'),
    ]

    title = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    description = models.TextField()
    area = models.DecimalField(max_digits=10, decimal_places=2)
    floor_number = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    parking_spaces = models.PositiveIntegerField()
    year_built = models.PositiveIntegerField()
    maintenance_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    neighborhood_description = models.TextField(blank=True)
    images = models.ImageField(upload_to='property_images/')
    house_type = models.CharField(
        max_length=20,
        choices=HOUSE_TYPE_CHOICES,
        default='villa'
    )
    transaction_type = models.CharField(
        max_length=20,
        choices=TRANSACTION_TYPE_CHOICES,
        default='sale'
    )

   

    def __str__(self):
        return self.title


