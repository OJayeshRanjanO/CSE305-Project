function register()
{
    var regsiterData = $('#registerForm').serialize();
    regsiterData = toJSON(regsiterData);
    $.ajax({
      type: "POST",
      url: "/register-user",
      data: regsiterData,
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR)
    {
        data = $.parseJSON(JSON.stringify(data));
        if (data.login === "fail")
        {
//                alert(data.login);
            $("#loginContainer").append("<div style='color:red'> Incorrect password or password </div>")
        }
        else if (data.login === "true")
        {
            // localStorage.setItem("username", data.username);
            window.location.href = "/home"
        }
    });
}