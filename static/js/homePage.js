function logout(){
  window.location.href = "/logout"
}

function searchFlights(){
  var flightFrom = $("#flightFrom").find(":selected").text();
  var flightTo = $("#flightTo").find(":selected").text();
  var flightLeavingDate = $("#flightLeavingDate").val().toString();
  var flightClass = $("#flightClass").find(":selected").text();
  var flightPassengers = $("#flightPassengers").val();
  alert(flightFrom + " " + flightTo+ " " + flightLeavingDate + " " + flightClass+ " "+ flightPassengers);
  var checkoutInfo = 
  {
    "resource":"flight",
    "flightFrom":flightFrom, 
    "flightTo":flightTo,
    "flightLeavingDate":flightLeavingDate,
    "flightClass":flightClass,
    "flightPassengers":flightPassengers
  };

  alert(JSON.stringify(checkoutInfo));
  $.ajax({
      type: "POST",
      url: "/searchFlights",
      data: JSON.stringify(checkoutInfo),
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
        alert(JSON.stringify(data));
        var data = $.parseJSON(JSON.stringify(data)).flightDetails;
        stringToAppend = "";
        for (var i = 0; i < data.length; i++){
          stringToAppend = 
            `<div class="card" style="width: 18rem;">
              <div class="card-body">
                  <div class="cardBodyFlight">` + data[i].Flight_Carrier +`</div>
                  <div class="cardBodyDeparture">TBD</div>
                  <div class="cardBodyPrice">$`+ data[i].Fare +`</div>
              </div>
            </div>`
        }

        $("#flightSearchResults").append(stringToAppend);
    });
 

}
