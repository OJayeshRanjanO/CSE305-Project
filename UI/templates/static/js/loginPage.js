function login(){
    var formData = $('#loginForm').serialize();
    formData = toJSON(formData);
    alert(formData)
    $.ajax({
      type: "POST",
      url: "/checkLogin",
      data: formData,
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
        data = $.parseJSON(JSON.stringify(data));
        if (data.login === "fail"){
//                alert(data.login);
            $("#loginContainer").append("<div style='color:red'> Incorrect password or password </div>")
        }else if (data.login === "true"){
            // localStorage.setItem("username", data.username);
            window.location.href = "/home"
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