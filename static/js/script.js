$(document).ready(function () {
  $(".sidenav").sidenav();
  $("select").formSelect();
  $(".tooltipped").tooltip();
  $(".modal").modal();
  $(".carousel").carousel({
    numVisible: "7",
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

  // valide select box
  $("select[required]").css({
    display: "block",
    height: 0,
    padding: 0,
    width: 0,
    position: "absolute",
  });
});
