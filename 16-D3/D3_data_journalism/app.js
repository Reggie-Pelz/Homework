// @TODO: YOUR CODE HERE!      


var svgWidth = 960;
var svgHeight = 600;

var margin = {
  top: 20,
  right: 40,
  bottom: 80,
  left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

var svg = d3
  .select("#scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// var chosenXAxis = "Poverty (%)";



d3.csv('data.csv').then(function(metadata) {
    console.log(metadata)

    metadata.forEach(function(data) {
        data.poverty = +data.poverty;
        data.smokes = +data.smokes;
    });

    var xScale = d3.scaleLinear()
        .domain([0, (metadata.length)/2])
        .range([0, width]);

    var yLinearScale = d3.scaleLinear()
        .domain([0, d3.max(metadata, d => d.smokes)+5])
        .range([height, 0]);

    
    var bottomAxis = d3.axisBottom(xScale);
    var leftAxis = d3.axisLeft(yLinearScale);

    var xAxis = chartGroup.append("g")
        .classed("x-axis", true)
        .attr("transform", `translate(0, ${height})`)
        .call(bottomAxis);

    chartGroup.append("g")
        .call(leftAxis);


    chartGroup.append('g')
        .selectAll("dot")
        .data(metadata)
        .enter()
        .append("circle")
          .attr("cx", function (d) { return xScale(d.poverty); } )
          .attr("cy", function (d) { return yLinearScale(d.smokes); } )
          .attr("r", 12)
          .style("fill", "blue")

    chartGroup.append('text')
        .attr('x', 350)
        .attr('y', 550)
        .attr("font-weight", 700)
        .text('Poverty Rate (%)')

    chartGroup.append('text')
        .attr('x', -300)
        .attr('y', -50)
        .attr("transform", "rotate(-90)")
        .attr("font-weight", 700)
        .text('Smoking Rate (%)')

    var circleLabels = chartGroup.selectAll(null).data(metadata).enter().append("text");

    circleLabels
        .attr("x", function(d) { return xScale(d.poverty); })
        .attr("y", function(d) { return yLinearScale(d.smokes); })
        .text(function(d) { return d.abbr; })
        .attr("font-size", "9px")
        .attr("text-anchor", "middle")
        .attr("fill", "white");

});
