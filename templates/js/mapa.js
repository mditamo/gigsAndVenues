//<![CDATA[

var customIcons = {
        restaurant: {
                icon: 'images/icono.png',
                shadow: 'http://labs.google.com/ridefinder/images/mm_20_shadow.png'
        },
        bar: {
                icon: 'images/logo.png',
                shadow: 'http://labs.google.com/ridefinder/images/mm_20_shadow.png'
        }
};

               
function processGeocoding(location,map, callback, id, type)  
{  
	var geocoder = new google.maps.Geocoder(); 
    // Propiedades de la georreferenciación  
    var request = {  
        address: location  
    }  
    // Invocación a la georreferenciación (proceso asíncrono)  
    geocoder.geocode(request, function(results, status) {  
        if(status == google.maps.GeocoderStatus.OK)  
        {  
            // Invoca la función de callback  
            callback (results, map, id, type);  
            // Retorna los resultados obtenidos  
            return results;  
        }  
        // En caso de error retorna el estado  
        return status;  
    });  
}  

function addMarkers(geocodes, map, id, type)  
 {  
 		 var infoWindow = new google.maps.InfoWindow;
 		 var icon = customIcons[type] || {};
 	     //Centra el mapa en la nueva ubicación  
         var marker = new google.maps.Marker({  
             map: map,  
             icon: icon.icon,
             shadow: icon.shadow,
             title: 'Evento'
         });  
         marker.setPosition(geocodes[0].geometry.location);  
     	 bindInfoWindow(marker, map, infoWindow, id);
 }  

function load() {
		
        var map = new google.maps.Map(document.getElementById("map"), {
                center: new google.maps.LatLng(-34.60821750,-58.47316130000001),
                zoom: 12,
                mapTypeId: 'roadmap'});        
        var infoWindow = new google.maps.InfoWindow;
        var respuesta_busqueda=$("#respuesta_busqueda");
        respuesta_busqueda.html("");
        // Change this depending on the name of your PHP file
        downloadUrl("/mapa/listado", function(data) {
                var xml = data.responseXML;
                var markers = xml.getElementsByTagName("marker");
                for (var i = 0; i < markers.length; i++) {
                		
                		var id = markers[i].getAttribute("id");
                        var address = markers[i].getAttribute("address");
                        var type = markers[i].getAttribute("type");
                        var icon = customIcons[type] || {};
        				processGeocoding(address, map, addMarkers, id, type);
        				
                        
                }
        });
}
	
	
function bindInfoWindow(marker, map, infoWindow, id) {
        google.maps.event.addListener(marker, 'click', function() {
                downloadUrl("/mapa/id/"+id+"/ver", function(data) {
                        var xml = data.responseXML;
                        var markers = xml.documentElement.getElementsByTagName("marker");
                        if (markers.length==1)
                        {
                                var nombre_sede = markers[0].getAttribute("nombre_sede");
                                var nombre_evento = markers[0].getAttribute("nombre_evento");
                                var src_imagen = markers[0].getAttribute("src_imagen");
                                var fecha = markers[0].getAttribute("fecha");
                                var hora = markers[0].getAttribute("hora");
                                infoWindow.setContent('<div class="infoWindow"><h2>'+ nombre_sede +'</h2><img src="/media/'+src_imagen+'" ><br/><br/><h2>'+ nombre_evento +'</h2><br/><br/><b>Fecha:</b>'+fecha+'<br/></br><b>hora:</b>'+hora+'</div>');
                        		infoWindow.open(map, marker);
                        }
                        
                });
        });
}
	
function downloadUrl(url, callback) {
        var request = window.ActiveXObject ?
        new ActiveXObject('Microsoft.XMLHTTP') :
        new XMLHttpRequest;

        request.onreadystatechange = function() {
                if (request.readyState == 4) {
                        request.onreadystatechange = doNothing;
                        callback(request, request.status);
                }
        };

        request.open('GET', url, true);
        request.send(null);
}

function doNothing() {}

            //]]>