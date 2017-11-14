$(function () {
    $.ajax({
        url: "/datas/", type: "get", dataType: "json", success: function (t) {
            $(".nav").html(template("nav_tpl", {data: t})), $(".content").html(template("content_tpl", {data: t}))

        }
    }), $(".nav").on("click", "li a", function () {
        return $("html, body").animate({scrollTop: $($(this).attr("href")).offset().top}), !1
    }), $(document).scroll(function (t) {
        var o = $(".nav").offset().left;
        $(document).scrollTop() >= $(".header").height() ? $(".nav").css({
            position: "fixed",
            top: 0,
            left: o
        }) : $(document).scrollTop() < $(".header").height() && $(".nav").css({
            position: "absolute",
            top: 0,
            left: 0
        }),
            //console.log($(".content_items h3").first().offset().top),
            $(document).scrollTop() >= $(".content_items h3").first().offset().top ? $(".back_to_top").show() : $(".back_to_top").hide()
    }), $(".nav").on("click", ".nav_item", function () {
        $(this).parent().siblings().children().removeClass("active"), $(this).addClass("active")
    }), $(".back_to_top").click(function () {
        return $("html, body").animate({scrollTop: 0}), !1
    })
});