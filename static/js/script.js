$(document).ready(function () {
  $(".sidenav").sidenav();

  $(".tooltipped").tooltip();

  $("select").formSelect();
    // validate select box
  $("select[required]").css({
    display: "block",
    height: 0,
    padding: 0,
    width: 0,
    position: "absolute",
  });

  $(".modal").modal();

// responsive slick carousel
  $(".responsive").slick({
    dots: true,
    lazyLoad: "ondemand",
    infinite: true,
    variableWidth: true,
    speed: 300,
    slidesToShow: 3,
    slidesToScroll: 9,
    centerMode: true,
    centerPadding: "100px",
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
          infinite: true,
          dots: true,
        },
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
        },
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
    ],
  });

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
});

