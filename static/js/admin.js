function logout()
{
  window.location.href = "/logout"
}

function listFlights()
{
    // All active flights
    $("#viewResource").empty();
  $.ajax({
      type: "POST",
      url: "/listFlights"
    }).done(function (data, textStatus, jqXHR) {
        var data = $.parseJSON(data).flightList;
        console.log(data);
        stringToAppend = "";
        for (var i = 0; i < data.length; i++){
          if (data[i].Active === 0){
            stringToAppend += `<a href="#" class="list-group-item" value=Flight-`+data[i].FlightID+`>ID: `+data[i].FlightID+" <br> Flight: "+ data[i].Flight_Carrier+ " ("+data[i].Flight_Number+") - "+data[i].Class+"<br> Date: "+data[i].Schedule_Date+" <br> "+data[i].Src_Location+" >>>>>> "+data[i].Dst_Location+`<span class="badge badge-danger" style="background-color:red">--</span></a>`
          }else{
            stringToAppend += `<a href="#" class="list-group-item" value=Flight-`+data[i].FlightID+`>ID: `+data[i].FlightID+" <br> Flight: "+ data[i].Flight_Carrier+ " ("+data[i].Flight_Number+") - "+data[i].Class+"<br> Date: "+data[i].Schedule_Date+" <br> "+data[i].Src_Location+" >>>>>> "+data[i].Dst_Location+`<span class="badge badge-danger" style="background-color:green">O</span></a>`

          }
        }

        $("#viewResource").append(stringToAppend);
    });
}

function listCruises()
{
    // All active flights
  $("#viewResource").empty();
  $.ajax({
      type: "POST",
      url: "/listCruises"
    }).done(function (data, textStatus, jqXHR) {
        var data = $.parseJSON(data).cruiseList;
        console.log(data);
        stringToAppend = "";
        for (var i = 0; i < data.length; i++){
          if (data[i].Active === 0){
            stringToAppend += `<a href="#" class="list-group-item" value=Cruise-`+data[i].CruiseID+`>ID: `+data[i].CruiseID+" <br> Cruise: "+ data[i].Cruise_Name+ "<br> Date: "+data[i].Schedule_Date+" <br> "+data[i].Src_Location+" >>>>>> "+data[i].Dst_Location+`<span class="badge badge-danger" style="background-color:red">--</span></a>`
          }else{
            stringToAppend += `<a href="#" class="list-group-item" value=Cruise-`+data[i].CruiseID+`>ID: `+data[i].CruiseID+" <br> Cruise: "+ data[i].Cruise_Name+ "<br> Date: "+data[i].Schedule_Date+" <br> "+data[i].Src_Location+" >>>>>> "+data[i].Dst_Location+`<span class="badge badge-danger" style="background-color:green">O</span></a>`

          }
        }

        $("#viewResource").append(stringToAppend);
    });
}


function listCars()
{
    // All active flights
  $("#viewResource").empty();
  $.ajax({
      type: "POST",
      url: "/listCars"
    }).done(function (data, textStatus, jqXHR) {
        var data = $.parseJSON(data).carsList;
        console.log(data);
        stringToAppend = "";
        for (var i = 0; i < data.length; i++){
          console.log(data[i].Active)
          if (data[i].Active === 0){
            stringToAppend += `<a href="#" class="list-group-item" value=CarID-`+data[i].CarID+`>ID: `+data[i].CarID+" <br> Company: "+ data[i].Car_Company+ "<br> Type: "+data[i].Car_Type+`<span class="badge badge-danger" style="background-color:red">--</span></a>`
          }else{
            stringToAppend += `<a href="#" class="list-group-item" value=CarID-`+data[i].CarID+`>ID: `+data[i].CarID+" <br> Company: "+ data[i].Car_Company+ "<br> Type: "+data[i].Car_Type+`<span class="badge badge-danger" style="background-color:green">O</span></a>`

          }
        }

        $("#viewResource").append(stringToAppend);
    });
}


function listHotels()
{
    // All active flights
  $("#viewResource").empty();
  $.ajax({
      type: "POST",
      url: "/listHotels"
    }).done(function (data, textStatus, jqXHR) {
        var data = $.parseJSON(data).hotelsList;
        console.log(data);
        stringToAppend = "";
        for (var i = 0; i < data.length; i++){
          if (data[i].Active === 0){
            stringToAppend += `<a href="#" class="list-group-item" value=Accommodation-`+data[i].AccommodationID+`>ID: `+data[i].AccommodationID+" <br> Type: "+ data[i].Accommodation_Type+ "<br> Facilities: "+data[i].Facilities+"<br> Size: "+data[i].Size+"<br> Location: "+data[i].Location+`<span class="badge badge-danger" style="background-color:red">--</span></a>`
          }else{
            stringToAppend += `<a href="#" class="list-group-item" value=Accommodation-`+data[i].AccommodationID+`>ID: `+data[i].AccommodationID+" <br> Type: "+ data[i].Accommodation_Type+ "<br> Facilities: "+data[i].Facilities+"<br> Size: "+data[i].Size+"<br> Location: "+data[i].Location+`<span class="badge badge-danger" style="background-color:green">O</span></a>`

          }
        }

        $("#viewResource").append(stringToAppend);
    });
}

function updateGUI(id){
    document.getElementById("cruise").style.backgroundColor = "transparent";
    document.getElementById("flight").style.backgroundColor = "transparent";
    document.getElementById("hotel").style.backgroundColor = "transparent";
    document.getElementById("car").style.backgroundColor = "transparent";
      $("#viewResource").empty();

  // alert(id);
  if (id === "cruise"){document.getElementById(id).style.backgroundColor = "grey"};
  if (id === "flight"){document.getElementById(id).style.backgroundColor = "grey"};
  if (id === "hotel"){document.getElementById(id).style.backgroundColor = "grey"};
  if (id === "car"){document.getElementById(id).style.backgroundColor = "grey"};
    
    $("#currentResource").attr("value",id);


}

function viewResource(){
  var currentTab = $("#currentResource").attr("value");
  if (currentTab === "cruise"){listCruises()};
  if (currentTab === "flight"){listFlights()};
  if (currentTab === "hotel"){listHotels()};
  if (currentTab === "car"){listCars()};

}

