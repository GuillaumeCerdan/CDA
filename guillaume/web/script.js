
$(document).ready(function() {
    let url = "http://localhost/cda/guillaume/web/data.json";

    console.log(url);

    $.ajax({
        type: "GET",
        dataType: "json",
        url: url,
        data: {},
        success: function(data) {
            $.each(data, function(key, value) {
                let html = "<div class='layout'><div class='white-bck'>";
                html += "<p class='mb-10px mt-0px fs-12'>" + key + "</p>";
                html += "<div class='d-flex-wrap'>";
                $.each(value, function(key2, value2) {
                    html += "<p class='fs-10 mr-5px'>" + key2 + " : " + value2 + "</p>";
                });
                html += "</div></div></div>";
                $("#data").append(html);
            });
        }
    });
});


// let url = "http://localhost/cda/guillaume/web/data.json";

// fetch(url)
// .then(data => {
//     console.log(data);
// })
// .then(res => {
//     console.log(res);
// });
