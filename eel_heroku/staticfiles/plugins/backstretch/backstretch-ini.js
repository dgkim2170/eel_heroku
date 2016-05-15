$(document).ready(function() {
  $.getScript("../../static/plugins/backstretch/jquery.backstretch.min.js", function() {
    $(".fullscreen-static-image").backstretch("../../static/img/img1.jpg");
  });
});