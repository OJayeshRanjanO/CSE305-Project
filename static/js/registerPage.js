function register()
{
    if (validate_form() === true)
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
    else
    {
        alert("Please fill out all fields");
    }
}

function toJSON(data)
{
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

function validate_form()
{
    var nameLength = $("#name").size();
    var ageLength = $("#age").size();
    var emailLength = $("#email").size();
    var passwordLength = $("#pwd").size();

    console.log("Length of name: " + nameLength);
    console.log("Length of age: " + ageLength);
    console.log("Length of email: " + emailLength);
    if (nameLength > 0 && ageLength > 0 && emailLength > 0 && passwordLength > 0)
        return true;
    else
        return false;
}

