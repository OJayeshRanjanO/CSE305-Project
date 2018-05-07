function register()
{
    $("#emailLabel").empty();
    // alert("TEST");
    removeRedBorder('name');
    removeRedBorder('gender');
    removeRedBorder('age');
    removeRedBorder('email');
    removeRedBorder('pwd');
    var name = $("#name").val();
    // alert(name)
    var gender = $("#gender").find(":selected").text();
    var age = $("#age").val();
    var email = $("#email").val();
    var pwd = $("#pwd").val();


    if (name === ""){
        $("#name").css("border","2px solid red");
        return;
    }
    if (gender === ""){
        $("#gender").css("border","2px solid red");
        return;
    }
    if (age < 1){
        $("#age").css("border","2px solid red");
        return;
    }
    if (email === ""){
        $("#email").css("border","2px solid red");
        return;
    }
    if (pwd === ""){
        $("#pwd").css("border","2px solid red");
        return;
    }

    console.log(name + " " + gender + " " + age + " " + email + " " + pwd);
    registerData = {
        "name":name,
        "gender":gender,
        "age":age,
        "email":email,
        "pwd":pwd
    };
    // console.log(registerData)
    // This parses all the data from the form
    // var registerData = $('#registerForm').serialize();
    // var gender = $('#gender').val();
    // registerData += "&gender=" + gender;
    // // Stores it to a JSON type
    // registerData = toJSON(registerData);

    $.ajax({
        type: "POST",
        url: "/registerUser",
        data: JSON.stringify(registerData),
        dataType: "json",
        contentType : "application/json"
    }).done(function (data, textStatus, jqXHR)
    {
        // data.login from main.py
        // data = $.parseJSON(JSON.stringify(data));
        // console.log(data)
        // alert("TEST");
        // console.log(data);
        if (data.registered === "false")
        {   
            $("#emailLabel").append("<div style='color:red'> Email Address already in use </div>")
            $("#email").css("border","2px solid red");
        }
        else if (data.registered === "true")
        {
            // localStorage.setItem("username", data.username);
            window.location.href = "/"
        }
    });

}


function removeRedBorder(field){
  $("#"+field).css("border","none");

}
