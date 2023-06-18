from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, nationalCode, firstName, lastName, mobile, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not nationalCode:
            raise ValueError("Users must have an email address")

        user = self.model(
            nationalCode=nationalCode,
            firstName=firstName,
            lastName=lastName,
            mobile=mobile
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nationalCode, firstName, lastName, mobile, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            nationalCode,
            firstName=firstName,
            lastName=lastName,
            mobile=mobile,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    firstName = models.CharField(max_length=255, null=True, blank=True, verbose_name="نام")
    lastName = models.CharField(max_length=255, null=True, blank=True, verbose_name="نام خانوادگی")
    fatherName = models.CharField(max_length=255, null=True, blank=True, verbose_name="نام پدر")
    nationalCode = models.CharField(max_length=10, unique=True, verbose_name="کدملی")
    birthDate = models.DateField(null=True, blank=True)
    mobile = models.CharField(max_length=18, null=True, blank=True, verbose_name="شماره همراه")
    telephone = models.CharField(max_length=18, null=True, blank=True, verbose_name="شماره ثابت")
    province = models.CharField(max_length=18, null=True, blank=True, verbose_name="استان")
    city = models.CharField(max_length=18, null=True, blank=True, verbose_name="شهر")
    address = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "nationalCode"
    REQUIRED_FIELDS = ["firstName", "lastName", "mobile"]

    def __str__(self):
        return self.nationalCode

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
