$(function() {
    $( "#datepicker" ).datepicker();
});
function chooseFile() {
   $("#fileInput").click();
}
function add(){
   var dom=document.getElementById("my_table");
   var col1="<tr><td><input type="text"></td>";
   var col2="<tr><td><input type="text"></td>";
   inputdateObject.value = YYYY-MM-DD;
   var col3="<tr><td><input type="text"> YYYY-MM-DD </td>";
   var col4="<tr><td><input type="text"></td>";
   var col5="<tr><td><input type="text"></td>";
   var col6="<tr><td><input type="text"></td>";
   var col7="<tr><td><input type="text" id="datepicker" ></td>"
   var col8="<input type="file" id="fileInput" name="fileInput" />"+
"<button type="button" onclick="chooseFile();">choose file</button>";
   dom.result.value=col1+col2+col3+col4+col5+col6+col7+col8;
 }
