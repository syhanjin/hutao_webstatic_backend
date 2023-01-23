# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-1-22 19:29                                                   =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : models.py                                                         =
#    @Program: backend                                                         =
# ==============================================================================
import uuid

from django.db import models


class ImageManager(models.Manager):
    def create(self, *args, **kwargs):
        _id = uuid.uuid4()
        image = kwargs["image"]
        image.name = f"{_id.hex}.jpg"
        return super(ImageManager, self).create(id=_id, image=image)

    pass


class Image(models.Model):
    class Meta:
        ordering = ['created']

    image = models.ImageField(upload_to="images")
    id = models.UUIDField(verbose_name="编号", primary_key=True, default=uuid.uuid4, editable=False, max_length=64)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    objects = ImageManager()

    def __unicode__(self):
        return str(self.created)

    @property
    def url(self):
        return self.image.url
