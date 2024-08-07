$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (data) {
      $('DIV#hello').text(data.hello);
    },
    error: function () {
      console.error('Error fetching data');
    }
  });
});
