function logout(){
  window.location.href = "/logout"
}

function getLocations(){
    $.ajax({
      type: "POST",
      url: "/getLocation",
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
      // $("#hotelSearchResults").empty();
        // alert(JSON.stringify(data));
        // console.log(data)
        $("#flightPassengers").val(data.numPassengers);
        $("#cruisePassengers").val(data.numPassengers);
        $("#guests").val(data.numPassengers);


        var data = data.location;
        stringToAppend = "";
        for (var i = 0; i < data.length; i++){
          stringToAppend+= "<option>"+data[i].City+"</option>";
        }
        // alert(stringToAppend);
        $("#From").append(stringToAppend);
        $("#To").append(stringToAppend);
        $("#location").append(stringToAppend);

    });

}

function hotelsMetaLoad(){
  getLocations();

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
        $("#accommodationType").append(stringToAppend);

    });

}

function addToCart(obj){
  var item = obj.parentNode.parentNode.childNodes[11].getAttribute("value");
  // alert(item);

  $.ajax({
      type: "POST",
      url: "/addToCart",
      data: JSON.stringify({"item":item}),
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {

    });


}

function checkOut(){
  // alert("TEST");
  window.location.href = "/checkout"

}

function createNewGroup(){
    window.location.href = "/home"
}

function searchFlights(){
  var flightFrom = $("#From").find(":selected").text();
  var flightTo = $("#To").find(":selected").text();
  var flightLeavingDate = $("#flightLeavingDate").val().toString();
  var flightClass = $("#flightClass").find(":selected").text();
  var flightPassengers = $("#flightPassengers").val();
  // alert(flightFrom + " " + flightTo+ " " + flightLeavingDate + " " + flightClass+ " "+ flightPassengers);
  if (flightFrom === "From"){
    $("#From").css("border","2px solid red");
    return;
  }
  if (flightTo === "To"){
    $("#To").css("border","2px solid red");
    return;
  }
  if (flightLeavingDate === "mm/yy/dddd" || flightLeavingDate === ""){
    $("#flightLeavingDate").css("border","2px solid red");
    return;
  }
  if (flightClass === "Class"){
    $("#flightClass").css("border","2px solid red");
    return;
  }
  if (flightPassengers < 1){
    $("#flightPassengers").css("border","2px solid red");
    return;
  }
  var checkoutInfo = 
  {
    "resource":"flight",
    "flightFrom":flightFrom, 
    "flightTo":flightTo,
    "flightLeavingDate":flightLeavingDate,
    "flightClass":flightClass,
    "flightPassengers":flightPassengers
  };

  // alert(JSON.stringify(checkoutInfo));
  $.ajax({
      type: "POST",
      url: "/searchFlights",
      data: JSON.stringify(checkoutInfo),
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
      $("#flightSearchResults").empty();
        // alert(JSON.stringify(data));
      // console.log(data);
        var data = data.flightDetails;
        stringToAppend = "";
        for (var i = 0; i < data.length; i++){
          stringToAppend = 
            `<div class="card" >
                <div class="cardBodyFlight">Carrier: ` + data[i].Flight_Carrier + " ("+ data[i].Flight_Number +`) </div>
                <div class="cardBodyDeparture">Departure: ` + data[i].Schedule_Date +`</div>
                <div class="cardBodyDeparture">Fare: $`+ data[i].Fare * flightPassengers +`</div>
                <div class="cardBodyDeparture">`+ flightFrom + ' >>>>> ' + flightTo + `</div>
                <div class=card-hover>
                  <i onclick=addToCart(this); data-toggle="modal" data-target="#addedToCart" class="material-icons addToCartNonReview" style="font-size:50px">add_shopping_cart</i>
                </div>
                <div display=none value=Flight-`+ data[i].FlightID+`></div>
            </div>`
        }

        $("#flightSearchResults").append(stringToAppend);
    });
 

}

function searchCruises(){
  // alert("TEST");
  var cruiseFrom = $("#From").find(":selected").text();
  var cruiseTo = $("#To").find(":selected").text();
  var cruiseLeavingDate = $("#cruiseLeavingDate").val().toString();
  var cruisePassengers = $("#cruisePassengers").val();
  // alert(cruiseFrom + " " + cruiseTo+ " " + cruiseLeavingDate + " "+ cruisePassengers);
  if (cruiseFrom === "From"){
    $("#From").css("border","2px solid red");
    return;
  }
  if (cruiseTo === "To"){
    $("#To").css("border","2px solid red");
    return;
  }
  if (cruiseLeavingDate === "mm/yy/dddd" || cruiseLeavingDate === ""){
    $("#cruiseLeavingDate").css("border","2px solid red");
    return;
  }
  if (cruisePassengers < 1){
    $("#cruisePassengers").css("border","2px solid red");
    return;
  }
  var checkoutInfo = 
  {
    "resource":"cruise",
    "cruiseFrom":cruiseFrom, 
    "cruiseTo":cruiseTo,
    "cruiseLeavingDate":cruiseLeavingDate,
    "cruisePassengers":cruisePassengers
  };

  // alert(JSON.stringify(checkoutInfo));
  $.ajax({
      type: "POST",
      url: "/searchCruises",
      data: JSON.stringify(checkoutInfo),
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
        // alert(JSON.stringify(data));
        $("#cruiseSearchResults").empty();
        var data = $.parseJSON(JSON.stringify(data)).cruiseDetails;
        stringToAppend = "";
        // {"cruiseDetails": [{"CruiseID": 9, "Cruise_Name": "Caribbean Princess", "Schedule_Date": "2018-03-31", "Src_Location": 1, "Dst_Location": 4, "Fare": 700.0}]}
        for (var i = 0; i < data.length; i++){
          stringToAppend = 
            `<div class="card" >
                  <div class="cardBodyFlight">Cruise: ` + data[i].Cruise_Name +`</div>
                  <div class="cardBodyDeparture">Departure: ` + data[i].Schedule_Date +`</div>
                  <div class="cardBodyDeparture">Fare: $`+ data[i].Fare * cruisePassengers +`</div>
                  <div class="cardBodyDeparture">`+ cruiseFrom + ' >>>>> ' + cruiseTo + `</div>
                  <div class=card-hover>
                    <i onclick=addToCart(this); data-toggle="modal" data-target="#addedToCart" class="material-icons addToCart" style="font-size:50px">add_shopping_cart</i>
                    <i data-target="#showCruiseReview" data-toggle="modal" onclick="reviewResource(this);" class="material-icons review" style="font-size:50px">speaker_notes</i>
                  </div>
                  <div display=none value=Cruise-`+ data[i].CruiseID+`></div>
            </div>`
        }
        // alert(data)

        $("#cruiseSearchResults").append(stringToAppend);
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
        var data1 = data.carCompany;
        var data2 = data.carType;
        stringToAppend1 = "";
        stringToAppend2 = "";
        for (var i = 0; i < data1.length; i++){
          stringToAppend1+= "<option>"+data1[i].Car_Company+"</option>";

        }
        for (var i = 0; i < data2.length; i++){
          stringToAppend2+= "<option>"+data2[i].Car_Type+"</option>";

        }

        $("#carCompany").append(stringToAppend1);
        $("#carType").append(stringToAppend2);

    });

}

function searchCars(){
  var carCompany = $("#carCompany").find(":selected").text();
  var carType = $("#carType").find(":selected").text();
  // alert(carType + " " + carCompany);
  if (carCompany === "Company"){
    $("#carCompany").css("border","2px solid red");
    return;
  }
  if (carType === "Type"){
    $("#carType").css("border","2px solid red");
    return;
  }
  var checkoutInfo = 
  {
    "resource":"car",
    "carType":carType, 
    "carCompany":carCompany
  };

  // alert(JSON.stringify(checkoutInfo));
  $.ajax({
      type: "POST",
      url: "/searchCars",
      data: JSON.stringify(checkoutInfo),
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
      $("#carSearchResults").empty();
        var data = $.parseJSON(JSON.stringify(data)).carDetails;
        stringToAppend = "";
        for (var i = 0; i < data.length; i++){
          // alert(data[i].Car_Company + " " + data[i].Car_Type + " " + data[i].Rent);
          stringToAppend = 
            `<div class="card" >
                  <div class="cardBodyFlight">Company: ` + data[i].Car_Company +`</div>
                  <div class="cardBodyDeparture">Type: ` + data[i].Car_Type +`</div>
                  <div class="cardBodyDeparture">Rate: $`+ data[i].Rent +`</div>
                  <div class="cardBodyDeparture"></div>
                  <div class=card-hover>
                    <i onclick=addToCart(this); data-toggle="modal" data-target="#addedToCart" class="material-icons addToCartNonReview" style="font-size:50px">add_shopping_cart</i>
                  </div>
                  <div display=none value=Car-`+ data[i].CarID+`></div>
            </div>`
        }

        $("#carSearchResults").append(stringToAppend);
    });
 

}

function searchHotels(){
  var guests = $("#guests").val();
  var location = $("#location").find(":selected").text();
  var accommodationType = $("#accommodationType").find(":selected").text();
  // alert(flightFrom + " " + flightTo+ " " + flightLeavingDate + " " + flightClass+ " "+ flightPassengers);
  // alert(accommodationType + " " + location + " " + guests);
  if (location === "Location"){
    $("#location").css("border","2px solid red");
    return;
  }
  if (accommodationType === "Type"){
    $("#accommodationType").css("border","2px solid red");
    return;
  }
  if (guests < 1){
    $("#guests").css("border","2px solid red");
    return;
  }
  var checkoutInfo = 
  {
    "resource":"hotel",
    "guests":guests, 
    "location":location,
    "accommodationType":accommodationType
  };

  // alert(JSON.stringify(checkoutInfo));
  $.ajax({
      type: "POST",
      url: "/searchHotels",
      data: JSON.stringify(checkoutInfo),
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
      $("#hotelSearchResults").empty();
        // alert(JSON.stringify(data));
        var data = $.parseJSON(JSON.stringify(data)).hotelDetails;
        stringToAppend = "";
        for (var i = 0; i < data.length; i++){
          // alert(data[i].Car_Company + " " + data[i].Car_Type + " " + data[i].Rent);
          stringToAppend = 
            `<div class="card" >
                  <div class="cardBodyFlight">Location: ` + location +`</div>
                  <div class="cardBodyDeparture">Facilities: ` + data[i].Facilities +`</div>
                  <div class="cardBodyDeparture">Size: ` + data[i].Size +`</div>
                  <div class="cardBodyDeparture">Rate: $`+ data[i].Rate +`</div>
                  <div class=card-hover>
                    <i data-target="#addedToCart" data-toggle="modal" onclick="addToCart(this);" class="material-icons addToCart" style="font-size:50px">add_shopping_cart</i>
                    <i data-target="#showHotelReview" data-toggle="modal" onclick="reviewResource(this);" class="material-icons review" style="font-size:50px">speaker_notes</i>
                  </div>
                  <div display=none value=Accommodation-`+ data[i].AccommodationID+`></div>
            </div>`
        }

        $("#hotelSearchResults").append(stringToAppend);
    });
}

function getUserItems(){
    $.ajax({
      type: "POST",
      url: "/generateCheckout",
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
      var car = data.Car;
      var flight = data.Flight;
      var cruise = data.Cruise;
      var accommodation = data.Accommodation;
      var passengers = data.Passengers;
      var checkoutList = "";
      console.log(car);
      console.log(flight);
      console.log(cruise);
      console.log(accommodation);
      var cost = 0
      for (var i = 0;i < car.length; i++){
        checkoutList +=`
          <div class=item>
            <div class=itemType>
              <br>
              <p>Car</p>
            </div>
            <div class=itemDescription>
              <br>
              <p>`+ car[i].Car_Company + `</p>
              <p>`+ car[i].Car_Type + `</p>
            </div>
            <div class=itemCost>
              <br>
              <p>Price: $`+ car[i].Rent + `</p>
            </div>
          </div>`
          cost+=car[i].Rent;
      }
      for (var i = 0;i < flight.length; i++){
        checkoutList +=`
          <div class=item>
            <div class=itemType>
              <br>
              <p>Flight</p>
            </div>
            <div class=itemDescription>
              <br>
              <p>`+ flight[i].Flight_Carrier + `</p>
              <p>`+ flight[i].Class + `</p>
            </div>
            <div class=itemCost>
              <br>
              <p>Price: $`+ (flight[i].Fare * passengers) + `</p>
            </div>
          </div>`
          cost += (flight[i].Fare * passengers);
      }
      for (var i = 0;i < cruise.length; i++){
        checkoutList +=`
          <div class=item>
            <div class=itemType>
              <br>
              <p>Cruise</p>
            </div>
            <div class=itemDescription>
              <br>
              <p>`+ cruise[i].Cruise_Name + `</p>
            </div>
            <div class=itemCost>
              <br>
              <p>Price: $`+ (cruise[i].Fare * passengers) + `</p>
            </div>
          </div>`

          cost += (cruise[i].Fare * passengers);
      }
      for (var i = 0;i < accommodation.length; i++){
        checkoutList +=`
          <div class=item>
            <div class=itemType>
              <br>
              <p>Hotel</p>
            </div>
            <div class=itemDescription>
              <br>
              <p>`+ accommodation[i].Facilities + `</p>
              <p>`+ accommodation[i].Accommodation_Type + `</p>
            </div>
            <div class=itemCost>
              <br>
              <p>Price: $`+ (accommodation[i].Rate * passengers) + `</p>
            </div>
          </div>`

          cost+= (accommodation[i].Rate * passengers);
      }
      $("#checkOutItems").append(checkoutList);
      // alert(cost);
      $("#totalCost").text("Total: $"+cost);
      $("#totalCost").attr("value",cost);

    });
}

function checkoutItems(){
  // alert("TEST")
  var fname = $("#fname").val();
  var lname = $("#lname").val();
  var cc = $("#cc").val();
  var cvv = $("#cvv").val();
  var exp = $("#exp").val().toString();
  var addr = $("#addr").val();
  var cost = $("#totalCost").attr("value");
  var cardType = $("#cardType").find(":selected").text();
  alert(cost)

  // # (Payment_Type, Card_Number, Card_Holder_Name ,Card_Exp_Date, Transaction_Time, Amount_Paid)

  var toSend = {
    "Payment_Type":cardType,
    "Card_Holder_Name":fname + " " + lname,
    "Card_Number":cc,
    "Card_Exp_Date":exp,
    "Amount_Paid":cost
  }

 $.ajax({
      type: "POST",
      url: "/payTrip",
      data:JSON.stringify({"userInfo":toSend}),
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {

    });

}


function reviewResource(obj){

  var item = obj.parentNode.parentNode.childNodes[11].getAttribute("value");
  // alert(item);
  $("#resourceReview").attr("value",item);
  $("#addReviewButton").removeAttr("disabled");
  document.getElementById("reviewDetails").value = "";
  rating(0);


  $.ajax({
    type: "POST",
    url: "/fetchReview",
    data:JSON.stringify({"item":item}),
    dataType: "json",
    contentType : "application/json"
  }).done(function (data, textStatus, jqXHR) {
    $("#resourceReview").empty();
      if (data.userInReview === "True"){
          $("#addReviewButton").attr("disabled","disabled");
      }
      data = data.Reviews;
      stringToAppend = "";
      for (var i = 0; i < data.length;i++){
        stringToAppend +=
        `<a href="#" class="list-group-item"> 
          Name: `+ data[i].Name +`<br>
          Comment:  `+ data[i].Review_Details +`<br>
          Rating:  `+ data[i].Rating +`<br>
        </a>`
      }
      // alert(stringToAppend);
      $("#resourceReview").append(stringToAppend);

  });
}


function addReview(){
  var rating = $("#rating1").parent().attr("value");
  var comment = document.getElementById("reviewDetails").value.toString();
  var item = $("#resourceReview").attr("value");
  $("#addReviewButton").attr("disabled","disabled");
  if (comment.length < 1 || comment.length > 500){
    $("#reviewDetails").css("border","2px solid red");
    $("#addReviewButton").removeAttr("disabled");
    return
  }


  $.ajax({
      type: "POST",
      url: "/addReview",
      data: JSON.stringify({"rating":rating,"comment":comment,"item":item}),
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
        $("#resourceReview").empty();

        data = data.Reviews;
        stringToAppend = "";
        for (var i = 0; i < data.length;i++){
          stringToAppend +=
          `<a href="#" class="list-group-item"> 
            Name: `+ data[i].Name +`<br>
            Comment:  `+ data[i].Review_Details +`<br>
            Rating:  `+ data[i].Rating +`<br>
          </a>`
        }
        // alert(stringToAppend);
        $("#resourceReview").append(stringToAppend);

    });
}


function rating(number){
  $("#rating1").parent().attr("value",number)

  $( "#rating1" ).removeClass( "checked" );
  $( "#rating2" ).removeClass( "checked" );
  $( "#rating3" ).removeClass( "checked" );
  $( "#rating4" ).removeClass( "checked" );
  $( "#rating5" ).removeClass( "checked" );

  if (number >= 1){
      $( "#rating1" ).addClass( "checked" )
  }
  if (number >= 2){
      $( "#rating2" ).addClass( "checked" )
  }
  if (number >= 3){
      $( "#rating3" ).addClass( "checked" )
  }
  if (number >= 4){
      $( "#rating4" ).addClass( "checked" )
  }
  if (number === 5){
      $( "#rating5" ).addClass( "checked" )
  }

  // alert($("#rating1").parent().attr("value"));
}

function redirectTo(id){
  // alert(id);
  if (id === "cruise"){window.location.href = "/cruises"};
  if (id === "flight"){window.location.href = "/flights"};
  if (id === "hotel"){window.location.href = "/hotels"};
  if (id === "car"){window.location.href = "/cars"};

}


function removeRedBorder(field){
  $("#"+field).css("border","none");

}