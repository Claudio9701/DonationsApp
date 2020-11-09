import uuid
from django.db import models

# Create your models here.
class Beneficiary(models.Model):
    national_identity_document = models.CharField(max_length=8)

    class Meta:
        verbose_name_plural = 'Beneficiaries'


class Donor(models.Model):
    INDIVIDUAL = 'IND'
    LEGAL = 'LEG'
    TYPE_OF_PERSON_CHOICES = [
        (INDIVIDUAL, 'Individual'),
        (LEGAL, 'Legal'),
    ]
    type_of_person = models.CharField(
        max_length=3,
        choices=TYPE_OF_PERSON_CHOICES,
    )
    single_taxpayer_register = models.CharField(max_length=13)
    contact_name = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=9)
    contact_email = models.EmailField()


class Partner(models.Model):
    single_taxpayer_register = models.CharField(max_length=13)
    contact_name = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=9)
    contact_email = models.EmailField(blank=True, null=True)
    bank_account_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    location_latitude = models.FloatField(blank=True, null=True)
    location_longitude = models.FloatField(blank=True, null=True)
    products_or_services = models.ManyToManyField("Product")


class Product(models.Model):
    NON_PERISHABLE_FOODS = 'NPF'
    PERISHABLE_FOODS = 'PEF'
    TOILETRIES = 'TLT'
    HYGIENE = 'HYG'
    ACCEPT_CARDS = 'ACC'
    DIGITAL_WALLET = 'DGW'
    PET_FOOD = 'PTF'
    BANK_AGENT = 'BAG'
    PRODUCT_CHOICES = [
        (NON_PERISHABLE_FOODS, 'Non Perishable Foods'),
        (PERISHABLE_FOODS, 'Perishable Foods'),
        (TOILETRIES, 'Toiletries'),
        (HYGIENE, 'Hygiene Items'),
        (ACCEPT_CARDS, 'Accept Cards'),
        (DIGITAL_WALLET, 'Digital Wallet'),
        (PET_FOOD, 'Pet Food'),
        (BANK_AGENT, 'Bank Agent'),
    ]
    name = models.CharField(
        max_length=3,
        choices=PRODUCT_CHOICES
    )


class Donation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    donor = models.ForeignKey("Donor", on_delete=models.CASCADE)
    partner = models.ForeignKey("Partner", on_delete=models.CASCADE)
    beneficiary = models.ForeignKey("Beneficiary", on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    amount = models.FloatField()
    ON_PREPARATION = 'PRE'
    READY_TO_PICKUP = 'RTP'
    DELIVERED = 'DLV'
    STATUS_CHOICES = [
        (ON_PREPARATION, 'On preparation'),
        (READY_TO_PICKUP, 'Ready to be picked up'),
        (DELIVERED, 'Delivered'),
    ]
    status = models.CharField(max_length=3, choices=STATUS_CHOICES)
