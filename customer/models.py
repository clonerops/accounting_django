from django.db import models

# Create your models here.
class Customer(models.Model):
    firstName = models.CharField(max_length=255, null=True, blank=True, verbose_name="نام")
    lastName = models.CharField(max_length=255, null=True, blank=True, verbose_name="نام خانوادگی")
    fatherName = models.CharField(max_length=255, null=True, blank=True, verbose_name="نام پدر")
    nationalCode = models.CharField(max_length=10, unique=True, verbose_name="کدملی")
    birthDate = models.DateField(null=True, blank=True, verbose_name="تاریخ تولد")
    mobile = models.CharField(max_length=18, null=True, blank=True, verbose_name="شماره همراه")
    telephone = models.CharField(max_length=18, null=True, blank=True, verbose_name="شماره ثابت")
    province = models.CharField(max_length=18, null=True, blank=True, verbose_name="استان")
    city = models.CharField(max_length=18, null=True, blank=True, verbose_name="شهر")
    address = models.TextField(null=True, blank=True, verbose_name="آدرس")
    is_active = models.BooleanField(default=True, verbose_name="آیا کاربر فعال باشد؟")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    class Meta:
        db_table = "customers"
        verbose_name="مشتری"
        verbose_name_plural="مشتریان"


    def __str__(self):
        return self.firstName + " " + self.lastName
