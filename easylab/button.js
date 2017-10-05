// Find all the buttons
var all_btns = document.getElementsByTagName('button');

// Attach event handlers
for (btn in all_btns) {
    btn.addEventListener('click', handleMyClick);
}

// Handle a click event
function handleMyClick(event) {
    // Find the table row where the click happened
    var tr = event.target.parentNode.parentNode;
    // Find all the data in the row
    var tds = tr.getElementsByTagName('td');
    var data = [];
    for (td in tds) {
        data.push(td.innerHTML);
    }
}
