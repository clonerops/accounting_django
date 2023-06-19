from django.db import models
from account.models import User
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name="product_createdby", verbose_name="ایجاد شده توسط")
    isActive = models.BooleanField(default=True, verbose_name="آیا محصول فعال باشد؟")
    isStock = models.BooleanField(default=True, verbose_name="آیا محصول موجود می باشد؟")
    isDeleted = models.BooleanField(default=False, verbose_name="آیا محصول در لیست حذف شده ها باشد؟")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    class Meta: 
        db_table = "products"
        verbose_name="محصول"
        verbose_name_plural="محصولات"

    def __str__(self) -> str:
        return self.title

