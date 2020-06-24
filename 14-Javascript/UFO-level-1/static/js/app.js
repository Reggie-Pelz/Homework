// from data.js
var tableData = data;

//select page elements
var button = d3.select('#filter-btn');
var form = d3.select('#form');
var list = d3.select('#ufo-table');
var tbody = d3.select("tbody");

//event handler function
function runEnter(){

    d3.event.preventDefault();

    tbody.html('')

    var inputElement = d3.select('#datetime');
    var inputValue = inputElement.property('value');

    console.log(inputValue);
    console.log(tableData);

    var filteredData = tableData.filter(date => date.datetime === inputValue);

    console.log(filteredData);
    
    //insert search results into table
    filteredData.forEach((sighting) => {
        var row = tbody.append("tr");
        Object.entries(sighting).forEach(([key, value]) => {
            var cell = row.append("td");
            cell.text(value);
        });

    });

};


// event handlers
button.on('click', runEnter);
form.on('submit', runEnter);
