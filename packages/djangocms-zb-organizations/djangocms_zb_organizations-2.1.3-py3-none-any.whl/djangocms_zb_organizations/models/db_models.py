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
# Date:         5/05/22 8:53 AM
# Project:      djangoPlugin
# Module Name:  models
# ****************************************************************
from cms.models.pluginmodel import CMSPlugin
from cities_light.models import Country
from cities_light.models import Region
from cities_light.models import SubRegion
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField
from djangocms_zb_organizations.lib.choices import Choices
from ckeditor.fields import RichTextField

from djangocms_zb_organizations.lib import managers


class Category(models.Model):
    """
    Modelo que representa la entidad Category, contiene las diferentes categorías y subcategorías
     en las que se clasifican las organizaciones o empresas.
    """
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.PROTECT, related_name="parent_category",
                               verbose_name=_("Parent category"),
                               help_text=_("Parent category, if it is a subcategory."))
    name = models.CharField(null=False, blank=False, max_length=150, verbose_name=_("Category name"))
    is_enabled = models.BooleanField(default=True, verbose_name=_("Is enabled"),
                                     help_text=_("Indicates if the category is enabled."))

    class Meta:
        verbose_name_plural = _("Categories")

    def __str__(self):
        category_name = self.name
        if self.parent is not None:
            category_name = str(self.parent) + "/" + str(self.name)
        return category_name


class Organization(models.Model):
    """
    Modelo que representa la entidad Organization donde se almacena la info base de una empresa/organización
    """
    name = models.CharField(null=False, blank=False, max_length=150, unique=True, verbose_name=_("Name"),
                            help_text=_("Organization name"))
    initial = models.CharField(null=True, blank=True, max_length=20, verbose_name=_("acronym/initials"),
                               help_text=_("Organization acronym/initials"))
    address = models.CharField(null=True, blank=True, max_length=150, verbose_name=_("Address"),
                               help_text=_("Company/organization address."))
    country = models.ForeignKey(Country, null=False, blank=False, on_delete=models.PROTECT, verbose_name=_("Country"),
                                help_text=_("Country where the company/organization is located."))
    region = models.ForeignKey(Region, null=False, blank=False, on_delete=models.PROTECT, verbose_name=_("Región"),
                               help_text=_("Region or state where the company/organization is located."))
    subregion = models.ForeignKey(SubRegion, null=False, blank=False, on_delete=models.PROTECT,
                                  verbose_name=_("Sub Región"),
                                  help_text=_("City or sub region where the company/organization is located."))
    phone = models.CharField(null=True, blank=True, max_length=15, verbose_name=_("Phone number"),
                             help_text=_("Phone number of the organization/company."))
    email = models.EmailField(null=True, blank=True, max_length=50, verbose_name=_("Email"),
                              help_text=_("Primary company/organization email."))
    schedule = models.TextField(null=True, blank=True, max_length=200, verbose_name=_("Attention schedule"))
    keyword = models.TextField(null=True, blank=True, max_length=150, verbose_name=_("Keywords"), help_text=_(
        "Keywords separated by commas, no spaces. They will be taken into account for the search of the "
        "organization on the map."), db_collation="utf8_general_ci")
    category = models.ManyToManyField(Category, blank=False, related_name="organization_category",
                                      verbose_name=_("Categories"))
    logo = FilerImageField(null=True, blank=True, on_delete=models.PROTECT, related_name="logo_organization",
                           verbose_name=_("Logo"),
                           help_text=_("Organization logo"))
    facebook = models.URLField(null=True, blank=True, verbose_name="Facebook", help_text=_("Facebook Link"))
    instagram = models.URLField(null=True, blank=True, verbose_name="Instagram", help_text=_("Instagram Link"))
    twitter = models.URLField(null=True, blank=True, verbose_name="Twitter", help_text=_("Twitter Link"))
    youtube = models.URLField(null=True, blank=True, verbose_name="Youtube", help_text=_("Youtube Link"))
    latitude = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=7, verbose_name=_("Latitude"),
                                   help_text=_("Latitude in which the company/organization is located."))
    longitude = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=7,
                                    verbose_name=_("Longitude"),
                                    help_text=_("Longitude in which the company/organization is located."))
    is_enabled = models.BooleanField(default=True, verbose_name=_("Is enabled"),
                                     help_text=_("Indicates if the company/organization is enabled."))

    # Set default manager
    objects = managers.OrganizationManager()

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(name="organization_name", fields=("name",))
        ]
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")


class Contact(models.Model):
    """
    Modelo que representa la entidad Contact donde se almacena la info
    de los contactos de cada una de las organizaciones
    """
    organization = models.ForeignKey(Organization, null=False, blank=False, on_delete=models.CASCADE,
                                     related_name="contact_organization", verbose_name=_("Organization"))
    name = models.CharField(null=False, blank=False, max_length=150, verbose_name=_("Contact name"))
    phone = models.CharField(null=True, blank=True, max_length=15, verbose_name=_("Contact phone"))
    email = models.EmailField(null=True, blank=True, max_length=50, verbose_name=_("Contact email"))
    is_enabled = models.BooleanField(default=True, verbose_name=_("Is enabled"),
                                     help_text=_("Indicates if the contact/organization is enabled."))

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.name


class MicroSite(models.Model):
    """
    Modelo que representa la entidad Microsite, contenidos con los que
    se puede armar un micrositio para cada empresa u organización"
    """
    organization = models.OneToOneField(Organization, null=False, blank=False, on_delete=models.CASCADE,
                                        related_name="micro_site_organization", verbose_name=_("Organization"))
    slug = models.SlugField(unique="True", null=False, blank=False, max_length=50, verbose_name="Slug")
    abstract = RichTextField(null=True, blank=True, max_length=350, verbose_name=_("Microsite abstract"),
                             help_text=_("Summary to show on the microsite."))
    content = RichTextField(null=False, blank=False, verbose_name=_("Microsite content"),
                            help_text=_("Content (text) to be displayed on the microsite."))
    video = models.TextField(null=True, blank=True, max_length=350, verbose_name=_("Videos"), help_text=_(
        "Video URL separated by commas, no spaces. These videos will be displayed on the microsite."))
    is_enabled = models.BooleanField(default=True, verbose_name=_("Is enabled"),
                                     help_text=_("Indicates if the microsite is enabled."))

    class Meta:
        verbose_name = _("Microsite")
        verbose_name_plural = _("Microsites")

    def __str__(self):
        return self.organization.name


def set_slug(sender, instance, *args, **kwargs):
    if instance.id is None:
        instance.slug = slugify(instance.organization.name[0:50])


pre_save.connect(set_slug, sender=MicroSite)


class OrgPicture(models.Model):
    """
    Modelo que representa la entidad Picture donde se almacena las imágenes
    de cada organización para ser mostrada en los micrositios.
    """
    micro_site = models.ForeignKey(MicroSite, null=False, blank=False, on_delete=models.CASCADE,
                                   related_name="org_picture_micro_site", verbose_name=_("Microsite"))
    picture = FilerImageField(null=False, blank=False, on_delete=models.PROTECT, related_name="picture_organization",
                              verbose_name=_("Picture file"),
                              help_text=_("Represents the image file found in media (Filer)."))
    is_enabled = models.BooleanField(default=True, verbose_name=_("Is enabled"),
                                     help_text=_("Indicates if the picture/organization is enabled."))

    def __str__(self):
        return self.picture.name


class Catalog(models.Model):
    """
    Modelo que representa la entidad Catalog, información del catalogo
    para cada microsite"
    """
    micro_site = models.ForeignKey(MicroSite, null=False, blank=False, on_delete=models.CASCADE,
                                   related_name="catalog_micro_site", verbose_name=_("Microsite owner"),
                                   help_text=_("Microsite to which the catalog belongs."))
    name = models.CharField(null=False, blank=False, max_length=200, verbose_name=_("Product/Service name"),
                            help_text=_("Name of the product or service."))
    description = RichTextField(null=False, blank=False, verbose_name=_("Short description"),
                                help_text=_("Description of the product or service offered."))
    picture = FilerImageField(null=False, blank=False, on_delete=models.PROTECT, related_name="catalog_picture",
                              verbose_name=_("Catalog Picture"),
                              help_text=_("Represents the image file found in media (Filer)."))
    is_enabled = models.BooleanField(default=True, verbose_name=_("Is enabled"),
                                     help_text=_("Indicates if the product or service is enabled."))

    class Meta:
        verbose_name = _("Catalog")
        verbose_name_plural = _("Catalogs")

    def __str__(self):
        return self.name


class PluginConfig(CMSPlugin):
    """
    Modelo que representa la entidad requerida para la configuración del Plugin en Django CMS
    """
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name=_("Filter by category"),
                                 related_name="plugins_category")
    template = models.CharField(null=False, blank=False, max_length=100, choices=Choices.TEMPLATES_CHOICES,
                                default=Choices.TEMPLATES_CHOICES[0][0], verbose_name=_("Template dir"),
                                help_text=_("Directory that contains the templates that the plugin will use."))
