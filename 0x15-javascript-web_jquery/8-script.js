$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (films) {
      $.each(films.results, function (i, film) {
        $('UL#list_movies').append('<LI>' + film.title + '</LI>');
      });
    },
    error: function () {
      console.error('Error fetching data');
    }
  });
});
