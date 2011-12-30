var runner = {
  close: function () {
    window.location = $("#runner-frame").attr("src");
  }
};

$(function () {
  $("#close-runner").click(runner.close);
});