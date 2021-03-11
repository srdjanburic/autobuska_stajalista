const id_tacka = document.getElementById('id_tacka')
const dodajStanicuButton = document.getElementById('dodaj_stanicu')
const dodajLinijuButton = document.getElementById('dodaj_liniju')
let naziv = document.getElementById('naziv_linije')

let uslovZaDodavanjeLinije = false
let chekirajStanicu

var listaStanica = []


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

//dodavanje nove linije
function dodajLiniju(){
    if(naziv.value == ''){
        alert('Unesi naziv linije')
        
        
    }
    else{
        let nazivLinije = naziv.value
        const data = { nazivLinije, listaStanica}
        const options = {
            method: 'POST',
            headers: {
                "Content-type":"application/json"
            },
            body: JSON.stringify(data)
        }
        fetch("http://localhost:8000/api/linija/dodaj", options)
    }
}
function omogucavanjeCuvanjaLinije(){
    if(listaStanica.length>=3 ){
        dodajLinijuButton.disabled = false
    }else{
        dodajLinijuButton.disabled = true
    }
}
function uslov(){
    dodajLinijuButton.disabled=true
    uslovZaDodavanjeLinije = true
    
    
} 

// //Dodavanje nove stanice
function dodajStanicu(){
    
    id_tacka.readOnly = true
    dodajStanicuButton.hidden = true
    alert('Izaberi poziciju na mapi')
    map.addEventListener('click', function(e){
        
        const forma = document.querySelector('#forma')
        forma.hidden = false
        let clickedCoordinate = e.coordinate
        id_tacka.value = clickedCoordinate.toString()   
        document.getElementById('id_naziv').focus()        
    })
}

// Prikaz stanica iz baze
async function prikaziStanice(url){
    const response = await fetch(url)
    const data = await response.json()
    
    let pom = []
    for(let i = 0; i <data.length; i++){
       
        pom.push(new ol.Feature({
            geometry: new ol.geom.Point(data[i].fields.tacka.split(',').map(Number)),
            naziv: data[i].fields.naziv,
            opis: data[i].fields.opis,
            id: data[i].pk
        }))
    }
    const strokeStyle = new ol.style.Stroke({
        color: [46,45,45,1],
        width: 1.2
    })

    const cicleStyle = new ol.style.Circle({
        fill: new ol.style.Fill({
            color: [245,45,5,1]
        }),
        radius: 7,
        stroke: strokeStyle

    })
    var layer = new ol.layer.Vector({
        source: new ol.source.Vector({
            features: pom
        }),
        style: new ol.style.Style({
            image:cicleStyle
        })
    })
    map.addLayer(layer)
}
    //Vectore feature pop-up logic
    const overlayContainerElement = document.querySelector('.overlay-container')
    const overlayLayer = new ol.Overlay({
        element: overlayContainerElement
    })

    map.addOverlay(overlayLayer)

    const overlayFeatureName = document.getElementById('feature-name')
    const overlayFeatureAdditionalInfo = document.getElementById('feature-additional-info')


    map.on('click', function(e){
        overlayLayer.setPosition(undefined)
        let id
        map.forEachFeatureAtPixel(e.pixel,function(feature, layer){
            
            let clickedCoordinate = e.coordinate
            let ime = feature.get('naziv')
            let opis = feature.get('opis')
            id = feature.get('id')
            
            overlayLayer.setPosition(clickedCoordinate)
            overlayFeatureName.innerHTML = ime
            overlayFeatureAdditionalInfo.innerHTML = opis
            
        })
            //prikazivanje dugmeta za dodavanje linije
            if(uslovZaDodavanjeLinije){
                chekirajStanicu = document.getElementById('chekirajStanicu')
                overlayContainerElement.style.display = 'block'
                console.log('dva')
                if(listaStanica.includes(id)){
                    console.log('srdjan')
                    chekirajStanicu.innerHTML = 'X'
                    chekirajStanicu.classList = 'btn btn-danger'
                    
                    //ako je stanica oznacena, sljedeci dio koda ju izbacuje iz liste
                    chekirajStanicu.onclick =  ()=>{
                        for(let i = 0 ; i < listaStanica.length; i++){
                            if(listaStanica[i] === id){
                                listaStanica.splice(i,1)
                                chekirajStanicu.innerHTML = 'Dodaj'
                                chekirajStanicu.classList = 'btn btn-primary'
                                overlayContainerElement.style.display = 'none'
                            }
                        }
                        omogucavanjeCuvanjaLinije()
                    }
                }else{
                    chekirajStanicu.innerHTML = 'Dodaj'
                    chekirajStanicu.classList = 'btn btn-primary'

                    //ako stanica nije oznacena, sljedeci dio koda ju ubacuje u listu 
                    chekirajStanicu.onclick = (f) => {
                        
                        
                        listaStanica.push(id)
                        chekirajStanicu.innerHTML = 'X'
                        chekirajStanicu.classList = 'btn btn-danger'
                        overlayContainerElement.style.display = 'none'
                        omogucavanjeCuvanjaLinije()
                    }
                }
                
            }
        
    })





    

