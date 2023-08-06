# -*- coding: utf-8 -*-

#  Copyright (C)  2022. CQ Inversiones SAS.
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
# Date: 3/12/2022 8:49 a. m.
# Project: Djangocms-pruebas
# Module Name: organization
# ****************************************************************

from django.db import models
from django.db.models import Q

from djangocms_zb_organizations import models as zb_org_models


class OrganizationManager(models.Manager):
    """
    Manager for entity Organization
    """

    def get_queryset(self) -> models.QuerySet:
        """
        Method to return a queryset
        :return: queryset
        """
        return super().get_queryset()

    def get_organizations_by_category(self, category: int = 0) -> models.QuerySet:
        """
        Method to get organizations for specific category
        :param category: int: category_id, queryset categories
        :return: int: number of organizations.
        """
        queryset = self.get_queryset().all()
        if category > 0:
            queryset = queryset.filter(category=category, is_enabled=True)
            categories = zb_org_models.Category.objects.filter(
                Q(parent=category) | Q(parent__parent=category) | Q(parent__parent__parent=category) | Q(
                    parent__parent__parent__parent=category))
            for category in categories:
                organization = self.get_queryset().filter(category=category, is_enabled=True)
                queryset = queryset.union(organization)
        return queryset

    def get_count_by_category(self, category: int = 0) -> int:
        """
        Method to get organizations count for specific category
        :param category: int: category
        :return: int: number of organizations.
        """
        return self.get_organizations_by_category(category=category).count()
