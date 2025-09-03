from django.db import models
from organizations.models import Department, Employee, Location

class ComputerModel(models.Model):
    brand = models.CharField(max_length=50)
    model_name = models.CharField(max_length=100)
    def __str__(self): return f"{self.brand} {self.model_name}"

class Computer(models.Model):
    class Status(models.TextChoices):
        IN_STOCK = 'IN_STOCK', 'Trong kho'
        ASSIGNED = 'ASSIGNED', 'Đã cấp phát'
        REPAIR = 'REPAIR', 'Đang sửa chữa'
        DISPOSED = 'DISPOSED', 'Đã thanh lý'

    asset_tag = models.CharField(max_length=50, unique=True)
    serial = models.CharField(max_length=100, unique=True)
    computer_model = models.ForeignKey(ComputerModel, on_delete=models.PROTECT, related_name='computers')
    purchase_date = models.DateField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.IN_STOCK)
    current_location = models.ForeignKey(Location, on_delete=models.PROTECT)
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='computers')
    assigned_department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self): return f"{self.computer_model} ({self.asset_tag})"