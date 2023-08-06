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
# Date: 2/12/2022 5:48 p. m.
# Project: Djangocms-pruebas
# Module Name: organization
# ****************************************************************

from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed
from django.core.exceptions import ObjectDoesNotExist
from djangocms_zb_organizations.lib.exceptions import NotFound

from djangocms_zb_organizations.models import Organization
from djangocms_zb_organizations.lib.serializers import OrganizationSerializer


class OrganizationService(ModelViewSet):
    """
    Service class from CRUD operations Organization model
    """

    model_class = Organization
    permission_classes = [permissions.AllowAny]
    serializer_class = OrganizationSerializer

    def by_category(self, request, *args, **kwargs):
        """
       List of Organization entity
       :param request: request from HTTP
       :param args: Named args
       :param kwargs: Dict Args
       :return: Response with a dataset with a list of organizations by category
       """
        try:
            status_return = []
            data_return = []
            request_data = request.data
            if "category_id" in request_data:
                queryset = self.model_class.objects.get_organizations_by_category(request_data["category_id"])
                serializer = self.get_serializer(instance=queryset, many=True)
                data_return = serializer.data
                status_return = status.HTTP_200_OK if len(data_return) > 0 else status.HTTP_204_NO_CONTENT
                return Response(data=data_return, status=status_return)
        except APIException as exc:
            raise APIException(msg=exc.detail.get("message"), error=exc.detail.get("detail"),
                               http_status=exc.status_code) from exc
        except Exception as exc:
            raise APIException(error=str(exc), http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(data=data_return, status=status_return)

    def count_by_category(self, request, *args, **kwargs):
        """
       List of Organization entity
       :param request: request from HTTP
       :param args: Named args
       :param kwargs: Dict Args
       :return: Response with a dataset with a list of organizations by category
       """
        try:
            status_return = []
            request_data = request.data
            if "category_id" in request_data:
                total_organizations = self.model_class.objects.get_count_by_category(request_data["category_id"])
                status_return = status.HTTP_200_OK if total_organizations > 0 else status.HTTP_204_NO_CONTENT
        except APIException as exc:
            raise APIException(msg=exc.detail.get("message"), error=exc.detail.get("detail"),
                               http_status=exc.status_code) from exc
        except Exception as exc:
            raise APIException(error=str(exc), http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(data=total_organizations, status=status_return)

    def get_geo_json(self, request, *args, **kwargs):
        """
        Base method to get a model element, using its primary key
        :param request: request object received from HTTP
        :param args: args data from request
        :param kwargs: kwargs data from request
        :return: Response with an organization.
        """
        try:
            data_return = []
            status_return = status.HTTP_400_BAD_REQUEST
            request_data = request.data
            if request.is_ajax():
                if request.method == "POST" and "id" in request_data:
                    queryset = self.model_class.objects.get(id=request_data["id"])
                    serializer = self.get_serializer(instance=queryset, many=False)
                    data_return = serializer.data
                    status_return = status.HTTP_200_OK if len(data_return) > 0 else status.HTTP_204_NO_CONTENT
            else:
                raise MethodNotAllowed("geo_json", detail=_("Request is not ajax"), code="not_ajax")
        except ObjectDoesNotExist as exc:
            raise NotFound(_("Organization polygon not found")) from exc
        except MethodNotAllowed as exc:
            raise MethodNotAllowed("geo_json", exc.detail, exc.get_codes()) from exc
        except Exception as exc:
            raise APIException(str(exc)) from exc
        else:
            return Response(data=data_return, status=status_return)