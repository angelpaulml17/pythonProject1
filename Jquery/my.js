$(document).ready(function(){
//$('#addColumnChild').click(function(){
//   $('#demo tr').each(function(){
//      $(this).append(`<td></td>`);
//   });
//});
//
//$('#addRowChild').click(function(){
//   $('#my-table tbody').append(`<tr>${$('#default-row').html()}</tr>`);
//});
$(".buttonselect").click(function () {
    // Loop over the rows of the table and append the td tag
    $("demo.addColumnChild tr").append("<td>col1</td>");
});
});
