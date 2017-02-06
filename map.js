function createMap(width, height) {
  var scale = 90;
  var x = width/2
  var y = height / 1.2

  var svg = d3.select("#map")          // during debug cursor first goes to height 
              .append("svg")           // then comes back again to d3.select("#map") why??
              .attr("width", width)
              .attr("height", height);

  var projection = d3.geoMercator()
                      .scale(scale) 
                      .translate([x,y]); 

  var path = d3.geoPath().projection(projection)

  // svg.append("g")
  //     .attr("class", "countries")
  //       .selectAll("path")
                   
}