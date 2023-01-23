# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-1-22 21:31                                                   =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : views.py                                                          =
#    @Program: backend                                                         =
# ==============================================================================

from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from hutao.models import Album, Info, Letter, Voices
from hutao.serializers import (
    AlbumCreateSerializer, AlbumDetailSerializer, AlbumImageUploadSerializer, AlbumSerializer, InfoSerializer,
    LetterDetailSerializer,
    LettersSerializer,
    VoicesSerializer,
)
from images.models import Image
from tokenAuth.permissions import TokenAuth


class InfoViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = InfoSerializer
    queryset = Info.objects.all()
    permission_classes = [AllowAny]
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == "letters":
            return LettersSerializer
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


class AlbumPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 20


class AlbumViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = AlbumDetailSerializer
    queryset = Album.objects.all()
    permission_classes = [AllowAny]
    lookup_field = "id"
    pagination_class = AlbumPagination

    def get_serializer_class(self):
        if self.action == "list":
            return AlbumSerializer
        elif self.action == "create":
            return AlbumCreateSerializer
        elif self.action == "upload":
            return AlbumImageUploadSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ["create", "upload"]:
            self.permission_classes = [TokenAuth]
        return super().get_permissions()

    @action(methods=['post'], detail=True)
    def upload(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        obj = self.get_object()
        for image in data["images"]:
            obj.images.add(Image.objects.create(image=image))
        obj.save()
        return Response(data={"total": obj.images.count()})


class AlbumImagePagination(PageNumberPagination):
    # 默认的大小
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 100


class AlbumImageViewSet(GenericViewSet):
    # serializer_class = ImageSerializer
    queryset = Image.objects.all()
    permission_classes = [AllowAny]
    lookup_field = "id"
    pagination_class = AlbumImagePagination

    def get_album(self) -> Album:
        return Album.objects.get(id=self.kwargs["album_id"])

    def get_queryset(self):
        return self.get_album().images.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        # serializer = ListSerializer(instance=page, child=ImageField(use_url=, source="image"))
        data = []
        for image in page:
            data.append(request.build_absolute_uri(image.image.url))
        return self.get_paginated_response(data)
