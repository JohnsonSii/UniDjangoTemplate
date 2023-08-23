from django.db import models

# Create your models here.

import uuid


class User(models.Model):

    # 唯一主键
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # 用户名密码
    username = models.CharField(max_length=32, null=True)
    password = models.CharField(max_length=32, null=True)

    # 用户权限
    role = models.IntegerField(null=True)

    # 创建与更新日期
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
