# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-1-22 15:53                                                   =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : apps.py                                                           =
#    @Program: backend                                                         =
# ==============================================================================

from django.apps import AppConfig


class TokenAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tokenAuth'
