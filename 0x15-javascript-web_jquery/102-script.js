$('document').ready(function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    console.log(lang);
    if (lang) {
      $.ajax({
        type: 'GET',
        url: 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + lang,
        success: function (data) {
          console.log(data);
        },
        error: function () {
          console.error('Error fetching data');
        }
      });
    }
  });
});
