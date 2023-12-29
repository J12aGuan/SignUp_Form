import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from pathlib import Path
from flask import Flask, render_template, request

#Variable
Categories = 6

#Define
Dates = []
Times = []
Formatted_Times = []
Total_Available = []
Students_Name = []
Students_Email = []
Currently_Available = []
Room_Number = []
Informations = []
Events_In_Dict = []

All_Informations = []
All_Events_In_Dict = []

#Data Received
Received_Dates = []
Received_Times = []
Received_Total_Available = []
Received_Currently_Available = []
Received_student_info = []
Received_Add_or_Drop = []
sorted_data = []

app = Flask(__name__)

# # define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
gspread_client = ServiceAccountCredentials.from_json_keyfile_name("signup-form.json", scope)
client = gspread.authorize(gspread_client)      #Give access
sheet = client.open('SignUp_Form')      #Open the whole sheet

sheet_instance = sheet.get_worksheet(0)     #Get the first worksheet

def getInfo():
    records_data = sheet_instance.get_all_records()        #Get the information from worksheet

    for data in records_data:
        try: 
            if(int(data["Currently Available:"])) >= 1:
                Dates.append(data["Dates:"])
                Times.append(data["Times:"])
                Total_Available.append(data["Total Available:"])
                Students_Name.append(data["Students Name:"])
                Students_Email.append(data["Students Email:"])
                Currently_Available.append(data["Currently Available:"])
                Room_Number.append(data["Room Number:"])
                Informations.append(data)
                All_Informations.append(data)
            else:
                Dates.append(data["Dates:"])
                Times.append(data["Times:"])
                Total_Available.append(data["Total Available:"])
                Students_Name.append(data["Students Name:"])
                Students_Email.append(data["Students Email:"])
                Currently_Available.append(data["Currently Available:"])
                Room_Number.append(data["Room Number:"])
                All_Informations.append(data)
        except:
            pass
    
def formatInfo():
    #Remove empty space in google sheet that is saved in list
    while("" in Dates):
        Dates.remove("")

    while("" in Times):
        Times.remove("")

    while("" in Total_Available):
        Total_Available.remove("")

    while("" in Currently_Available):
        Currently_Available.remove("")
    
    while("" in Room_Number):
        Room_Number.remove("")

    #Format Times
    for Time in Times:
        try:
            Formatted_Time = str(Time).replace(" ", "")
            Formatted_Times.append(Formatted_Time)
        except:
            pass

    #Remove Student Name and Student Email which we don't need to include in the form
    for Information in Informations:
        for key in ["Students Name:", "Students Email:"]:
            Information.pop(key, None)
        Events_In_Dict.append(Information)

    for All_Information in All_Informations:
        for key in ["Students Name:", "Students Email:"]:
            All_Information.pop(key, None)
        All_Events_In_Dict.append(All_Information)

@app.route('/', methods = ['GET', 'POST'])
def main():
    if request.method == 'GET':
        try:
            Dates.clear()
            Times.clear()
            Formatted_Times.clear()
            Total_Available.clear()
            Students_Name.clear()
            Students_Email.clear()
            Currently_Available.clear()
            Room_Number.clear()
            Informations.clear()
            Events_In_Dict.clear()

            All_Informations.clear()
            All_Events_In_Dict.clear()

            Received_Dates.clear()
            Received_Times.clear()
            Received_Total_Available.clear()
            Received_Currently_Available.clear()
            Received_student_info.clear()
            Received_Add_or_Drop.clear()
            sorted_data.clear()
        except:
            pass
        getInfo()
        formatInfo()
        # print("Dates: " + str(Dates))
        # print("Formatted_Times: " + str(Formatted_Times))
        # print("Total_Available: " + str(Total_Available))
        # print("Students_Name: " + str(Students_Name))
        # print("Students_Email: " + str(Students_Email))
        # print("Currently_Available: " + str(Currently_Available))
        # print("Room_Number: " + str(Room_Number))
        # print("Events_In_Dict: " + str(Events_In_Dict))
        # print("All_Events_In_Dict: " + str(All_Events_In_Dict))
        
        return render_template('index.html', Events = Events_In_Dict, All_Events = All_Events_In_Dict)
    elif request.method == "POST": 
        try:
            Dates.clear()
            Times.clear()
            Formatted_Times.clear()
            Total_Available.clear()
            Students_Name.clear()
            Students_Email.clear()
            Currently_Available.clear()
            Room_Number.clear()
            Informations.clear()
            Events_In_Dict.clear()

            All_Informations.clear()
            All_Events_In_Dict.clear()

            Received_Dates.clear()
            Received_Times.clear()
            Received_Total_Available.clear()
            Received_Currently_Available.clear()
            Received_student_info.clear()
            Received_Add_or_Drop.clear()
            sorted_data.clear()
        except:
            pass
        getInfo()
        formatInfo()
        global data 
        data = ""
        data = request.form.get('data')

        print(data)

        sorted_data = list(data.split(" "))
        while("" in sorted_data):
            sorted_data.remove("")

        student_info_categories = (int(len(sorted_data)) % Categories)
        if(student_info_categories == 2):
            Received_student_info.append(sorted_data[(int(len(sorted_data)) - 2)])      #Append name
        else:
            Received_student_info.extend([sorted_data[(int(len(sorted_data)) - student_info_categories)], sorted_data[((int(len(sorted_data))) - 2)]])      #Append name
        
        Received_student_info.append(sorted_data[(int(len(sorted_data)) - 1)])      #Append email
        sorted_data = sorted_data[0: (int(len(sorted_data) - student_info_categories))]     #Update the list
        print("sorted_data: " + str(sorted_data))
        print("Received_student_info: " + str(Received_student_info))

        for i in range(int(len(sorted_data)/Categories)):
            Received_Add_or_Drop.append(sorted_data[(Categories * (i + 1) - 1)])

        print("Received_Add_or_Drop: " + str(Received_Add_or_Drop))

        for i in range(int(len(sorted_data)/Categories)):
            Received_Dates.append(sorted_data[Categories*i])
            Received_Times.append(sorted_data[1+(Categories*i)])
            Received_Total_Available.append(sorted_data[2+(Categories*i)])
            Received_Currently_Available.append(sorted_data[3+(Categories*i)])

        for i in range(len(Dates)):
            for a in range(len(Received_Dates)):
                if (str(Dates[i]) == str(Received_Dates[a]) and str(Formatted_Times[i]) == str(Received_Times[a]) and str(Total_Available[i]) == str(Received_Total_Available[a])):
                    if(str(Received_Add_or_Drop[a]) == "Add"):
                        if (str(Currently_Available[i]) >= str(1)):
                            Index = list(All_Events_In_Dict[i].keys()).index("Currently Available:")

                            #Get already existing student_info
                            val_student_names = sheet_instance.cell(i+2, Index+1).value
                            val_student_emails = sheet_instance.cell(i+2, Index+2).value

                            #Convert student_info list to string
                            Received_student_email = Received_student_info[-1]
                            Received_student_name = " ".join(str(i) for i in Received_student_info[0: -1])

                            print("Received_student_name: " + Received_student_name)
                            print("Received_student_email: " + Received_student_email)

                            #Update the sheet_info based on already existing data
                            if(val_student_names and val_student_emails):
                                Student_Name = Students_Name[i].split("\n")
                                Student_Email = Students_Email[i].split("\n")

                                print("Student_Name: " + str(Student_Name))
                                print("Student_Email: " + str(Student_Email))


                                if(str(Received_student_name).lower() in str(Student_Name).lower()):
                                    print("You already signed up for that date, don't sign up again")          
                                    break
                                elif(str(Received_student_email).lower() in str(Student_Email).lower()):
                                    print("Your email already signed up for that date, try again with a different email")          
                                    break
                                else:
                                    sheet_instance.update_cell(i+2, Index+1, str(val_student_names + "\n" + Received_student_name))
                                    sheet_instance.update_cell(i+2, Index+2, str(val_student_emails + "\n" + Received_student_email))
                                    sheet_instance.update_cell(i+2, Index+3, (int(All_Events_In_Dict[i]["Currently Available:"])-1))
                                    print("Added in after first row")
                            else:
                                sheet_instance.update_cell(i+2, Index+1, str(Received_student_name))
                                sheet_instance.update_cell(i+2, Index+2, str(Received_student_email))
                                sheet_instance.update_cell(i+2, Index+3, (int(All_Events_In_Dict[i]["Currently Available:"])-1))
                                print("Added in first row")

                    elif(str(Received_Add_or_Drop[a]) == "Drop"):
                        if(str(Currently_Available[i]) < str(Total_Available[i])):
                            Index = list(All_Events_In_Dict[i].keys()).index("Currently Available:")

                            #Get already existing student_info
                            val_student_names = sheet_instance.cell(i+2, Index+1).value
                            val_student_emails = sheet_instance.cell(i+2, Index+2).value

                            print("val_student_names: " + val_student_names)
                            print("val_student_emails: " + val_student_emails)

                            #Convert student_info list to string
                            Received_student_name = " ".join(str(i) for i in Received_student_info[0: -1])
                            Received_student_email = Received_student_info[-1]

                            print("Received_student_name: " + Received_student_name)
                            print("Received_student_email: " + Received_student_email)

                            Student_Name = Students_Name[i].split("\n")
                            Student_Email = Students_Email[i].split("\n")

                            print("Student_Name: " + str(Student_Name))
                            print("Student_Email: " + str(Student_Email))

                            for b in range(len(Student_Name)):
                                if(str(Student_Name[b]).lower() == str(Received_student_name).lower() and str(Student_Email[b]).lower() == str(Received_student_email).lower()):
                                    #Update the sheet_info based on already existing data
                                    if(val_student_names and val_student_emails):
                                        if(b == 0 and len(Student_Name) >= 2):
                                            val_student_names = val_student_names.replace(str(Student_Name[b]) + "\n", "")
                                            val_student_emails = val_student_emails.replace(str(Student_Email[b]) + "\n", "")
                                        elif(b == 0 and len(Student_Name) < 2):
                                            val_student_names = val_student_names.replace(str(Student_Name[b]), "")
                                            val_student_emails = val_student_emails.replace(str(Student_Email[b]), "")
                                        else:
                                            val_student_names = val_student_names.replace("\n" + str(Student_Name[b]), "")
                                            val_student_emails = val_student_emails.replace("\n" + str(Student_Email[b]), "")

                                        sheet_instance.update_cell(i+2, Index+1, str(val_student_names))
                                        sheet_instance.update_cell(i+2, Index+2, str(val_student_emails))
                                        sheet_instance.update_cell(i+2, Index+3, (int(All_Events_In_Dict[i]["Currently Available:"])+1))
                                    else:
                                        print("An error has occurred when trying to drop the schedule")
                                else:
                                    pass
                    else:
                        print("An error has occured when trying to add or drop schedule")
                
        try:
            Dates.clear()
            Times.clear()
            Formatted_Times.clear()
            Total_Available.clear()
            Students_Name.clear()
            Students_Email.clear()
            Currently_Available.clear()
            Room_Number.clear()
            Informations.clear()
            Events_In_Dict.clear()

            All_Informations.clear()
            All_Events_In_Dict.clear()

            Received_Dates.clear()
            Received_Times.clear()
            Received_Total_Available.clear()
            Received_Currently_Available.clear()
            Received_student_info.clear()
            Received_Add_or_Drop.clear()
            sorted_data.clear()
        except:
            pass

        return render_template('index.html', Events = Events_In_Dict, All_Events = All_Events_In_Dict)
        
if __name__ == '__main__':
    app.run()
