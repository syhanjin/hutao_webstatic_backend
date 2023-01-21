# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-1-21 19:36                                                   =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : models.py                                                         =
#    @Program: backend                                                         =
# ==============================================================================
import uuid

from django.db import models

from images.models import Image


class Info(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=64)
    name = models.CharField(max_length=128, default="")
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    voices = models.ForeignKey('Voices', on_delete=models.SET_NULL, null=True)


class BasicInfoItem(models.Model):
    class Meta:
        ordering = ['priority']

    owner = models.ForeignKey(Info, related_name="basic_info", on_delete=models.CASCADE)
    priority = models.PositiveIntegerField(default=10000)
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=256)


class ExtraInfoItem(models.Model):
    class Meta:
        ordering = ["priority"]

    owner = models.ForeignKey(Info, related_name="extra_info", on_delete=models.CASCADE)
    priority = models.PositiveIntegerField(default=10000)
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=1024)


class Voices(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=64)


class VoiceLang(models.Model):
    owner = models.ForeignKey(Voices, related_name="langs", on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    type = models.CharField(max_length=32)


class VoiceLangItem(models.Model):
    owner = models.ForeignKey(VoiceLang, related_name="items", on_delete=models.CASCADE)
    label = models.CharField(max_length=256)
    content = models.CharField(max_length=1024)
    src = models.URLField()


class Letter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=64)
    owner = models.ForeignKey(Info, related_name="letters", on_delete=models.CASCADE)
    sent = models.DateField()
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=2048)
    audio = models.FileField(null=True, default=None)

