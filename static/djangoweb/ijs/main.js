$(document).ready(function() {

var winHeight = jQuery(window).height();
$(".intro li.main").css('height', winHeight);
$(".intro li.main").css('padding-top', (winHeight-333)/2);

$(".intro li.main").hover(function(){
        $(this).siblings().css("width", "48%");
        $(this).css("width", "52%");
        $(this).find('.grid-list').removeClass("animated fadeOutDown");
        $(this).find('.grid-list').addClass("animated fadeInUp");
        $(this).find('.lay').removeClass("animated fadeOutDown");
        $(this).find('.lay').addClass("animated fadeInUp");
    }, function(){
    $(".intro li.main").css("width", "50%");
        $(this).find('.grid-list').removeClass("animated fadeInUp");
        $(this).find('.grid-list').addClass("animated fadeOutDown");
        $(this).find('.lay').removeClass("animated fadeInUp");
        $(this).find('.lay').addClass("animated fadeOutDown");
});

});
