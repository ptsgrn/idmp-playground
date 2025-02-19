from django.db import models


class Substance(models.Model):
    """ สารออกฤทธิ์ตามมาตรฐาน IDMP (ISO 11238) """
    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    """ ผู้ผลิตยา """
    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MedicinalProduct(models.Model):
    """ ผลิตภัณฑ์ยา (ISO 11615) """
    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=255, unique=False)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PharmaceuticalProduct(models.Model):
    """ รูปแบบของยา (ISO 11616) """
    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    medicinal_product=models.ForeignKey(
        MedicinalProduct, on_delete=models.CASCADE)
    dosage_form=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.medicinal_product.name} ({self.dosage_form})"
