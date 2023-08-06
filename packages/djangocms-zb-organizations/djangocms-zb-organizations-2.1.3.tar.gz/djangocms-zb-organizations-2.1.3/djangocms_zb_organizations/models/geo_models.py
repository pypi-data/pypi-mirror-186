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
# Date: 5/10/2022 2:07 p. m.
# Project: Djangocms-pruebas
# Module Name: geo_models
# ****************************************************************

from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

from djangocms_zb_organizations.models import Organization


class GeoOrganization(models.Model):
    organization = models.OneToOneField(Organization, null=False, blank=False, on_delete=models.CASCADE,
                                        related_name="geo_organization", related_query_name="organization",
                                        verbose_name=_("Organization"))
    polygon = models.MultiPolygonField(null=True, blank=True, verbose_name=_('Polygons'),
                                       help_text=_('Location Area Coordinates'))
