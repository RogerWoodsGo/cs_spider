var website_list = new Array("all", "36kr","cyb","other")
function onChangeWebsite(website, e){
    $("#website_menu li").removeClass("active");
    $(e).addClass("active")
}

function onChangeItem(item, e){
   //已有的和这一条 
    $(e).find("a").toggleClass("selected");
    var website = $("#website_menu .active a").attr("name");
    var query_path = "website=" + website + "&item=" + item;
    $.get("/item?" + query_path,function(data,status){
        alert("Data: " + data + "\nStatus: " + status);
    });
}
