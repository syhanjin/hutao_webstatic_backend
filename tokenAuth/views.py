# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-1-29 18:21                                                   =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : views.py                                                          =
#    @Program: backend                                                         =
# ==============================================================================

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from tokenAuth.models import Token
from tokenAuth.permissions import TokenAuth


class TokenViewSet(viewsets.GenericViewSet):
    queryset = Token.objects.all()
    permission_classes = [TokenAuth]
    lookup_field = "token"

    @action(methods=["post"], detail=False)
    def auth(self, request, *args, **kwargs):
        return Response(data={"token": request.data["token"]})
