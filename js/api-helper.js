const REST_API_URL = "http://ec2-52-32-33-15.us-west-2.compute.amazonaws.com:5002/"
const USER_ID = "0"

function GetSensorData(user_id, sensor_id, from_index, fCallback, /* cb args  */ ) {
    var xhttp = new XMLHttpRequest();
    xhttp.callback = fCallback
    xhttp.arguments = Array.prototype.slice.call(arguments, 3);
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            this.callback.apply(this, this.arguments)
        }
    };
    xhttp.open("GET", REST_API_URL + user_id.toString() + "/sensor/" + sensor_id.toString() + "/data/from/" + from_index.toString(), true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send(null);
}

function GetSpendingForecastData(user_id, from_index, fCallback, /* cb args  */ ) {
    var xhttp = new XMLHttpRequest();
    xhttp.callback = fCallback
    xhttp.arguments = Array.prototype.slice.call(arguments, 3);
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            this.callback.apply(this, this.arguments)
        }
    };
    xhttp.open("GET", REST_API_URL + user_id.toString() + "/spending_forecast/data/from/" + from_index.toString(), true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send(null);
}

function addData(chart, label, data) {
    chart.data.labels.push(label);
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(data);
    });
    chart.update();
}

function updateValue(elementId, newValue) {
  document.getElementById(elementId).innerHTML = newValue
};

