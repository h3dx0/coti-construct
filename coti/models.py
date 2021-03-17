from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import EmailValidator
from django.db import models


# Create your models here.
class Person(AbstractUser):
    email_validator = EmailValidator()

    objects = UserManager()
    telephone = models.CharField(max_length=10)

    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Correo electrónico',
        help_text='Debe agregar un correo electronico válido',
        validators=[email_validator],
        error_messages={
            'unique': "El correo electrónico seleccionado ya está siendo usando en el sistema.",
        },
    )

    class Meta:
        ordering = ['first_name']


class Seller(Person):
    commission = models.DecimalField(max_digits=5, decimal_places=3)


class Client(Person):
    catchment = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    out_number = models.CharField(max_length=255)
    int_number = models.CharField(blank=True, null=True, max_length=255)
    cp = models.IntegerField()
    colony = models.CharField(max_length=255)
    municipality = models.CharField(max_length=255)
    state = models.CharField(max_length=255)


class TInstallation(models.Model):
    name = models.CharField(unique=True, max_length=255)
    price = models.DecimalField(max_digits=19, decimal_places=2)


class TColor(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True, blank=True)


class TPresentation(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True, blank=True)


class TPayment(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True, blank=True)
    commission = models.DecimalField(max_digits=5, decimal_places=3)


class Piece(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True, blank=True)
    high = models.DecimalField(max_digits=12, decimal_places=6)
    width = models.DecimalField(max_digits=12, decimal_places=6)
    thickness = models.DecimalField(max_digits=12, decimal_places=6)
    area = models.DecimalField(max_digits=12, decimal_places=6)
    weight = models.DecimalField(max_digits=12, decimal_places=6)
    price = models.DecimalField(max_digits=19, decimal_places=2)

    def __str__(self):
        return self.name


class Profile(Piece):
    price_in_usd = models.BooleanField(default=True)

    @staticmethod
    def obj_type():
        return 'PROFILE'


class Frame(Piece):
    frame_profile = models.ForeignKey(Profile, on_delete=models.PROTECT)

    @staticmethod
    def obj_type():
        return 'FRAME'


class Accessory(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(null=True, blank=True)
    units = models.IntegerField()
    price = models.DecimalField(max_digits=19, decimal_places=2)
    units_by_sqr_meters = models.BooleanField(default=False)
    price_in_usd = models.BooleanField(default=False)
    presentation = models.ForeignKey(TPresentation, on_delete=models.PROTECT)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)


class Material(models.Model):
    installation_area = models.DecimalField(max_digits=12, decimal_places=6)
    installation_area_wasted = models.DecimalField(max_digits=12, decimal_places=6)
    pieces = models.DecimalField(max_digits=12, decimal_places=6)
    pieces_closeup = models.IntegerField()
    area_check = models.DecimalField(max_digits=12, decimal_places=6)
    profile_price = models.DecimalField(max_digits=19, decimal_places=2)
    profile_price_in_usd = models.BooleanField(default=True)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
    installation = models.ForeignKey(TInstallation, on_delete=models.PROTECT)
    color = models.ForeignKey(TColor, on_delete=models.PROTECT)


class AccessoryMaterial(models.Model):
    units_by_sqr_meters = models.IntegerField()
    total_units = models.IntegerField()
    total_units_presentation = models.IntegerField()
    accessory_price = models.DecimalField(max_digits=19, decimal_places=2)
    accessory_price_in_usd = models.BooleanField(default=False)
    accessory = models.ForeignKey(Accessory, on_delete=models.PROTECT)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)


class FrameMaterial(models.Model):
    lineal_meters = models.DecimalField(max_digits=12, decimal_places=6)
    units = models.DecimalField(max_digits=12, decimal_places=6)
    units_closeup = models.IntegerField()
    frame_price = models.DecimalField(max_digits=19, decimal_places=2)
    frame = models.ForeignKey(Frame, on_delete=models.PROTECT)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)


class Valuation(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)
    comments = models.TextField(blank=True, null=True)
    private_comments = models.TextField(blank=True, null=True)
    delivery_time = models.DateField()
    exchange_rate = models.DecimalField(max_digits=12, decimal_places=6)
    payment = models.ForeignKey(TPayment, on_delete=models.PROTECT)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
