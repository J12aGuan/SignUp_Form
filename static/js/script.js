//Variables
new_page = false;

//getElementById
Event_Table = document.getElementById("Event");
All_Event_Table = document.getElementById("All_Event");


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
    success: function(update_data_events)
    {
      var Deleted_Row = 0;
      var response = JSON.parse(update_data_events);
      response.forEach((response_data, loop_detect) => {
        console.log(typeof loop_detect);
        response_data.forEach((individual_data, index) => {
          if(loop_detect == 0){
            Event_Table.rows[index].cells.item(0).innerHTML = "Date: " + individual_data["Dates:"];
            Event_Table.rows[index].cells.item(1).innerHTML = "Time: " + individual_data["Times:"];
            Event_Table.rows[index].cells.item(2).innerHTML = "Total Available: " + individual_data["Total Available:"];
            Event_Table.rows[index].cells.item(3).innerHTML = "Currently Available: " + individual_data["Currently Available:"];
            Event_Table.rows[index].cells.item(4).innerHTML = "Room Number: " + individual_data["Room Number:"];
          }
          else{
            All_Event_Table.rows[index].cells.item(0).innerHTML = "Date: " + individual_data["Dates:"];
            All_Event_Table.rows[index].cells.item(1).innerHTML = "Time: " + individual_data["Times:"];
            All_Event_Table.rows[index].cells.item(2).innerHTML = "Total Available: " + individual_data["Total Available:"];
            All_Event_Table.rows[index].cells.item(3).innerHTML = "Currently Available: " + individual_data["Currently Available:"];
            All_Event_Table.rows[index].cells.item(4).innerHTML = "Room Number: " + individual_data["Room Number:"];
          }
        })
        // console.log(response_data[0]);
        // console.log(response_data[1]);
        // console.log(response_data[2]);
        // console.log(response_data[3]);
        // console.log(response_data[4]);
      })
    },
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