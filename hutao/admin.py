# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-1-21 20:3                                                    =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : admin.py                                                          =
#    @Program: backend                                                         =
# ==============================================================================

# Register your models here.
import json
import os.path
from datetime import datetime

from hutao.models import BasicInfoItem, ExtraInfoItem, Info, Letter, VoiceLang, VoiceLangItem, Voices
from images.models import Image

ID = "e686fef2-d216-4834-9386-7f6567233daa"
LETTERS = [
    {
        "sent": datetime(2021, 7, 15).date(),
        "title": "本堂主挚友亲启。",
        "content": """
好友，本堂主有一喜讯，专程通知：今天是本堂主生辰吉日，早晨起床只觉诗兴大发，特此赋诗一首，邀你共赏。

胡家奇女初问世，宏天云展生万象。
火蝶振翅若梅瓣，夜尽晓梦隐留香。
风起，云动，往生无常。
花开，岩寂，诸事清朗。

又及，本堂主近日途经无妄坡数趟，路遇岩壁生花，此等盎然生机，不折风骨，正如好友你一般使我高兴。
据说这些清雅可人的小花与椰奶一同饮用，有利口开胃之功效。我已试过，望你速尝。
有空常来堂里坐！堂主想你！
""".strip()
    },
    {
        "sent": datetime(2022, 7, 15).date(),
        "title": "挚友挚友看这里！",
        "content": """
近日本堂主对钓鱼一事兴趣陡升，但不知为何坐镇池边数日都丝毫不见鱼儿上钩，想来是缺少帮手所致。
要说钓鱼，自然需要挚友你喽！你天南海北四处垂钓，是高手中的高手，不如过来帮我看看，是这里的鱼儿肚子吃得太饱，还是饵不对胃口？另外，虽然钓鱼失败，但本堂主一个猛子扎进水里亲手捞了几条美味的鱼！滑溜鱼片佐阳春面，鲜香搭配，动静相宜。此般美味，可不能我一人独享呀。
天上一只鸟，地上一粒米，
你和堂主在一起，每天笑嘻嘻。
速来！就在这儿等你！
""".strip()
    }
]


def load_hutao_info(voices_json_path):
    if not os.path.exists(voices_json_path):
        raise ValueError()
    voices_json = json.load(open(voices_json_path, "r", encoding="utf-8"))
    info = Info.objects.create(name="胡桃")
    basic_info_item = [
        BasicInfoItem.objects.create(owner=info, name="姓名", value="胡桃", priority=1000),
        BasicInfoItem.objects.create(owner=info, name="命座", value="蝶之座", priority=2000),
        BasicInfoItem.objects.create(owner=info, name="武器", value="长柄武器", priority=3000),
        BasicInfoItem.objects.create(owner=info, name="称号", value="雪霁梅香", priority=4000),
        BasicInfoItem.objects.create(owner=info, name="职位", value="往生堂第七十七代堂主", priority=5000),
    ]
    image = Image.objects.create()
    image.image = "images/001.jpg"
    info.image = image
    voices = Voices.objects.create()
    langs = [
        {"type": "chinese", "name": "汉语"},
        {"type": "japanese", "name": "日语"},
        {"type": "korean", "name": "韩语"},
        {"type": "english", "name": "英语"},
    ]
    for lang in langs:
        voice_lang = VoiceLang.objects.create(owner=voices, **lang)
        for voice in voices_json.get(lang["type"]):
            VoiceLangItem.objects.create(owner=voice_lang, **voice)
    info.voices = voices
    info.save()


def load_letters():
    info = Info.objects.get(id=ID)
    for letter in LETTERS:
        Letter.objects.create(owner=info, **letter)


def load_info(info_json_path):
    if not os.path.exists(info_json_path):
        raise ValueError()
    info_json = json.load(open(info_json_path, "r", encoding="utf-8"))
    info = Info.objects.get(id=ID)
    for item in info_json["data"]:
        ExtraInfoItem.objects.create(
            owner=info,
            name=item["label"],
            value=item["content"]
        )
