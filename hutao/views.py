# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-1-21 17:22                                                   =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : views.py                                                          =
#    @Program: backend                                                         =
# ==============================================================================
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from hutao.models import Info, Letter, Voices
from hutao.serializers import InfoSerializer, LetterDetailSerializer, LettersSerializer, VoicesSerializer


class InfoViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = InfoSerializer
    queryset = Info.objects.all()
    permission_classes = [AllowAny]
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == "letters":
            self.serializer_class = LettersSerializer
        return super().get_serializer_class()

    @action(methods=['get'], detail=True)
    def letters(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        return Response(data=serializer.data["letters"])


class VoicesViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = VoicesSerializer
    queryset = Voices.objects.all()
    permission_classes = [AllowAny]
    lookup_field = 'id'


class LettersViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = LetterDetailSerializer
    queryset = Letter.objects.all()
    permission_classes = [AllowAny]
    lookup_field = "id"
