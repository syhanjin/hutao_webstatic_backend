# -*- coding: utf-8 -*-

# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-1-24 21:1                                                    =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : serializers.py                                                    =
#    @Program: backend                                                         =
# ==============================================================================
from rest_framework import serializers

from hutao.models import Album, BasicInfoItem, ExtraInfoItem, Info, Letter, VoiceLang, VoiceLangItem, Voices
from images.serializers import ImageSerializer


class BasicInfoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicInfoItem
        fields = ("name", "value")


class ExtraInfoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfoItem
        fields = ("name", "value")


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = Info.PUBLIC_FIELDS

    basic_info = BasicInfoItemSerializer(many=True)
    extra_info = ExtraInfoItemSerializer(many=True)
    image = ImageSerializer()


class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = ("title", "sent", "id")


class LetterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = ("title", "sent", "content", "audio")


class LettersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ["letters"]

    letters = LetterSerializer(many=True)


class VoiceLangItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceLangItem
        fields = ("label", "content", "src")


class VoiceLangSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceLang
        fields = ("name", "type", "items")

    items = VoiceLangItemSerializer(many=True)


class VoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voices
        fields = ['langs']

    langs = VoiceLangSerializer(many=True)


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = Album.SUMMARY_FIELDS

    cover = serializers.ImageField(use_url=True, source="cover.image")


class AlbumDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = Album.PUBLIC_FIELDS

    cover = serializers.ImageField(use_url=True, source="cover.image")
    # images = serializers.ListSerializer(child=serializers.ImageField(use_url=True, source="image"))


class AlbumCreateSerializer(serializers.ModelSerializer):
    token = serializers.UUIDField(read_only=True)
    cover = serializers.ImageField()
    id = serializers.UUIDField(required=False)

    class Meta:
        model = Album
        fields = Album.REQUIRED_FIELDS + ["token", "id"]


class AlbumImageUploadSerializer(serializers.Serializer):
    images = serializers.ListField(child=serializers.ImageField(), min_length=1)
    token = serializers.UUIDField(read_only=True)


class AlbumImageDeleteSerializer(serializers.Serializer):
    images = serializers.ListField(child=serializers.UUIDField(), min_length=1)
    token = serializers.UUIDField(read_only=True)


class AlbumSetCoverSerializer(serializers.Serializer):
    cover = serializers.ImageField()
    token = serializers.UUIDField(read_only=True)
