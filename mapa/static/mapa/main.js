
    const map = new ol.Map({
        view: new ol.View({
            center:[1914531.2339354588, 5586893.354533319],
            zoom: 8
        }),
       
        target: 'js-map'
    })
    const openStreetMapStandard = new ol.layer.Tile({
        source: new ol.source.OSM(),
        visible: true,
        title: 'OSMStandard'
    })
    map.addLayer(openStreetMapStandard)

    map.addEventListener('click', function(e){
        console.log(e.coordinate)
    })

    var layer = new ol.layer.Vector({
        source: new ol.source.Vector({
            features: [
                new ol.Feature({
                    geometry: new ol.geom.Point([1914531.2339354588, 5586893.354533319])
                })
            ]
        })
    });
    map.addLayer(layer);

    map.addEventListener('click', function(e){
        var layer = new ol.layer.Vector({
            source: new ol.source.Vector({
                features: [
                    new ol.Feature({
                        geometry: new ol.geom.Point(e.coordinate)
                    })
                ]
            })
        })
        map.addLayer(layer)
    })
  
// Prikaz stanica iz baze

  

//     var attribution = new ol.control.Attribution({
//         collapsible: false
//     });
   
//     var map = new ol.Map({
//      //  controls: ol.control.defaults({attribution: false}).extend([attribution]), 
//         layers: [
//             new ol.layer.Tile({
//                 source: new ol.source.OSM({
//                     url: 'https://tile.openstreetmap.be/osmbe/{z}/{x}/{y}.png',
//                     attributions: [ ol.source.OSM.ATTRIBUTION, 'Tiles courtesy of <a href="https://geo6.be/">GEO-6</a>' ],
//                     maxZoom: 18
//                 })
//             })
//         ],
//         target: 'js-map',
//         view: new ol.View({
//             center: ol.proj.fromLonLat([4.35247, 50.84673]),
//             maxZoom: 18,
//             zoom: 12
//         })
//     });
//     var layer = new ol.layer.Vector({
//         source: new ol.source.Vector({
//             features: [
//                 new ol.Feature({
//                     geometry: new ol.geom.Point(ol.proj.fromLonLat([4.35247, 50.84673]))
//                 })
//             ]
//         })
//     });
//   //  map.addLayer(layer);

//     var container = document.getElementById('popup');
//     var content = document.getElementById('popup-content');
//     var closer = document.getElementById('popup-closer');
   
//     var overlay = new ol.Overlay({
//         element: container,
//         autoPan: true,
//         autoPanAnimation: {
//             duration: 250
//         }
//     });
//     map.addOverlay(overlay);
   
//     closer.onclick = function() {
//         overlay.setPosition(undefined);
//         closer.blur();
//         return false;
//     };
//     map.on('singleclick', function (event) {
//         if (map.hasFeatureAtPixel(event.pixel) === true) {
//             var coordinate = event.coordinate;
   
//             content.innerHTML = '<b>Hello world!</b><br />I am a popup.';
//             overlay.setPosition(coordinate);
//         } else {
//             overlay.setPosition(undefined);
//             closer.blur();
//         }
//     });

   

    

