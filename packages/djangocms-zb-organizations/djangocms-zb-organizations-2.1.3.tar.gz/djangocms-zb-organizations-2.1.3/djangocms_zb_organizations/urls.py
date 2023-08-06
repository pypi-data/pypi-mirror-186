# -*- coding: utf-8 -*-

#      Copyright (C)  2022. CQ Inversiones SAS.
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

# ****************************************************************
# IDE: PyCharm
# Developed by: JhonyAlexanderGonzal
# Date: 1/06/2022 5:32 p. m.
# Project: Djangocms-pruebas
# Module Name: urls
# ****************************************************************

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import micro_site
from djangocms_zb_organizations.lib.services import OrganizationService

urlpatterns = [
    path(r"counter/by-category/",
         OrganizationService.as_view({"post": 'count_by_category'})),
    path(r"get-geo-json/",
         OrganizationService.as_view({"post": 'get_geo_json'})),
    path(r"by-category/", OrganizationService.as_view({"post": 'by_category'})),
    path('<slug:slug>/', micro_site, name='micro_site'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
