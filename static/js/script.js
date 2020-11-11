$(document).ready(function () {
  $(".sidenav").sidenav();
  $("select").formSelect();
  $(".tooltipped").tooltip();
  $(".modal").modal();
  $(".carousel").carousel({});

  // init Masonry
  var $grid = $(".grid").masonry({
    itemSelector: ".grid-item",
    gutter: 15,
    fitWidth: true,
  });
  // layout Masonry after each image loads
  $grid.imagesLoaded().progress(function () {
    $grid.masonry("layout");
  });

  // validate select box
  $("select[required]").css({
    display: "block",
    height: 0,
    padding: 0,
    width: 0,
    position: "absolute",
  });

// responsive slick carousel 
$('.responsive').slick({
  dots: true,
  arrows: true,
  infinite: true,
  speed: 300,
  slidesToShow: 4,
  slidesToScroll: 4,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 3,
        infinite: true,
          arrows: true,

        dots: true,
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
  ]
});

});
