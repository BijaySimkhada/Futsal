from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must enter email")
        if not username:
            raise ValueError("User must enter username")

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):     #overridding
    email = models.EmailField(verbose_name="E-mail", max_length=60, unique="True")
    username = models.CharField(max_length=30, unique=True)
    acc_type = models.CharField(max_length=20)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class UserInfo(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)
    phone = models.CharField(max_length=10, null=False)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)

    def __str__(self):
        return self.first_name


class FutsalInfo(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)
    phone = models.CharField(max_length=10, null=False)
    futsal_name = models.CharField(max_length=30, null=False)
    location = models.CharField(max_length=40, null=False)
    price = models.FloatField(null=False)
    open_at = models.CharField(max_length=40, null=False)
    close_at = models.CharField(max_length=40, null=False)

    def __str__(self):
        return self.futsal_name
