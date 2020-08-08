  url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson'

  // d3.json(url, function(data) {

  //   console.log(data.features[0].geometry.coordinates)  //lat and lng
  //   console.log(data.features[0].properties.mag)  //magnitude   

  // })






d3.json(url, function(data) {

  console.log(data.features)

  function markerSize(mag) {
    return mag * 10000;
  }

  function getColor(d) {
    return d <= 1 ? '#8DFF33' :
           d > 1 & d <= 2  ? '#FFFF33' :
           d > 2 & d <= 3  ? '#FFBB33' :
           d > 3 & d <= 4  ? '#FF8A33' :
           d > 4 & d <= 5   ? '#FB6530' :
           d > 5   ? '#FB3030' :
                      '#FFEDA0';
  }

  var myMap = L.map("map", {
    center: [40.2338, -111.6585],
    zoom: 5
  });

  L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/light-v10",
  accessToken: API_KEY
  }).addTo(myMap);

  for (var i = 0; i < data.features.length; i++) {
    L.circle([(data.features[i].geometry.coordinates[1]), (data.features[i].geometry.coordinates[0])], {
      fillOpacity: 0.75,
      color: 'gray',
      weight: .5,
      fillColor: getColor(data.features[i].properties.mag),
      radius: markerSize(data.features[i].properties.mag) 
    }).bindPopup("<h2>" + data.features[i].properties.place + "</h2> <hr> <h2>Magnitude: " + data.features[i].properties.mag + "</h2>").addTo(myMap);

  }

  var legend = L.control({position: 'bottomright'});

    legend.onAdd = function (map) {

      var div = L.DomUtil.create('div', 'info legend'),
          mag = [0, 1, 2, 3, 4, 5],
          labels = [];

      // loop through our density intervals and generate a label with a colored square for each interval
      for (var i = 0; i < mag.length; i++) {
          div.innerHTML +=
              '<i style="background:' + getColor(mag[i] + 1) + '"></i> ' +
              mag[i] + (mag[i + 1] ? '&ndash;' + mag[i + 1] + '<br>' : '+');
      }

      return div;
  };

  legend.addTo(myMap);

})
