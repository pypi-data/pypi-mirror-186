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

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         5/05/22 11:06 AM
# Project:      djangoPlugin
# Module Name:  cms_plugins
# ****************************************************************
import os.path
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from django.db.models import Q

from djangocms_zb_organizations.models import PluginConfig, Organization, Category


@plugin_pool.register_plugin
class DjangocmsZbOrganizationsPlugin(CMSPluginBase):
    """
    Organizations manager plugin for Django CMS
    """
    name = _("Organizations Manager Plugin for Django CMS")
    module = "Zibanu"
    cache = False
    model = PluginConfig
    autocomplete_fields = ['category']

    def _get_render_template(self, context, instance, placeholder):
        """
        Private method to replace default template in CMS
        :param context: Context CMS Var
        :param instance: Model instance
        :param placeholder: Placeholder
        :return: str: Name of new template
        """
        base_dir = f"djangocms_zb_organizations/default/"
        base_template = "organizations_map.html"
        if instance.template:
            base_dir = f"djangocms_zb_organizations/{instance.template}/"

        return os.path.join(base_dir, base_template)

    def get_render_template(self, context, instance, placeholder):
        return self._get_render_template(context, instance, placeholder)

    def render(self, context, instance, placeholder):
        """
        Override method to render template
        :param context: Context CMS Var
        :param instance: Model instance
        :param placeholder: Placeholder
        :return: context
        """
        request = context['request']
        # Se realiza la busqueda de las organizaciones hasta 3 niveles que el parent de su categoría sea igual a la
        # categoría seleccionada
        organizations = Organization.objects.filter(
            Q(category=instance.category) | Q(category__parent=instance.category) | Q(
                category__parent__parent=instance.category) | Q(category__parent__parent__parent=instance.category) | Q(
                category__parent__parent__parent__parent=instance.category), is_enabled=True).distinct()

        # Se obtienen las subcategorias hasta 3 niveles de la categoria seleccionada
        subcategories = Category.objects.filter(
            Q(parent=instance.category) | Q(parent__parent=instance.category) | Q(
                parent__parent__parent=instance.category) | Q(parent__parent__parent__parent=instance.category),
            is_enabled=True)

        def conditional_category_filter(select):
            if select != "category":
                return Q(category=instance.category)
            else:
                return Q()

        def conditional_filter(select):
            filt = select + "__icontains"
            if select == "category" or select == "subregion":
                filt = select + "__name__icontains"
            elif select == "service":
                filt = "micro_site_organization__catalog_micro_site__name__icontains"
            return filt

        def conditional_search(select, category, value):
            if select != "category":
                return value
            else:
                return category

        # Se valida si existe el metodo POST y sus campos y se almacenan en variables
        if request.method == 'POST' and (request.POST.get(
                'select-search') or request.POST.get('s-category') or request.POST.get('input-search')):
            select_search = request.POST.get('select-search')
            s_category = request.POST.get('s-category')
            input_search = request.POST.get('input-search')

            # Se realiza la validación y la busqueda de acuerdo al campo seleccionado
            if select_search == "keyword":
                organizations = Organization.objects.filter(id=0)
                for word in input_search.split(','):
                    organization = Organization.objects.filter(
                        conditional_category_filter(select_search) | Q(category__parent=instance.category) | Q(
                            category__parent__parent=instance.category) | Q(
                            category__parent__parent__parent=instance.category) | Q(
                            category__parent__parent__parent__parent=instance.category), keyword__icontains=word,
                        is_enabled=True)
                    organizations = organizations.union(organization)
            else:
                organizations = Organization.objects.filter(
                    conditional_category_filter(select_search) | Q(category__parent=instance.category) | Q(
                        category__parent__parent=instance.category) | Q(
                        category__parent__parent__parent=instance.category) | Q(
                        category__parent__parent__parent__parent=instance.category),
                    **{conditional_filter(select_search): conditional_search(select_search, s_category, input_search)},
                    is_enabled=True)

        org_js = []
        for organization in organizations:
            if organization.latitude is not None and organization.longitude is not None:
                if organization.address is None:
                    organization.address = "Dirección no registrada"
                org_js.append([
                    organization.id,
                    organization.name,
                    organization.address,
                    float(organization.latitude),
                    float(organization.longitude),
                ])

        context.update({
            "organizations": organizations,
            "subcategories": subcategories,
            "org_js": org_js,
        })

        context = super().render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class DjangocmsZbOrganizationsCarouselLogoPlugin(CMSPluginBase):
    """
    Organizations Logo Carousel Admin Plugin for Django CMS
    """
    name = _("Organizations Logo Carousel Admin Plugin for Django CMS")
    module = "Zibanu"
    cache = False
    model = PluginConfig
    autocomplete_fields = ['category']

    def _get_render_template(self, context, instance, placeholder):
        """
        Private method to replace default template in CMS
        :param context: Context CMS Var
        :param instance: Model instance
        :param placeholder: Placeholder
        :return: str: Name of new template
        """
        base_dir = f"djangocms_zb_organizations/default/"
        base_template = "organizations_carousel_logo.html"
        if instance.template:
            base_dir = f"djangocms_zb_organizations/{instance.template}/"

        return os.path.join(base_dir, base_template)

    def get_render_template(self, context, instance, placeholder):
        return self._get_render_template(context, instance, placeholder)

    def render(self, context, instance, placeholder):
        """
        Override method to render template
        :param context: Context CMS Var
        :param instance: Model instance
        :param placeholder: Placeholder
        :return: context
        """
        # Se realiza la busqueda de las organizaciones hasta 3 niveles que el parent de su categoría sea igual a la
        # categoría seleccionada
        organizations = Organization.objects.filter(Q(category=instance.category) | Q(
            category__parent=instance.category) | Q(category__parent__parent=instance.category) | Q(
            category__parent__parent__parent=instance.category), is_enabled=True, logo__isnull=False).distinct()

        context = super().render(context, instance, placeholder)

        context.update({
            "organizations": organizations,
        })
        return context
