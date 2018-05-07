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

  if (id === "cruise"){
    document.getElementById(id).style.backgroundColor = "grey";
    document.getElementById("addResource").dataset.target  = "#addCruise";
    getLocations();
  };
  if (id === "flight"){
    document.getElementById(id).style.backgroundColor = "grey";
    document.getElementById("addResource").dataset.target  = "#addFlight";
    getLocations();

  };
  if (id === "hotel"){
    document.getElementById(id).style.backgroundColor = "grey";
    document.getElementById("addResource").dataset.target  = "#addHotel";
    hotelsMetaLoad();
    getLocations();
  };
  if (id === "car"){
    document.getElementById(id).style.backgroundColor = "grey";
    document.getElementById("addResource").dataset.target = "#addCar";
    carMetaData();
    
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
  removeRedBorder('carCompany');
  removeRedBorder('price');
  var carType = $("#carType").find(":selected").text();
  var carCompany = $("#carCompany").val();
  var price = $("#price").val();

  if (carCompany === ""){
    $("#carCompany").css("border","2px solid red");
    return;
  }
  if (price === ""){
    $("#price").css("border","2px solid red");
    return;
  }
  $("#addCar").modal('hide');

  $.ajax({
      type: "POST",
      url: "/addCar",
      data:JSON.stringify({"carType":carType,"carCompany":carCompany,"price":price}),
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {

    });

}

function addHotel(){
  removeRedBorder('facilities');
  removeRedBorder('rate');
  removeRedBorder('discount');
  removeRedBorder('size');

  var accommodationType = $("#accommodationType").find(":selected").text();
  var location =  $("#location").find(":selected").text();
  var facilities = $("#facilities").val();
  var rate = $("#rate").val();
  var discount = $("#discount").val();
  var size = $("#size").val();
  // alert(accommodationType + " " + location + " " + facilities + " " + rate + " " + discount + " " + size);
  if (facilities === ""){
    $("#facilities").css("border","2px solid red");
    return;
  }
  if (rate <= 0){
    $("#rate").css("border","2px solid red");
    return;
  }
  if (discount < 0 || discount > 100 || discount ===""){
    $("#discount").css("border","2px solid red");
    return;
  }
  if (size < 1){
    $("#size").css("border","2px solid red");
    return;
  }

  $("#addHotel").modal('hide');


  $.ajax({
      type: "POST",
      url: "/addHotel",
      data:JSON.stringify({"accommodationType":accommodationType,"location":location,"facilities":facilities,"rate":rate,"discount":discount,"size":size}),
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {

    });
}


function addCruise(){
  removeRedBorder('cruiseName');
  removeRedBorder('cruiseDate');
  removeRedBorder('fare');
  var cruiseName =  $("#cruiseName").val();
  var cruiseDate =  $("#cruiseDate").val().toString();
  var csrcLocation = $("#csrcLocation").find(":selected").text();
  var cdstLocation = $("#cdstLocation").find(":selected").text();
  var fare = $("#fare").val();
  // alert(cruiseName + " " + cruiseDate + " " + csrcLocation + " " + cdstLocation + " " + fare);
  if (cruiseName === ""){
    $("#cruiseName").css("border","2px solid red");
    return;
  }
  if (cruiseDate === "mm/dd/yyyy" || cruiseDate === ""){
    $("#cruiseDate").css("border","2px solid red");
    return;
  }
  if (fare <= 0){
    $("#fare").css("border","2px solid red");
    return;
  }

  $("#addCruise").modal('hide');


  $.ajax({
      type: "POST",
      url: "/addCruise",
      data:JSON.stringify({"cruiseName":cruiseName,"cruiseDate":cruiseDate,"csrcLocation":csrcLocation,"cdstLocation":cdstLocation,"fare":fare}),
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {

    });
}

function addFlight(){
  removeRedBorder('flightCarrier');
  removeRedBorder('flightNumber');
  removeRedBorder('flightDate');
  removeRedBorder('flightFare');

  var flightCarrier =  $("#flightCarrier").val();
  var flightNumber =  $("#flightNumber").val();
  var flightDate =  $("#flightDate").val().toString();
  var fsrcLocation = $("#fsrcLocation").find(":selected").text();
  var fdstLocation = $("#fdstLocation").find(":selected").text();
  var Class = $("#Class").find(":selected").text();
  var flightFare = $("#flightFare").val();

  if (flightCarrier === ""){
    $("#flightCarrier").css("border","2px solid red");
    return;
  }
  if (flightNumber === ""){
    $("#flightNumber").css("border","2px solid red");
    return;
  }
  if (flightDate === "mm/dd/yyyy" || flightDate === ""){
    $("#flightDate").css("border","2px solid red");
    return;
  }
  if (fsrcLocation === fdstLocation){
    $("#fsrcLocation").css("border","2px solid red");
    $("#fdstLocation").css("border","2px solid red");
    return;
  }
  if (flightFare <= 0){
    $("#flightFare").css("border","2px solid red");
    return;
  }

  $("#addFlight").modal('hide');

  var obj = {
    "flightCarrier":flightCarrier,
    "flightNumber":flightNumber,
    "flightDate":flightDate,
    "fsrcLocation":fsrcLocation,
    "fdstLocation":fdstLocation,
    "Class":Class,
    "fare":flightFare
  }

  $.ajax({
      type: "POST",
      url: "/addFlight",
      data:JSON.stringify(obj),
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

function hotelsMetaLoad(){
  //Loading room Type
  $.ajax({
      type: "POST",
      url: "/getRoomType",
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
        var data = data.roomList;
        stringToAppend = "";
        for (var i = 0; i < data.length; i++){
          stringToAppend+= "<option>"+data[i].Accommodation_Type+"</option>";
        }
        // alert(stringToAppend);
        $("#accommodationType").empty();
        $("#accommodationType").append(stringToAppend);

    });

}

function getLocations(){
    $.ajax({
      type: "POST",
      url: "/getLocation",
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {


        var data = data.location;
        stringToAppend = "";
        for (var i = 0; i < data.length; i++){
          stringToAppend+= "<option>"+data[i].City+"</option>";
        }
        // alert(stringToAppend);
        // $("#From").append(stringToAppend);
        // $("#To").append(stringToAppend);
        $("#location").empty();
        $("#csrcLocation").empty();
        $("#cdstLocation").empty();
        $("#fsrcLocation").empty();
        $("#fdstLocation").empty();

        $("#location").append(stringToAppend);
        $("#csrcLocation").append(stringToAppend);
        $("#cdstLocation").append(stringToAppend);
        $("#fsrcLocation").append(stringToAppend);
        $("#fdstLocation").append(stringToAppend);

    });

}

function viewResource(){
  var currentTab = $("#currentResource").attr("value");
  if (currentTab === "cruise"){listCruises()};
  if (currentTab === "flight"){listFlights()};
  if (currentTab === "hotel"){listHotels()};
  if (currentTab === "car"){listCars()};

}


function removeRedBorder(field){
  $("#"+field).css("border","none");

}

function getCurrentDate(obj){
  obj.type='date'
  var d = new Date();
  var month = d.getMonth()+1;
  if (month < 10){
    month = "0"+(d.getMonth()+1)
  }
  var day = d.getDate()+1;
  if (day < 10){
    day = "0"+(d.getMonth()+1)
  }
  console.log(day)
  $("#"+obj.id).attr("value",d.getFullYear()+"-"+month+"-"+day);
  $("#"+obj.id).attr("min",d.getFullYear()+"-"+month+"-"+day);

}
