$(document).ready(function () {
  $(".sidenav").sidenav();
  $("select").formSelect();
  $(".tooltipped").tooltip();
  $(".modal").modal();
  $(".carousel").carousel();
  // init Masonry
  var $grid = $(".grid").masonry({
    itemSelector: ".grid-item",
    gutter: 15,
    fitWidth: true
  });
  // layout Masonry after each image loads
  $grid.imagesLoaded().progress(function () {
    $grid.masonry("layout");
  });
});
