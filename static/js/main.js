$(document).ready(function() {
    // alert("hey there!");
    // $("#search-box").on("change paste keyup", new_query);
    $("#search-button").on("click", new_query);
});

function new_query(event) {
    // console.log($("#search-box").val());
    
    $.post("/search", { query: $("#search-box").val() }, function(data) {
        console.log(data);
        var res = ""
        for (var key in data) {
            // console.log(data[key].url);
            res += "<a target='_blank' href='/article?id=" + data[key]._id + "'>" + data[key].title + "</a><br />";
        }
        $("#result").html(res);
    });
}