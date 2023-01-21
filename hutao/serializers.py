# -*- coding: utf-8 -*-

# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-1-21 19:49                                                   =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : serializers.py                                                    =
#    @Program: backend                                                         =
# ==============================================================================
from rest_framework import serializers

from hutao.models import BasicInfoItem, ExtraInfoItem, Info, Letter, VoiceLang, VoiceLangItem, Voices
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
        fields = ("name", "basic_info", "extra_info", "image", "voices")

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
