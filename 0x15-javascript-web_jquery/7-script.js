$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function (data) {
      $('DIV#character').append(data.name);
    },
    error: function () {
      console.error('Error fetching data');
    }
  });
});
