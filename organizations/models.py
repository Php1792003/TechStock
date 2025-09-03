from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    def __str__(self): return self.name

class Location(models.Model):
    class LocationType(models.TextChoices):
        WAREHOUSE = 'WAREHOUSE', 'Kho'
        DEPARTMENT = 'DEPARTMENT', 'Phòng ban'
        VENDOR_REPAIR = 'VENDOR_REPAIR', 'Nhà cung cấp sửa chữa'
        DISPOSAL = 'DISPOSAL', 'Nơi thanh lý'
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=LocationType.choices)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self): return f"{self.get_type_display()}: {self.name}"

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    emp_code = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15, blank=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='employees')
    is_active = models.BooleanField(default=True)
    def __str__(self): return self.user.get_full_name() or self.user.username