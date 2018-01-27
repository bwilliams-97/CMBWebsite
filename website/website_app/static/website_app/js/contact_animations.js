$(function () {
    $('#myCarousel').on('slid.bs.carousel', function (e) {
        if ($('.carousel-inner .item:last').hasClass('active')) {
            $('#myCarousel').carousel('pause');
        }
        if ($('.carousel-inner .item:first').hasClass('active')) {
            $('#myCarousel').carousel('cycle');
        }
    });
});

 $(window).scroll(function() { // check if scroll event happened
        if ($(document).scrollTop() > 80) { // check if user scrolled more than 50 from top of the browser window
          $(".navbar-fixed-top").css("background-color", "rgba(0,0,0,0.5)"); // if yes, then change the color of class "navbar-fixed-top" to white (#f8f8f8)
        } else {
          $(".navbar-fixed-top").css("background-color", "transparent"); // if not, change it back to transparent
        }
      });
