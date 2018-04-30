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
      url: "/listFlights",
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
        var data = data.flightList;
        console.log(data);
        stringToAppend = "";
        for (var i = 0; i < data.length; i++){
          if (data[i].Active === 0){
            stringToAppend += `<a href="#" class="list-group-item" value=Flight-`+data[i].FlightID+`>ID: `+data[i].FlightID+" <br> Flight: "+ data[i].Flight_Carrier+ " ("+data[i].Flight_Number+") - "+data[i].Class+"<br> Date: "+data[i].Schedule_Date+" <br> "+data[i].Src_Location+" >>>>>> "+data[i].Dst_Location+`<span class="badge badge-danger" style="background-color:red" onclick="toggleResource(this)">--</span></a>`
          }else{
            stringToAppend += `<a href="#" class="list-group-item" value=Flight-`+data[i].FlightID+`>ID: `+data[i].FlightID+" <br> Flight: "+ data[i].Flight_Carrier+ " ("+data[i].Flight_Number+") - "+data[i].Class+"<br> Date: "+data[i].Schedule_Date+" <br> "+data[i].Src_Location+" >>>>>> "+data[i].Dst_Location+`<span class="badge badge-danger" style="background-color:green" onclick="toggleResource(this)">O</span></a>`

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
      url: "/listCruises",
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
        var data = data.cruiseList;
        console.log(data);
        stringToAppend = "";
        for (var i = 0; i < data.length; i++){
          if (data[i].Active === 0){
            stringToAppend += `<a href="#" class="list-group-item" value=Cruise-`+data[i].CruiseID+`>ID: `+data[i].CruiseID+" <br> Cruise: "+ data[i].Cruise_Name+ "<br> Date: "+data[i].Schedule_Date+" <br> "+data[i].Src_Location+" >>>>>> "+data[i].Dst_Location+`<span class="badge badge-danger" style="background-color:red" onclick="toggleResource(this)">--</span></a>`
          }else{
            stringToAppend += `<a href="#" class="list-group-item" value=Cruise-`+data[i].CruiseID+`>ID: `+data[i].CruiseID+" <br> Cruise: "+ data[i].Cruise_Name+ "<br> Date: "+data[i].Schedule_Date+" <br> "+data[i].Src_Location+" >>>>>> "+data[i].Dst_Location+`<span class="badge badge-danger" style="background-color:green" onclick="toggleResource(this)">O</span></a>`

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
      url: "/listCars",
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
        var data = data.carsList;
        console.log(data);
        stringToAppend = "";
        for (var i = 0; i < data.length; i++){
          console.log(data[i].Active)
          if (data[i].Active === 0){
            stringToAppend += `<a href="#" class="list-group-item" value=CarID-`+data[i].CarID+`>ID: `+data[i].CarID+" <br> Company: "+ data[i].Car_Company+ "<br> Type: "+data[i].Car_Type+`<span class="badge badge-danger" style="background-color:red" onclick="toggleResource(this)">--</span></a>`
          }else{
            stringToAppend += `<a href="#" class="list-group-item" value=CarID-`+data[i].CarID+`>ID: `+data[i].CarID+" <br> Company: "+ data[i].Car_Company+ "<br> Type: "+data[i].Car_Type+`<span class="badge badge-danger" style="background-color:green" onclick="toggleResource(this)">O</span></a>`

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
      url: "/listHotels",
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
        var data = data.hotelsList;
        console.log(data);
        stringToAppend = "";
        for (var i = 0; i < data.length; i++){
          if (data[i].Active === 0){
            stringToAppend += `<a href="#" class="list-group-item" value=Accommodation-`+data[i].AccommodationID+`>ID: `+data[i].AccommodationID+" <br> Type: "+ data[i].Accommodation_Type+ "<br> Facilities: "+data[i].Facilities+"<br> Size: "+data[i].Size+"<br> Location: "+data[i].Location+`<span class="badge badge-danger" style="background-color:red" onclick="toggleResource(this)">--</span></a>`
          }else{
            stringToAppend += `<a href="#" class="list-group-item" value=Accommodation-`+data[i].AccommodationID+`>ID: `+data[i].AccommodationID+" <br> Type: "+ data[i].Accommodation_Type+ "<br> Facilities: "+data[i].Facilities+"<br> Size: "+data[i].Size+"<br> Location: "+data[i].Location+`<span class="badge badge-danger" style="background-color:green" onclick="toggleResource(this)">O</span></a>`

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
  if (id === "cruise"){
    document.getElementById(id).style.backgroundColor = "grey";
    document.getElementById("addResource").dataset.target  = "#addCruise";
  };
  if (id === "flight"){
    document.getElementById(id).style.backgroundColor = "grey";
    document.getElementById("addResource").dataset.target  = "#addFlight";
  };
  if (id === "hotel"){
    document.getElementById(id).style.backgroundColor = "grey";
    document.getElementById("addResource").dataset.target  = "#addHotel";
  };
  if (id === "car"){
    document.getElementById(id).style.backgroundColor = "grey";
    carMetaData();
    document.getElementById("addResource").dataset.target = "#addCar";
    
  };
    
  $("#currentResource").attr("value",id);


}

function toggleResource(obj){
  // alert();
  var nodeValue = obj.parentNode.getAttribute("value");

  $.ajax({
      type: "POST",
      url: "/toggle",
      data:JSON.stringify({"nodeValue":nodeValue}),
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
      viewResource();
    });

}

function addCar(){
  var carType = $("#carType").find(":selected").text();
  var carCompany = $("#carCompany").val();
  var price = $("#price").val();

  $.ajax({
      type: "POST",
      url: "/addCar",
      data:JSON.stringify({"carType":carType,"carCompany":carCompany,"price":price}),
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
      
    });

}

function carMetaData(){
    $.ajax({
      type: "POST",
      url: "/getCarData",
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
      $("#carSearchResults").empty();
        var data2 = data.carType;
        stringToAppend2 = "";
        for (var i = 0; i < data2.length; i++){
          stringToAppend2+= "<option>"+data2[i].Car_Type+"</option>";

        }
        $("#carType").append(stringToAppend2);

    });

}

function viewResource(){
  var currentTab = $("#currentResource").attr("value");
  if (currentTab === "cruise"){listCruises()};
  if (currentTab === "flight"){listFlights()};
  if (currentTab === "hotel"){listHotels()};
  if (currentTab === "car"){listCars()};

}

