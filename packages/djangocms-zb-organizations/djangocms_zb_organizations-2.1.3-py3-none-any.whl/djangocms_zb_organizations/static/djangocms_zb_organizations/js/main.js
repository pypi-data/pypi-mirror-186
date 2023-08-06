/*
 *     Copyright (C)  2022. CQ Inversiones SAS.
 *
 *     This program is free software: you can redistribute it and/or modify
 *     it under the terms of the GNU General Public License as published by
 *     the Free Software Foundation, either version 3 of the License, or
 *     (at your option) any later version.
 *
 *     This program is distributed in the hope that it will be useful,
 *     but WITHOUT ANY WARRANTY; without even the implied warranty of
 *     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *     GNU General Public License for more details.
 *
 *     You should have received a copy of the GNU General Public License
 *     along with this program.  If not, see <https://www.gnu.org/licenses/>.
 *
 */

/*Configuración y carga de mapa con Google Maps*/

$(function () {
    // Se valida si el navegador soporta Geolocalización
    if (navigator.geolocation) {
        // Se obtiene las coordnadas de la posición del navegador y se pasa a la función getCoords para centrar el mapa
        navigator.geolocation.getCurrentPosition(getCoords, getError);
    } else {
        // Si el navegador no soporta geolocalización se centra el mapa con las coordenadas de Neiva.
        initialize(2.9262767, -75.2936958);
    }


});

// Función que toma los datos de latitud y longitud
function getCoords(position) {
    let lat = position.coords.latitude;
    let lng = position.coords.longitude;

    // Se pasa latitud y longitud a la función initialize
    initialize(lat, lng);
}

function getError() {
    // Si hay un error al obtener las coordenadas por medio de Geolocalización, se centra el mapa con las
    //coordenadas de Neiva
    initialize(2.9262767, -75.2936958);
}

// Función para definir los parametros de configuración del mapa de Google y los puntos, se le pasa la latitud y
// longitud.

let map = L.map('map');

function initialize(lat, lng) {
    // se agrega el mapa al elemento del html con id map
    map.setView([lat, lng], 8);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    }).addTo(map);

    var myIcon = L.icon({
        iconUrl: '/static/djangocms_zb_organizations/img/usted_esta_aqui.png',
        iconSize: [30, 50],
    });

    // Se agrega marcador de usted está aquí con la posición de la persona si los datos son diferentes al default
    if (lat !== 2.9262767 && lng !== -75.2936958) {
        let marker = L.marker(
            [lat, lng],
            {icon: myIcon},
        );
        marker.addTo(map);
    }

    // Se recoge el array que viene con las organizaciones en la variable window.data desde el template
    let markers = org;

    // Se recorre los multiples markers location, latitude y longitude que vienen en el array
    for (let i = 0; i < markers.length; i++) {
        let marker = L.marker(
            [markers[i][3], markers[i][4]],
            {title: markers[i][1] + " - " + markers[i][2]},
        );
        marker.addTo(map);
    }
}

function markerCenter(id) {
    let alertMsm = document.getElementById("alert-msm");
    let classAlert = alertMsm.classList;
    if (!classAlert.contains("d-none")) {
        alertMsm.classList.add("d-none");
    }
    let organizations = org;
    let org_res = organizations.find(org => org[0] === id);
    map.flyTo([org_res[3], org_res[4]], 14);
    var iconOrange = L.icon({
        iconUrl: '/static/djangocms_zb_organizations/img/marker_icon_o.png',
        iconSize: [25, 41],
        iconAnchor: [13, 41],
    });
    if (this.mark) {
        map.removeLayer(this.mark);
    }
    mark = L.marker(
        [org_res[3], org_res[4]],
        {icon: iconOrange, title: org_res[1]},
    );
    mark.addTo(map);

    fetch("/organizaciones/get-geo-json/", {
        method: "POST",
        body: JSON.stringify({id: id}),
        headers: {
            "X-CSRFToken": $('input[name=csrfmiddlewaretoken]').val(),
            "X-Requested-With": "XMLHttpRequest",
            "content-type": "application/json"
        }
    }).then(response => {
        if (response.ok && response.status === 200)
            return response.json();
        else {
            throw Error(response.statusText);
        }
    }).then(data => {
        if (data) {
            map.flyTo([org_res[3], org_res[4]], 12);
        }
        if (this.leafMapShapes) {
            this.leafMapShapes.clearLayers();
        }
        leafMapShapes = L.geoJson(data, {
            style: function () {
                return {
                    color: '#000000',
                    opacity: 0.6,
                    fillColor: '#00FF00',
                    fillOpacity: 0.2,
                    weight: 2,
                    dashArray: '3 1 3',
                }
            }
        });
        leafMapShapes.addTo(map);
    }).catch((err) => {
        if (this.leafMapShapes) {
            this.leafMapShapes.clearLayers();
        }
    })
}

function showMsm() {
    let alertMsm = document.getElementById("alert-msm");
    alertMsm.classList.remove("d-none");
    setTimeout(() => {
        alertMsm.classList.add("d-none");
    }, 5000)
}

/* Manejo de los selects y estilos adicionales dinamicos*/
const select_search = document.querySelector("#select-search");
const select_search_s_category = document.querySelector("#s-category");
const group_s_category = document.getElementById("group-s-category");
const group_input_search = document.getElementById("group-input-search");
const btn_send_s_category = document.getElementById("btn-send-s-category");
const msm_keyword = document.getElementById("msm-keyword");
const mostrar = () => {
    const valor = select_search.value;
    if (valor === "0" || valor === "category") {
        if (group_input_search)
            group_input_search.style.display = 'none';
    } else
        if (group_input_search)
            group_input_search.style.display = 'inline';

    if (valor === "keyword"){
        if (msm_keyword)
            msm_keyword.style.display = 'inline';
    }else{
        if (msm_keyword)
            msm_keyword.style.display = 'none';
    }

    if (valor === "category") {
        if (group_s_category)
            group_s_category.style.display = 'inline';
        const valor_s_cat = select_search_s_category.value;
        if (valor_s_cat === "0") {
            if (btn_send_s_category)
                btn_send_s_category.style.display = "none";
        } else {
            if (btn_send_s_category)
                btn_send_s_category.style.display = "inline";
        }
    } else
        if (group_s_category)
            group_s_category.style.display = 'none';
};

select_search.addEventListener("change", mostrar);
select_search_s_category.addEventListener("change", mostrar);