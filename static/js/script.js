$(document).ready(function () {
  $(".sidenav").sidenav();
  $("select").formSelect();
  $(".tooltipped").tooltip();
  $(".modal").modal();
  $(".carousel").carousel();
  $(".grid").masonry({
    // options
    itemSelector: ".grid-item",
    columnWidth: 200,
  });
});
