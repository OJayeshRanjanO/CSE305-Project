function logout()
{
  window.location.href = "/logout"
}

function listFlights()
{
    // All active flights
  $.ajax({
      type: "POST",
      url: "/listFlights"
    }).done(function (data, textStatus, jqXHR) {
        var data = $.parseJSON(data).flightList;
        console.log(data);
        stringToAppend = "";
        for (var i = 0; i < data.length; i++){
//          stringToAppend = 
        }

        $("#flightSearchResults").append(stringToAppend);
    });
}

function updateGUI(id){
    document.getElementById("cruise").style.backgroundColor = "transparent";
    document.getElementById("flight").style.backgroundColor = "transparent";
    document.getElementById("hotel").style.backgroundColor = "transparent";
    document.getElementById("car").style.backgroundColor = "transparent";
  // alert(id);
  if (id === "cruise"){document.getElementById(id).style.backgroundColor = "grey"};
  if (id === "flight"){document.getElementById(id).style.backgroundColor = "grey"};
  if (id === "hotel"){document.getElementById(id).style.backgroundColor = "grey"};
  if (id === "car"){document.getElementById(id).style.backgroundColor = "grey"};
    
    $("#currentResource").attr("value",id);
    alert($("#currentResource").text());

}

