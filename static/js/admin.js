function logout()
{
  window.location.href = "/logout"
}

function listFlights()
{
    // All active flights
  $.ajax({
      type: "GET",
      url: "/listFlights"
    }).done(function (data, textStatus, jqXHR) {
        var data = $.parseJSON(data).flightList;
        console.log(data);
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

function searchCruises(){
  alert("TEST");
  var cruiseFrom = $("#cruiseFrom").find(":selected").text();
  var cruiseTo = $("#cruiseTo").find(":selected").text();
  var cruiseLeavingDate = $("#cruiseLeavingDate").val().toString();
  var cruisePassengers = $("#cruisePassengers").val();
  alert(cruiseFrom + " " + cruiseTo+ " " + cruiseLeavingDate + " "+ cruisePassengers);
  var checkoutInfo = 
  {
    "resource":"cruise",
    "cruiseFrom":cruiseFrom, 
    "cruiseTo":cruiseTo,
    "cruiseLeavingDate":cruiseLeavingDate,
    "cruisePassengers":cruisePassengers
  };

  alert(JSON.stringify(checkoutInfo));
  $.ajax({
      type: "POST",
      url: "/searchCruises",
      data: JSON.stringify(checkoutInfo),
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
        alert(JSON.stringify(data));
        var data = $.parseJSON(JSON.stringify(data)).cruiseDetails;
        stringToAppend = "";
        // {"cruiseDetails": [{"CruiseID": 9, "Cruise_Name": "Caribbean Princess", "Schedule_Date": "2018-03-31", "Src_Location": 1, "Dst_Location": 4, "Fare": 700.0}]}
        for (var i = 0; i < data.length; i++){
          stringToAppend = 
            `<div class="card" style="width: 18rem;">
              <div class="card-body">
                  <div class="cardBodyFlight">` + data[i].Cruise_Name +`</div>
                  <div class="cardBodyDeparture">` + data[i].Schedule_Date +`</div>
                  <div class="cardBodyPrice">$`+ data[i].Fare +`</div>
              </div>
            </div>`
        }
        alert(data)

        $("#cruiseSearchResults").append(stringToAppend);
    });
 

}

function redirectTo(id){
  // alert(id);
  if (id === "cruise"){window.location.href = "/cruises"};
  if (id === "flight"){window.location.href = "/home"};
  if (id === "hotel"){window.location.href = "/hotels"};
  if (id === "car"){window.location.href = "/cars"};

}

