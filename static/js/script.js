//Variables
new_page = false;
/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function selectSchedule() {
    document.getElementById("scheduleDropdown").classList.toggle("show");
    document.getElementById("cancelscheduleDropdown").classList.remove("show");
};

function cancelSchedule() {
  document.getElementById("cancelscheduleDropdown").classList.toggle("show");
  document.getElementById("scheduleDropdown").classList.remove("show");
};

//When an event is being clicked
function schedule(index, Event_Dates, Event_Times, Spot_Total, Spot_Available, Room_Number) {
  // index = index.rowIndex
  // document.getElementById("Event").deleteRow(index);

  var table = document.getElementById("table");
  if (table.classList.contains("table_title")) {
    table.classList.remove("table_title");
    table.classList.toggle("table_title_display");
  }
  var rowCount = table.rows.length;  
  console.log(rowCount);
  var row = table.insertRow(rowCount);  
  var cell1 = row.insertCell(0);
  var cell2 = row.insertCell(1);
  var cell3 = row.insertCell(2);
  var cell4 = row.insertCell(3);
  var cell5 = row.insertCell(4);
  var cell6 = row.insertCell(5);
  cell1.innerHTML = Event_Dates;
  cell2.innerHTML = Event_Times;
  cell3.innerHTML = Spot_Total;
  cell4.innerHTML = Spot_Available;
  cell5.innerHTML = Room_Number;
  cell6.innerHTML = "Add";
  Event_Times = Event_Times.replace(/ /g, '');
  document.getElementById("list").innerHTML += Event_Dates + " " + Event_Times + " " + Spot_Total + " " + Spot_Available + " " + Room_Number + " " + "Add" + " ";
};

function unSchedule(index, Event_Dates, Event_Times, Spot_Total, Spot_Available, Room_Number){
  // index = index.rowIndex
  // document.getElementById("All_Event").deleteRow(index);

  var table = document.getElementById("table");
  if (table.classList.contains("table_title")) {
    table.classList.remove("table_title");
    table.classList.toggle("table_title_display");
  }

  var rowCount = table.rows.length;  
  console.log(rowCount);
  var row = table.insertRow(rowCount);  
  var cell1 = row.insertCell(0);
  var cell2 = row.insertCell(1);
  var cell3 = row.insertCell(2);
  var cell4 = row.insertCell(3);
  var cell5 = row.insertCell(4);
  var cell6 = row.insertCell(5);
  cell1.innerHTML = Event_Dates;
  cell2.innerHTML = Event_Times;
  cell3.innerHTML = Spot_Total;
  cell4.innerHTML = Spot_Available;
  cell5.innerHTML = Room_Number;
  cell6.innerHTML = "Drop";
  Event_Times = Event_Times.replace(/ /g, '');

  document.getElementById("list").innerHTML += Event_Dates + " " + Event_Times + " " + Spot_Total + " " + Spot_Available + " " + Room_Number + " " + "Drop" + " ";
};

function passData(){
  student_name = document.getElementById("student_name").value;
  student_email = document.getElementById("student_email").value;
  student_email = student_email.replaceAll(" ", "");
  document.getElementById("list").innerHTML += student_name + " " + student_email + " ";
  Data = document.getElementById("list").innerHTML;

  $.ajax({ 
    url: '/', 
    type: 'POST', 
    data: { 'data': Data }, 
  });

  alert("Submitted, please confirm the result in the Google sheet");

  var table = document.getElementById("table");
  if (table.classList.contains("table_title_display")) {
    table.classList.remove("table_title_display");
    table.classList.toggle("table_title");
  }
  
  for(var i = 1; i < table.rows.length;){
    table.deleteRow(i);
  }

  document.getElementById("student_name").value = "";
  document.getElementById("student_email").value = "";
  document.getElementById("list").innerHTML = "";

  if(new_page == false){
    window.open("https://docs.google.com/spreadsheets/d/1BWoxXRK9Fk1leIw-J07AIp6nj2EnPEDkqhPUtRCJ7IE/edit?usp=sharing", "_blank");
    new_page = true
  };
  
};

//Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
};