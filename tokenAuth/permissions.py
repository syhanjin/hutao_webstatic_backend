# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-1-22 16:5                                                    =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : permissions.py                                                    =
#    @Program: backend                                                         =
# ==============================================================================

# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission

from tokenAuth.models import Token


class TokenAuth(BasePermission):
    def has_permission(self, request, view):
        token = request.data.get("token")
        return token and Token.objects.filter(token=token).exists()
