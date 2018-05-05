function validate_form()
{
    var nameLength = $("#name").val().length;
    var ageLength = $("#age").val().length;
    var emailLength = $("#email").val().length;
    var passwordLength = $("#pwd").val().length;

    if (nameLength > 0 && ageLength > 0 && emailLength > 0 && passwordLength > 0)
    {
        register();
        return true;
    }
    else
    {
        //alert("Please fill out form");
        return false;
    }
}

function register()
{
    // This parses all the data from the form
    var registerData = $('#registerForm').serialize();
    var gender = $('#gender').val();
    registerData += "&gender=" + gender;
    // Stores it to a JSON type
    registerData = toJSON(registerData);

    $.ajax({
        type: "POST",
        url: "/registerUser",
        data: registerData,
        dataType: "json",
        contentType : "application/json"
    }).done(function (data, textStatus, jqXHR)
    {
        // data.login from main.py
        data = $.parseJSON(JSON.stringify(data));
        if (data.registered === "fail")
        {
            $("#registerContainer").append("<div style='color:red'> Incorrect info </div>")
        }
        else if (data.registered === "true")
        {
            // localStorage.setItem("username", data.username);
            window.location.href = "/home"
        }
    });

}

function toJSON(data)
{
  data = data.split("&");
  var obj={};
    for(i = 0; i < data.length; i++)
    {
        var x = data[i].split("=");
        x[1] = x[1].replace(/%20/g," ");
        obj[x[0]] = x[1].replace("%40","@");
    }
    console.log(obj);
  // obj['username'] = localStorage['username']
  return JSON.stringify(obj);
}