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
# Date: 10/05/2022 10:52 a. m.
# Project: Djangocms-pruebas
# Module Name: admin
# ****************************************************************
import json
import os
import tempfile
import uuid
import geopandas as gpd
from django import forms
from django.conf import settings
from django.contrib import admin, messages
from django.contrib.gis.admin.widgets import OpenLayersWidget
from django.contrib.gis.gdal import OGRGeomType
from django.contrib.gis.db import models
from django.core.validators import FileExtensionValidator
from django.db import transaction
from django.forms import Media
from django.utils.translation import gettext_lazy as _

# Import models
from .models import Category, Organization, Contact, OrgPicture, MicroSite, Catalog, GeoOrganization


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "parent":
            kwargs["queryset"] = Category.objects.filter(is_enabled=True)
        return super(CategoryAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ["name", "parent", "is_enabled"]
    search_fields = ["name"]
    autocomplete_fields = ['parent']


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1


class GeoAdminMixin:
    """
    Copied over from django.contrib.gis.admin.GeoModelAdmin

    The administration options class for Geographic models. Map settings
    may be overloaded from their defaults to create custom maps.
    """

    # The default map settings that may be overloaded -- still subject
    # to API changes.
    default_lon = -75.2936958
    default_lat = 2.9262767
    default_zoom = 8
    display_wkt = False
    display_srid = False
    extra_js = []
    num_zoom = 18
    max_zoom = False
    min_zoom = False
    units = False
    max_resolution = False
    max_extent = False
    modifiable = True
    mouse_position = True
    scale_text = True
    layerswitcher = True
    scrollable = True
    map_width = 600
    map_height = 400
    map_srid = 4326
    map_template = 'gis/admin/openlayers.html'
    openlayers_url = 'https://cdnjs.cloudflare.com/ajax/libs/openlayers/2.13.1/OpenLayers.js'
    point_zoom = num_zoom - 6
    wms_url = 'http://vmap0.tiles.osgeo.org/wms/vmap0'
    wms_layer = 'basic'
    wms_name = 'OpenLayers WMS'
    wms_options = {'format': 'image/jpeg'}
    debug = False
    widget = OpenLayersWidget

    @property
    def media(self):
        """Injects OpenLayers JavaScript into the admin."""
        return super().media + Media(js=[self.openlayers_url] + self.extra_js)

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        """
        Overloaded from ModelAdmin so that an OpenLayersWidget is used
        for viewing/editing 2D GeometryFields (OpenLayers 2 does not support
        3D editing).
        """
        if isinstance(db_field, models.GeometryField) and db_field.dim < 3:
            # Setting the widget with the newly defined widget.
            kwargs['widget'] = self.get_map_widget(db_field)
            return db_field.formfield(**kwargs)
        else:
            return super().formfield_for_dbfield(db_field, request, **kwargs)

    def get_map_widget(self, db_field):
        """
        Return a subclass of the OpenLayersWidget (or whatever was specified
        in the `widget` attribute) using the settings from the attributes set
        in this class.
        """
        is_collection = db_field.geom_type in (
            'MULTIPOINT',
            'MULTILINESTRING',
            'MULTIPOLYGON',
            'GEOMETRYCOLLECTION',
        )
        if is_collection:
            if db_field.geom_type == 'GEOMETRYCOLLECTION':
                collection_type = 'Any'
            else:
                collection_type = OGRGeomType(db_field.geom_type.replace('MULTI', ''))
        else:
            collection_type = 'None'

        class OLMap(self.widget):
            template_name = self.map_template
            geom_type = db_field.geom_type

            wms_options = ''
            if self.wms_options:
                wms_options = ["%s: '%s'" % pair for pair in self.wms_options.items()]
                wms_options = ', %s' % ', '.join(wms_options)

            params = {
                'default_lon': self.default_lon,
                'default_lat': self.default_lat,
                'default_zoom': self.default_zoom,
                'display_wkt': self.debug or self.display_wkt,
                'geom_type': OGRGeomType(db_field.geom_type),
                'field_name': db_field.name,
                'is_collection': is_collection,
                'scrollable': self.scrollable,
                'layerswitcher': self.layerswitcher,
                'collection_type': collection_type,
                'is_generic': db_field.geom_type == 'GEOMETRY',
                'is_linestring': db_field.geom_type in ('LINESTRING', 'MULTILINESTRING'),
                'is_polygon': db_field.geom_type in ('POLYGON', 'MULTIPOLYGON'),
                'is_point': db_field.geom_type in ('POINT', 'MULTIPOINT'),
                'num_zoom': self.num_zoom,
                'max_zoom': self.max_zoom,
                'min_zoom': self.min_zoom,
                'units': self.units,  # likely should get from object
                'max_resolution': self.max_resolution,
                'max_extent': self.max_extent,
                'modifiable': self.modifiable,
                'mouse_position': self.mouse_position,
                'scale_text': self.scale_text,
                'map_width': self.map_width,
                'map_height': self.map_height,
                'point_zoom': self.point_zoom,
                'srid': self.map_srid,
                'display_srid': self.display_srid,
                'wms_url': self.wms_url,
                'wms_layer': self.wms_layer,
                'wms_name': self.wms_name,
                'wms_options': wms_options,
                'debug': self.debug,
            }

        return OLMap


class GeoOrgInline(GeoAdminMixin, admin.TabularInline):
    model = GeoOrganization


# Clase perzonalida para agregar un field en el form del admin de organizaciones
class ExtraField(forms.ModelForm):
    # Fiel para subida multiple de archivos
    file_field = forms.FileField(label=_("Polygon files"), widget=forms.ClearableFileInput(attrs={'multiple': True}),
                                 required=False,
                                 help_text=_("Upload .shp and .shx files for the polygons of the organization"),
                                 validators=[FileExtensionValidator(allowed_extensions=['shp', 'shx'])])


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone', 'country', 'region', 'subregion', 'is_enabled']
    inlines = (ContactInline, GeoOrgInline,)
    search_fields = ["name", 'address', 'phone', 'region__name', 'subregion__name']
    list_filter = ['is_enabled', 'category__parent']
    autocomplete_fields = ['country', 'region', 'subregion']
    form = ExtraField
    fieldsets = (
        (_("Main Options"), {
            'fields': (
                ('name', 'initial'), ('address', 'phone'), ('email', 'country'), ('region', 'subregion'),
                ('schedule', 'keyword'), 'logo', 'category'),
        }),
        (_('Location'), {
            'fields': (('latitude', 'longitude'),),
        }),
        (_('Social Networks'), {
            'classes': ('collapse',),
            'fields': (('facebook', 'instagram'), ('twitter', 'youtube'),),
        }),
        (None, {
            'fields': (('file_field',), 'is_enabled',),
        }),
    )

    # Metodo que filtra las categorias habilitadas a mostrar en el form del admin
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter(is_enabled=True)
        return super(OrganizationAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    # Metodo save que se interviene para configurar el funcionamiento al guardar los datos del form en la BD
    def save_model(self, request, obj, form, change):
        # Se llama el metodo padre para realizar el guardado.
        super().save_model(request, obj, form, change)
        # Validación para saber si existe el campo file agregado en el form
        if request.FILES and request.FILES["file_field"]:
            files = request.FILES.getlist('file_field')
            # Se valida que sean dos archivos
            if len(files) == 2:
                parts_file0 = files[0].name.split('.')
                ext_file0 = parts_file0.pop().lower()
                parts_file1 = files[1].name.split('.')
                ext_file1 = parts_file1.pop().lower()
                # Se valida que los archivos sean un .shp y un .shx
                if (ext_file0 == "shp" and ext_file1 == "shx") or (
                        ext_file0 == "shx" and ext_file1 == "shp"):
                    # Se crean y se guardan los archivos que hay en memoria a la carpeta temp del S.O.
                    name = uuid.uuid4().hex
                    name_file0 = name + "." + ext_file0
                    name_file1 = name + "." + ext_file1
                    DJANGOCMS_ZB_ORGANIZATIONS_TEMP_DIR = getattr(
                        settings,
                        'DJANGOCMS_ZB_ORGANIZATIONS_TEMP_DIR',
                        tempfile.gettempdir(),
                    )
                    if DJANGOCMS_ZB_ORGANIZATIONS_TEMP_DIR != "":
                        file_to_save0 = os.path.join(DJANGOCMS_ZB_ORGANIZATIONS_TEMP_DIR, name_file0)
                        file_to_save1 = os.path.join(DJANGOCMS_ZB_ORGANIZATIONS_TEMP_DIR, name_file1)
                        f0 = open(file_to_save0, "wb")
                        f0.write(files[0].read())
                        f0.close()
                        f1 = open(file_to_save1, "wb")
                        f1.write(files[1].read())
                        f1.close()
                        # Se lee uno de los archivos con geopandas
                        gdf = gpd.read_file(file_to_save0)
                        # Se convierte los Dataframes en formato Geojson
                        data = gdf.to_json()
                        # Se convierte la data en un Dict para procesarla
                        dict_data = json.loads(data)
                        coordinates = []
                        # Se recorre el dict y se agregan las coordenadas en una lista de coordenadas
                        for feature in dict_data["features"]:
                            coordinates.append(feature["geometry"]["coordinates"])
                        # se crea el dict de la data con el tipo de campo y las coordenadas
                        data = {"type": "Multipolygon", "coordinates": coordinates}
                        # Se convierte a un str para poder guardarla en el campo Multipolygon
                        str_data = json.dumps(data)
                        # Se guardan los datos en la tabla de GeoOrganization
                        try:
                            geo = GeoOrganization.objects.filter(organization=obj).first()
                            with transaction.atomic():
                                if geo is not None:
                                    geo.organization = obj
                                    geo.polygon = str_data
                                    geo.save()
                                else:
                                    GeoOrganization.objects.create(organization=obj, polygon=str_data)
                        except Exception:
                            messages.error(request,
                                           _("The polygons were not processed, because the coordinates are in a "
                                             "different format or there was a problem processing the data."))
                        finally:
                            # Se eliminan los archivos del directorio temporal
                            os.remove(file_to_save0)
                            os.remove(file_to_save1)
                    else:
                        messages.error(request,
                                       _("The polygons were not processed, because the temporary directory is "
                                         "configured."))
                else:
                    messages.error(request,
                                   _("The polygons were not processed, because a .shp and a .shx file are required."))
            else:
                messages.error(request, _("The polygons were not processed, because only two files are required."))


class OrgPictureInline(admin.TabularInline):
    DJANGOCMS_ZB_ORGANIZATIONS_SLIDER_MIN = getattr(
        settings,
        'DJANGOCMS_ZB_ORGANIZATIONS_SLIDER_MIN',
        1,
    )

    DJANGOCMS_ZB_ORGANIZATIONS_SLIDER_MAX = getattr(
        settings,
        'DJANGOCMS_ZB_ORGANIZATIONS_SLIDER_MAX',
        2,
    )

    model = OrgPicture
    extra = 0
    min_num = DJANGOCMS_ZB_ORGANIZATIONS_SLIDER_MIN
    max_num = DJANGOCMS_ZB_ORGANIZATIONS_SLIDER_MAX


class CatalogInline(admin.StackedInline):
    model = Catalog
    extra = 0
    min_num = 1


@admin.register(MicroSite)
class MicroSiteAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "organization":
            kwargs["queryset"] = Organization.objects.filter(is_enabled=True)
        return super(MicroSiteAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ['organization', 'slug', 'is_enabled']
    inlines = (OrgPictureInline, CatalogInline,)
    search_fields = ['organization__name', 'organization__category__name', 'organization__category__parent__name']
    autocomplete_fields = ['organization']
    list_filter = ["is_enabled", "organization__category", "organization__category__parent"]

    def get_fieldsets(self, request, obj=None):
        if obj:  # editing an existing object
            return (
                [
                    (_("Main Options"), {
                        'fields': (
                            ('organization', 'slug'), 'abstract', 'content', 'video', 'is_enabled')
                    }),
                ]
            )
        else:
            return (
                [
                    (_("Main Options"), {
                        'fields': ('organization', 'abstract', 'content', 'video', 'is_enabled')
                    }),
                ]
            )
