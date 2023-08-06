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
# Date: 1/06/2022 5:17 p. m.
# Project: Djangocms-pruebas
# Module Name: views
# ****************************************************************

from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_object_or_404

from .models import MicroSite


def micro_site(request, slug):
    base_dir = f"djangocms_zb_organizations/"
    base_template = "micro_site.html"

    micro_site = get_object_or_404(MicroSite, slug=slug, is_enabled=True)
    videos = []
    if micro_site.video:
        for video in micro_site.video.split(","):
            id_video = video.split("/")
            videos.append("https://www.youtube.com/embed/" + id_video[-1])
    pictures = micro_site.org_picture_micro_site.filter(is_enabled=True)
    catalogs = micro_site.catalog_micro_site.filter(is_enabled=True)
    disclaimer = getattr(
        settings,
        'DJANGOCMS_ZB_ORGANIZATIONS_MS_DISCLAIMER',
        "",
    )
    return render(request, f'{base_dir}{base_template}',
                  {'micro_site': micro_site, 'pictures': pictures, 'catalogs': catalogs, 'videos': videos,
                   'disclaimer': disclaimer})
