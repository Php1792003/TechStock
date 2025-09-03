from django.db import models
from django.contrib.auth.models import User
from assets.models import Computer
from organizations.models import Department, Employee, Location
from datetime import datetime


class InventoryTxn(models.Model):
    class TxnType(models.TextChoices):
        ISSUE = 'ISSUE', 'Xuất cấp phát'
        RETURN = 'RETURN', 'Thu hồi/Trả về'

    code = models.CharField(max_length=30, unique=True, blank=True)
    type = models.CharField(max_length=20, choices=TxnType.choices)
    source_location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='source_txns', null=True,
                                        blank=True)
    dest_location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='dest_txns', null=True,
                                      blank=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_txns')
    received_by = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='received_txns', null=True,
                                    blank=True)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.code


class InventoryTxnLine(models.Model):
    inventory_txn = models.ForeignKey(InventoryTxn, on_delete=models.CASCADE, related_name='lines')
    computer = models.ForeignKey(Computer, on_delete=models.PROTECT)