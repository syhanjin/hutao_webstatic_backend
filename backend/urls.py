# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-1-21 14:0                                                    =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : urls.py                                                           =
#    @Program: backend                                                         =
# ==============================================================================
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers

import hutao.views

router = routers.DefaultRouter()
router.register(r'info', hutao.views.InfoViewSet)
router.register(r'voices', hutao.views.VoicesViewSet)
router.register(r'letter', hutao.views.LettersViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
]

urlpatterns = [
    path(settings.BASE_URL, include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
