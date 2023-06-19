from django.db import models
from account.models import User
from product.models import Product
# Create your models here.

TypeChoise = (
    ("1", "عمومی"),
    ("2", "واسط"),
)
class Store(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    type = models.CharField(
        max_length=255,
        choices= TypeChoise,
        default="1"
    )
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name="store_createdby", verbose_name="ایجاد شده توسط")
    isActive = models.BooleanField(default=True, verbose_name="آیا انبار فعال باشد؟")
    isDeleted = models.BooleanField(default=False, verbose_name="آیا انبار در لیست حذف شده ها باشد؟")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    class Meta: 
        db_table = "stores"
        verbose_name="انبار"
        verbose_name_plural="انبارها"


    def __str__(self) -> str:
        return self.title


class ProductStore(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="productId", verbose_name="شناسه محصول")
    storeId = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="storeId", verbose_name="شناسه انبار")
    floorInventory = models.IntegerField(verbose_name="موجودی کف")
    actualInventory = models.IntegerField(verbose_name="موجودی قابل سفارش")
    isActive = models.BooleanField(default=True, verbose_name="آیا فعال باشد")
    isDeleted = models.BooleanField(default=False, verbose_name="آیا در لیست حذف شده ها باشد؟")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    class Meta: 
        db_table = "productstore"
        verbose_name="مدیریت انبار-محصول"
        verbose_name_plural="مدیریت انبارها-محصول ها"

