# ==============================================================================
#  Copyright (C) 2023 Sakuyark, Inc. All Rights Reserved                       =
#                                                                              =
#    @Time : 2023-1-22 20:11                                                   =
#    @Author : hanjin                                                          =
#    @Email : 2819469337@qq.com                                                =
#    @File : urls.py                                                           =
#    @Program: backend                                                         =
# ==============================================================================
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework_nested import routers

import hutao.views

router = routers.DefaultRouter()
router.register(r'info', hutao.views.InfoViewSet)
router.register(r'voices', hutao.views.VoicesViewSet)
router.register(r'letter', hutao.views.LettersViewSet)
router.register(r'album', hutao.views.AlbumViewSet)
album_router = routers.NestedSimpleRouter(router, r"album", lookup="album")
album_router.register(r"image", hutao.views.AlbumImageViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
]

urlpatterns = [
    path(settings.BASE_URL, include(router.urls)),
    path(settings.BASE_URL, include(album_router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
