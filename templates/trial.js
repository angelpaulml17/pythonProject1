function appendRow() {
  var tbl = document.getElementById('my-table'), // table reference
    row = tbl.insertRow(tbl.rows.length), // append table row
    i;
  // insert table cells to the new row
  for (i = 0; i < tbl.rows[0].cells.length; i++) {
    createCell(row.insertCell(i), i, 'row');
  }
};

// create DIV element and append to the table cell
function createCell(cell) {
  var div = document.createElement('div'), // create DIV element
    cell.appendChild(div); // append DIV to the table cell
};

// append column to the HTML table
function appendColumn() {
  var tbl = document.getElementById('my-table'), // table reference
    i;
  // open loop for each row and append cell
  for (i = 0; i < tbl.rows.length; i++) {
    createCell(tbl.rows[i].insertCell(tbl.rows[i].cells.length), i, 'col');
  }
};
