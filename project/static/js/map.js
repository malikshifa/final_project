var shapes = [];

var map = L.map('map').setView([-41.2858, 174.78682], 14);
mapLink =
    '<a href="http://openstreetmap.org">OpenStreetMap</a>';
L.tileLayer(
    'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; ' + mapLink + ' Contributors',
    maxZoom: 18,
    }).addTo(map);

var LeafIcon = L.Icon.extend({
    options: {
        shadowUrl:
            'http://leafletjs.com/docs/images/leaf-shadow.png',
        iconSize:     [38, 95],
        shadowSize:   [50, 64],
        iconAnchor:   [22, 94],
        shadowAnchor: [4, 62],
        popupAnchor:  [-3, -76]
    }
});

var greenIcon = new LeafIcon({
    iconUrl: 'http://leafletjs.com/docs/images/leaf-green.png'
    });

var drawnItems = new L.FeatureGroup();
map.addLayer(drawnItems);

var drawControl = new L.Control.Draw({
    position: 'topright',
    draw: {
        polygon: {
            shapeOptions: {
                color: 'purple'
            },
            allowIntersection: false,
            drawError: {
                color: 'orange',
                timeout: 1000
            },
            showArea: true,
            metric: false,
            repeatMode: true
        },
        polyline: {
            shapeOptions: {
                color: 'red'
            },
        },
        rect: {
            shapeOptions: {
                color: 'green'
            },
        },
        circle: {
            shapeOptions: {
                color: 'steelblue'
            },
        },
        marker: {
            icon: greenIcon
        },
    },
    edit: {
        featureGroup: drawnItems
    }
});
map.addControl(drawControl);

map.on('draw:created', function (e) {
    var type = e.layerType,
        layer = e.layer;

    if (type === 'marker') {
        layer.bindPopup('A popup!');
    }

    drawnItems.addLayer(layer);
});

var latlngs = [[37, -109.05],[41, -109.03],[41, -102.05],[37, -102.04]];

var polygon = L.polygon(latlngs, {color: 'red'}).addTo(map);
//map.fitBounds(polygon.getBounds());



var drawnItems = new L.FeatureGroup();
map.addLayer(drawnItems);

map.on('draw:created', function (e) {

    var type = e.layerType,
        layer = e.layer;

    drawnItems.addLayer(layer);

    var shapes = getShapes(drawnItems);

    console.log(shapes);
    console.log(layer);

    // Process them any way you want and save to DB
    // ...

});
var getShapes = function(drawnItems) {


    drawnItems.eachLayer(function(layer) {

        // Note: Rectangle extends Polygon. Polygon extends Polyline.
        // Therefore, all of them are instances of Polyline
        if (layer instanceof L.Polyline) {
            shapes.push(layer.getLatLngs());
        }

        if (layer instanceof L.Circle) {
            shapes.push([layer.getLatLng()])
        }

        if (layer instanceof L.Marker) {
            shapes.push([layer.getLatLng()]);
        }

    });
    console.log("shapes");
    return shapes;

};

function show()
{

    var vals = request.lsitB
}

function store()
{
    console.log("check-1");
    if(shapes != null && shapes.length != 0)
    {
        var stringpoint = JSON.stringify(shapes);

        $.ajax({
        type: 'POST',
        url: "/mapdata/",
        data: {csrfmiddlewaretoken: window.CSRF_TOKEN,
                stringpoint: stringpoint,
                datatype:'JSON',
                data:'JSON',
                 },
        success: function() {
            console.log("Success!");
        }
    });
    }
    else
    {
        alert("There is no shape drawn on the map");
    }
}

