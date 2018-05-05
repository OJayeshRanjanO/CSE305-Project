function login()
{
    var formData = $('#loginForm').serialize();
    formData = toJSON(formData);
    // alert(formData)
    $.ajax({
      type: "POST",
      url: "/checkLogin",
      data: formData,
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
        data = $.parseJSON(JSON.stringify(data));
        if (data.login === "None"){
//                alert(data.login);
            $("#loginForm").append("<div style='color:red'> Incorrect password or password </div><br>")
            $("#email").css("border","2px solid red");
            $("#pwd").css("border","2px solid red");
        }else if (data.login === "Passenger"){
            window.location.href = "/home"
        }else if (data.login === "Employee"){
            window.location.href = "/admin"
        }
    });
}

function toJSON(data){
  data = data.split("&");
  var obj={};
    for(i = 0; i < data.length; i++)
    {
        var x = data[i].split("=");
        obj[x[0]] = x[1].replace("%40","@");
    }
  // obj['username'] = localStorage['username']
  return JSON.stringify(obj);
}


function createGroup(){
    $.ajax({
      type: "POST",
      url: "/createGroup",
      data: JSON.stringify({"numPassengers":$('#numPassengers').val()}),
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
        window.location.href = "/flights"

    });
}

function viewGroup(){
    $("#viewGroups").empty();
    $.ajax({
      type: "POST",
      url: "/viewGroup",
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
      pI = data.partyInfo;
      vG = data.viewGroup;
      stringToAppend = ""
      for (var i = 0; i < pI.length; i++){
        groupID = pI[i].PartyID;
        // console.log(pI[i])
        groupInfo = vG[groupID];
        // console.log(groupID);
        stringToAppend += `<br><br><a href="#" style="background:#e8e5e5" class="list-group-item" value=GroupID-`+groupID+`>Group: `+groupID+` &emsp;&emsp;&emsp; Size: ( `+ pI[i].Party_Size +` )</a>`
        cost = 0

        for (var j = 0; j < groupInfo.length; j++){
          resourceData = groupInfo[j];
          if (resourceData.AccommodationID){
            stringToAppend+=`
            <a href="#" class="list-group-item" value=AccommodationID-`+resourceData.AccommodationID+`>
            <div style="height:100%;width:50px;border-right:1px solid black;position:relative;float:left;text-align:center;margin-right:15px"> Hotel</div> 
            Location: `+resourceData.Location+`&emsp;
            Type: `+resourceData.Accommodation_Type+`&emsp;
            Facilities: `+resourceData.Facilities+`&emsp;
            Rate/Stay: `+resourceData.Rate+`
            </a>`
            cost+=resourceData.Rate;
          }
          if (resourceData.FlightID){
            stringToAppend+=`
            <a href="#" class="list-group-item" value=FlightID-`+resourceData.FlightID+`>
            <div style="height:100%;width:50px;border-right:1px solid black;position:relative;float:left;text-align:center;margin-right:15px"> Flight</div> 
            Src: `+resourceData.Src+` > Dst: `+resourceData.Dst+`&emsp;
            Flight: `+resourceData.Flight_Number+`&emsp;`+resourceData.Class+`&emsp;
            Fare/Person: `+resourceData.Fare+`
            </a>`
            cost+=(resourceData.Fare * pI[i].Party_Size);
          }
          if (resourceData.CarID){
            stringToAppend+=`
            <a href="#" class="list-group-item" value=CarID-`+resourceData.CarID+`>
            <div style="height:100%;width:50px;border-right:1px solid black;position:relative;float:left;text-align:center;margin-right:15px"> Car</div> 
            Company: `+resourceData.Car_Company+`&emsp;
            Type: `+resourceData.Car_Type+`&emsp;
            Rent/Use: `+resourceData.Rent+`
            </a>`
            cost+=resourceData.Rent;
          }
          if (resourceData.CruiseID){
            stringToAppend+=`
            <a href="#" class="list-group-item" value=CruiseID-`+resourceData.CruiseID+`>
            <div style="height:100%;width:50px;border-right:1px solid black;position:relative;float:left;text-align:center;margin-right:15px"> Cruise</div> 
            Src: `+resourceData.Src+` > Dst: `+resourceData.Dst+`&emsp;
            Cruise: `+resourceData.Cruise_Name+`&emsp;
            Fare/Person: `+resourceData.Fare+`
            </a>`
            cost+=(resourceData.Fare * pI[i].Party_Size);
          }
          console.log(resourceData);
        }
        stringToAppend+=`
        <a href="#" class="list-group-item" style="background-color:yellow">
        <div style="height:100%;width:50px;border-right:1px solid black;position:relative;float:left;text-align:center;margin-right:15px;"> Total</div>
        Cost: `+cost+`
        </a>`
      }
      $("#viewGroups").append(stringToAppend);

    });

}

function logout()
{
  window.location.href = "/logout"
}