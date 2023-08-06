$(document).ready(function() {
  $('#autosubmitform').on('change', function() {
    var $form = $(this).closest('form');
    $form.find('input[type=submit]').click();
  });
});
