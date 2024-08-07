$('document').ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').prepend('<li>Item</li>');
  });
  $('DIV#remove_item').click(function () {
    $('UL.my_list LI:last').remove();
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
