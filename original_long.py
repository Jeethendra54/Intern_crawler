import time
import requests
from bs4 import BeautifulSoup
from time import sleep

Time = 0
x = 0
user_text = str(input("Enter to extract : "))
start = time.time()
html_text = requests.get('https://internshala.com/internships/'+user_text+'-internship/').text
soup = BeautifulSoup(html_text, 'lxml')
Interns = soup.find_all('div',class_='container-fluid individual_internship visibilityTrackerItem')
for Intern in Interns:
    Company_name = Intern.find('h4',class_='heading_6 company_name').text.strip()
    Role = Intern.find('div',class_='heading_4_5 profile').text.strip()
    Location = Intern.find('div',id='location_names').text.strip()
    Start_date = Intern.find('div',id='start-date-first').text.strip()
    Stipend = Intern.find('span',class_='stipend').text
    Type = Intern.find('div',class_='status status-small status-inactive').text.strip()
    Duration = Intern.find('div',class_='other_detail_item_row').text.strip().replace(' ','')
    if (Duration[57:64] == '1Month') :
        Duration = '1 Month'
    if (Duration[57:64] == '2Months') :
        Duration = '2 Months'
    if (Duration[57:64] == '3Months') :
        Duration = '3 Months'
    if (Duration[57:64] == '4Months') :
        Duration = '4 Months'
    if (Duration[57:64] == '5Months') :
        Duration = '5 Months'
    if (Duration[57:64] == '6Months') :
        Duration = '6 Months'
    if(Duration[40:47] == '1Month'):
        Duration = '1 Month'
    if(Duration[40:47] == '2Months'):
        Duration = '2 Months'
    if(Duration[40:47] == '3Months'):
        Duration = '3 Months'
    if(Duration[40:47] == '4Months'):
        Duration = '4 Months'
    if(Duration[40:47] == '5Months'):
        Duration = '5 Months'
    if(Duration[40:47] == '6Months'):
        Duration = '6 Months'
    if(Duration[57:63] == '1Week'):
        Duration = '1 Week'
    if(Duration[57:63] == '2Weeks'):
        Duration = '2 Weeks'
    if(Duration[57:63] == '3Weeks'):
        Duration = '3 Weeks'
    if(Duration[57:63] == '4Weeks'):
        Duration = '4 Weeks'
    if(Duration[57:63] == '5Weeks'):
        Duration = '5 Weeks'
    if(Duration[57:63] == '6Weeks'):
        Duration = '6 Weeks'
    if(Stipend == 'Not provided'):
        Stipend = ' Not provided'

    print()
    print("Company: {}".format(Company_name))
    sleep(Time)
    print("Role: {}".format(Role))
    sleep(Time)
    print("Location: {}".format(Location))
    sleep(Time)
    print("Start Date: {}".format(Start_date[18:29]))
    sleep(Time)
    print("Stipend:{}".format(Stipend))
    sleep(Time)
    print("Internship/Job: {}".format(Type))
    sleep(Time)
    print("Duration: {}".format(Duration))
    x=x+1


#Page-2
html_text = requests.get('https://internshala.com/internships/'+user_text+'-internship/page-2/').text
soup = BeautifulSoup(html_text, 'lxml')
Interns = soup.find_all('div',class_='container-fluid individual_internship visibilityTrackerItem')
for Intern in Interns:
    Company_name = Intern.find('div',class_='heading_6 company_name').text.strip()
    Role = Intern.find('div',class_='heading_4_5 profile').text.strip()
    Location = Intern.find('div',id='location_names').text.strip()
    Start_date = Intern.find('div',id='start-date-first').text.strip()
    Stipend = Intern.find('span',class_='stipend').text
    Type = Intern.find('div',class_='status status-small status-inactive').text.strip()
    Duration = Intern.find('div',class_='other_detail_item_row').text.strip().replace(' ','')
    if (Duration[57:64] == '1Month') :
        Duration = '1 Month'
    if (Duration[57:64] == '2Months') :
        Duration = '2 Months'
    if (Duration[57:64] == '3Months') :
        Duration = '3 Months'
    if (Duration[57:64] == '4Months') :
        Duration = '4 Months'
    if (Duration[57:64] == '5Months') :
        Duration = '5 Months'
    if (Duration[57:64] == '6Months') :
        Duration = '6 Months'
    if(Duration[40:47] == '1Month'):
        Duration = '1 Month'
    if(Duration[40:47] == '2Months'):
        Duration = '2 Months'
    if(Duration[40:47] == '3Months'):
        Duration = '3 Months'
    if(Duration[40:47] == '4Months'):
        Duration = '4 Months'
    if(Duration[40:47] == '5Months'):
        Duration = '5 Months'
    if(Duration[40:47] == '6Months'):
        Duration = '6 Months'
    if(Duration[57:63] == '1Week'):
        Duration = '1 Week'
    if(Duration[57:63] == '2Weeks'):
        Duration = '2 Weeks'
    if(Duration[57:63] == '3Weeks'):
        Duration = '3 Weeks'
    if(Duration[57:63] == '4Weeks'):
        Duration = '4 Weeks'
    if(Duration[57:63] == '5Weeks'):
        Duration = '5 Weeks'
    if(Duration[57:63] == '6Weeks'):
        Duration = '6 Weeks'

    print()
    print("Company: {}".format(Company_name))
    sleep(Time)
    print("Role: {}".format(Role))
    sleep(Time)
    print("Location: {}".format(Location))
    sleep(Time)
    print("Start Date: {}".format(Start_date[18:29]))
    sleep(Time)
    print("Stipend:{}".format(Stipend))
    sleep(Time)
    print("Internship/Job: {}".format(Type))
    sleep(Time)
    print("Duration: {}".format(Duration))
    x=x+1


#Page-3
html_text = requests.get('https://internshala.com/internships/'+user_text+'-internship/page-3/').text
soup = BeautifulSoup(html_text, 'lxml')
Interns = soup.find_all('div',class_='container-fluid individual_internship visibilityTrackerItem')
for Intern in Interns:
    Company_name = Intern.find('div',class_='heading_6 company_name').text.strip()
    Role = Intern.find('div',class_='heading_4_5 profile').text.strip()
    Location = Intern.find('div',id='location_names').text.strip()
    Start_date = Intern.find('div',id='start-date-first').text.strip()
    Stipend = Intern.find('span',class_='stipend').text
    Type = Intern.find('div',class_='status status-small status-inactive').text.strip()
    Duration = Intern.find('div',class_='other_detail_item_row').text.strip().replace(' ','')
    if (Duration[57:64] == '1Month') :
        Duration = '1 Month'
    if (Duration[57:64] == '2Months') :
        Duration = '2 Months'
    if (Duration[57:64] == '3Months') :
        Duration = '3 Months'
    if (Duration[57:64] == '4Months') :
        Duration = '4 Months'
    if (Duration[57:64] == '5Months'):
        Duration = '5 Months'
    if (Duration[57:64] == '6Months') :
        Duration = '6 Months'
    if(Duration[40:47] == '1Month'):
        Duration = '1 Month'
    if(Duration[40:47] == '2Months'):
        Duration = '2 Months'
    if(Duration[40:47] == '3Months'):
        Duration = '3 Months'
    if(Duration[40:47] == '4Months'):
        Duration = '4 Months'
    if(Duration[40:47] == '5Months'):
        Duration = '5 Months'
    if(Duration[40:47] == '6Months'):
        Duration = '6 Months'
    if(Duration[57:63] == '1Week'):
        Duration = '1 Week'
    if(Duration[57:63] == '2Weeks'):
        Duration = '2 Weeks'
    if(Duration[57:63] == '3Weeks'):
        Duration = '3 Weeks'
    if(Duration[57:63] == '4Weeks'):
        Duration = '4 Weeks'
    if(Duration[57:63] == '5Weeks'):
        Duration = '5 Weeks'
    if(Duration[57:63] == '6Weeks'):
        Duration = '6 Weeks'

    print()
    print("Company: {}".format(Company_name))
    sleep(Time)
    print("Role: {}".format(Role))
    sleep(Time)
    print("Location: {}".format(Location))
    sleep(Time)
    print("Start Date: {}".format(Start_date[18:29]))
    sleep(Time)
    print("Stipend:{}".format(Stipend))
    sleep(Time)
    print("Internship/Job: {}".format(Type))
    sleep(Time)
    print("Duration: {}".format(Duration))
    x=x+1

#Page-4
html_text = requests.get('https://internshala.com/internships/'+user_text+'-internship/page-4/').text
soup = BeautifulSoup(html_text, 'lxml')
Interns = soup.find_all('div',class_='container-fluid individual_internship visibilityTrackerItem')
for Intern in Interns:
    Company_name = Intern.find('div',class_='heading_6 company_name').text.strip()
    Role = Intern.find('div',class_='heading_4_5 profile').text.strip()
    Location = Intern.find('div',id='location_names').text.strip()
    Start_date = Intern.find('div',id='start-date-first').text.strip()
    Stipend = Intern.find('span',class_='stipend').text
    Type = Intern.find('div',class_='status status-small status-inactive').text.strip()
    Duration = Intern.find('div',class_='other_detail_item_row').text.strip().replace(' ','')
    if (Duration[57:64] == '1Month') :
        Duration = '1 Month'
    if (Duration[57:64] == '2Months') :
        Duration = '2 Months'
    if (Duration[57:64] == '3Months') :
        Duration = '3 Months'
    if (Duration[57:64] == '4Months') :
        Duration = '4 Months'
    if (Duration[57:64] == '5Months') :
        Duration = '5 Months'
    if (Duration[57:64] == '6Months') :
        Duration = '6 Months'
    if(Duration[40:47] == '1Month'):
        Duration = '1 Month'
    if(Duration[40:47] == '2Months'):
        Duration = '2 Months'
    if(Duration[40:47] == '3Months'):
        Duration = '3 Months'
    if(Duration[40:47] == '4Months'):
        Duration = '4 Months'
    if(Duration[40:47] == '5Months'):
        Duration = '5 Months'
    if(Duration[40:47] == '6Months'):
        Duration = '6 Months'
    if(Duration[57:63] == '1Week'):
        Duration = '1 Week'
    if(Duration[57:63] == '2Weeks'):
        Duration = '2 Weeks'
    if(Duration[57:63] == '3Weeks'):
        Duration = '3 Weeks'
    if(Duration[57:63] == '4Weeks'):
        Duration = '4 Weeks'
    if(Duration[57:63] == '5Weeks'):
        Duration = '5 Weeks'
    if(Duration[57:63] == '6Weeks'):
        Duration = '6 Weeks'

    print()
    print("Company: {}".format(Company_name))
    sleep(Time)
    print("Role: {}".format(Role))
    sleep(Time)
    print("Location: {}".format(Location))
    sleep(Time)
    print("Start Date: {}".format(Start_date[18:29]))
    sleep(Time)
    print("Stipend:{}".format(Stipend))
    sleep(Time)
    print("Internship/Job: {}".format(Type))
    sleep(Time)
    print("Duration: {}".format(Duration))
    x=x+1


#Page-5
html_text = requests.get('https://internshala.com/internships/'+user_text+'-internship/page-5/').text
soup = BeautifulSoup(html_text, 'lxml')
Interns = soup.find_all('div',class_='container-fluid individual_internship visibilityTrackerItem')
for Intern in Interns:
    Company_name = Intern.find('div',class_='heading_6 company_name').text.strip()
    Role = Intern.find('div',class_='heading_4_5 profile').text.strip()
    Location = Intern.find('div',id='location_names').text.strip()
    Start_date = Intern.find('div',id='start-date-first').text.strip()
    Stipend = Intern.find('span',class_='stipend').text
    Type = Intern.find('div',class_='status status-small status-inactive').text.strip()
    Duration = Intern.find('div',class_='other_detail_item_row').text.strip().replace(' ','')
    if (Duration[57:64] == '1Month') :
        Duration = '1 Month'
    if (Duration[57:64] == '2Months') :
        Duration = '2 Months'
    if (Duration[57:64] == '3Months') :
        Duration = '3 Months'
    if (Duration[57:64] == '4Months') :
        Duration = '4 Months'
    if (Duration[57:64] == '5Months') :
        Duration = '5 Months'
    if (Duration[57:64] == '6Months') :
        Duration = '6 Months'
    if(Duration[40:47] == '1Month'):
        Duration = '1 Month'
    if(Duration[40:47] == '2Months'):
        Duration = '2 Months'
    if(Duration[40:47] == '3Months'):
        Duration = '3 Months'
    if(Duration[40:47] == '4Months'):
        Duration = '4 Months'
    if(Duration[40:47] == '5Months'):
        Duration = '5 Months'
    if(Duration[40:47] == '6Months'):
        Duration = '6 Months'
    if(Duration[57:63] == '1Week'):
        Duration = '1 Week'
    if(Duration[57:63] == '2Weeks'):
        Duration = '2 Weeks'
    if(Duration[57:63] == '3Weeks'):
        Duration = '3 Weeks'
    if(Duration[57:63] == '4Weeks'):
        Duration = '4 Weeks'
    if(Duration[57:63] == '5Weeks'):
        Duration = '5 Weeks'
    if(Duration[57:63] == '6Weeks'):
        Duration = '6 Weeks'

    print()
    print("Company: {}".format(Company_name))
    sleep(Time)
    print("Role: {}".format(Role))
    sleep(Time)
    print("Location: {}".format(Location))
    sleep(Time)
    print("Start Date: {}".format(Start_date[18:29]))
    sleep(Time)
    print("Stipend:{}".format(Stipend))
    sleep(Time)
    print("Internship/Job: {}".format(Type))
    sleep(Time)
    print("Duration: {}".format(Duration))
    x=x+1


#Page-6
html_text = requests.get('https://internshala.com/internships/'+user_text+'-internship/page-6/').text
soup = BeautifulSoup(html_text, 'lxml')
Interns = soup.find_all('div',class_='container-fluid individual_internship visibilityTrackerItem')
for Intern in Interns:
    Company_name = Intern.find('div',class_='heading_6 company_name').text.strip()
    Role = Intern.find('div',class_='heading_4_5 profile').text.strip()
    Location = Intern.find('div',id='location_names').text.strip()
    Start_date = Intern.find('div',id='start-date-first').text.strip()
    Stipend = Intern.find('span',class_='stipend').text
    Type = Intern.find('div',class_='status status-small status-inactive').text.strip()
    Duration = Intern.find('div',class_='other_detail_item_row').text.strip().replace(' ','')
    if (Duration[57:64] == '1Month') :
        Duration = '1 Month'
    if (Duration[57:64] == '2Months') :
        Duration = '2 Months'
    if (Duration[57:64] == '3Months') :
        Duration = '3 Months'
    if (Duration[57:64] == '4Months') :
        Duration = '4 Months'
    if (Duration[57:64] == '5Months') :
        Duration = '5 Months'
    if (Duration[57:64] == '6Months') :
        Duration = '6 Months'
    if(Duration[40:47] == '1Month'):
        Duration = '1 Month'
    if(Duration[40:47] == '2Months'):
        Duration = '2 Months'
    if(Duration[40:47] == '3Months'):
        Duration = '3 Months'
    if(Duration[40:47] == '4Months'):
        Duration = '4 Months'
    if(Duration[40:47] == '5Months'):
        Duration = '5 Months'
    if(Duration[40:47] == '6Months'):
        Duration = '6 Months'
    if(Duration[57:63] == '1Week'):
        Duration = '1 Week'
    if(Duration[57:63] == '2Weeks'):
        Duration = '2 Weeks'
    if(Duration[57:63] == '3Weeks'):
        Duration = '3 Weeks'
    if(Duration[57:63] == '4Weeks'):
        Duration = '4 Weeks'
    if(Duration[57:63] == '5Weeks'):
        Duration = '5 Weeks'
    if(Duration[57:63] == '6Weeks'):
        Duration = '6 Weeks'

    print()
    print("Company: {}".format(Company_name))
    sleep(Time)
    print("Role: {}".format(Role))
    sleep(Time)
    print("Location: {}".format(Location))
    sleep(Time)
    print("Start Date: {}".format(Start_date[18:29]))
    sleep(Time)
    print("Stipend:{}".format(Stipend))
    sleep(Time)
    print("Internship/Job: {}".format(Type))
    sleep(Time)
    print("Duration: {}".format(Duration))
    x=x+1

#Page-7
html_text = requests.get('https://internshala.com/internships/'+user_text+'-internship/page-7/').text
soup = BeautifulSoup(html_text, 'lxml')
Interns = soup.find_all('div',class_='container-fluid individual_internship visibilityTrackerItem')
for Intern in Interns:
    Company_name = Intern.find('div',class_='heading_6 company_name').text.strip()
    Role = Intern.find('div',class_='heading_4_5 profile').text.strip()
    Location = Intern.find('div',id='location_names').text.strip()
    Start_date = Intern.find('div',id='start-date-first').text.strip()
    Stipend = Intern.find('span',class_='stipend').text
    Type = Intern.find('div',class_='status status-small status-inactive').text.strip()
    Duration = Intern.find('div',class_='other_detail_item_row').text.strip().replace(' ','')
    if (Duration[57:64] == '1Month') :
        Duration = '1 Month'
    if (Duration[57:64] == '2Months') :
        Duration = '2 Months'
    if (Duration[57:64] == '3Months') :
        Duration = '3 Months'
    if (Duration[57:64] == '4Months') :
        Duration = '4 Months'
    if (Duration[57:64] == '5Months') :
        Duration = '5 Months'
    if (Duration[57:64] == '6Months') :
        Duration = '6 Months'
    if(Duration[40:47] == '1Month'):
        Duration = '1 Month'
    if(Duration[40:47] == '2Months'):
        Duration = '2 Months'
    if(Duration[40:47] == '3Months'):
        Duration = '3 Months'
    if(Duration[40:47] == '4Months'):
        Duration = '4 Months'
    if(Duration[40:47] == '5Months'):
        Duration = '5 Months'
    if(Duration[40:47] == '6Months'):
        Duration = '6 Months'
    if(Duration[57:63] == '1Week'):
        Duration = '1 Week'
    if(Duration[57:63] == '2Weeks'):
        Duration = '2 Weeks'
    if(Duration[57:63] == '3Weeks'):
        Duration = '3 Weeks'
    if(Duration[57:63] == '4Weeks'):
        Duration = '4 Weeks'
    if(Duration[57:63] == '5Weeks'):
        Duration = '5 Weeks'
    if(Duration[57:63] == '6Weeks'):
        Duration = '6 Weeks'

    print()
    print("Company: {}".format(Company_name))
    sleep(Time)
    print("Role: {}".format(Role))
    sleep(Time)
    print("Location: {}".format(Location))
    sleep(Time)
    print("Start Date: {}".format(Start_date[18:29]))
    sleep(Time)
    print("Stipend:{}".format(Stipend))
    sleep(Time)
    print("Internship/Job: {}".format(Type))
    sleep(Time)
    print("Duration: {}".format(Duration))
    x=x+1


#Page-8
html_text = requests.get('https://internshala.com/internships/'+user_text+'-internship/page-8/').text
soup = BeautifulSoup(html_text, 'lxml')
Interns = soup.find_all('div',class_='container-fluid individual_internship visibilityTrackerItem')
for Intern in Interns:
    Company_name = Intern.find('div',class_='heading_6 company_name').text.strip()
    Role = Intern.find('div',class_='heading_4_5 profile').text.strip()
    Location = Intern.find('div',id='location_names').text.strip()
    Start_date = Intern.find('div',id='start-date-first').text.strip()
    Stipend = Intern.find('span',class_='stipend').text
    Type = Intern.find('div',class_='status status-small status-inactive').text.strip()
    Duration = Intern.find('div',class_='other_detail_item_row').text.strip().replace(' ','')
    if (Duration[57:64] == '1Month') :
        Duration = '1 Month'
    if (Duration[57:64] == '2Months') :
        Duration = '2 Months'
    if (Duration[57:64] == '3Months') :
        Duration = '3 Months'
    if (Duration[57:64] == '4Months') :
        Duration = '4 Months'
    if (Duration[57:64] == '5Months') :
        Duration = '5 Months'
    if (Duration[57:64] == '6Months') :
        Duration = '6 Months'
    if(Duration[40:47] == '1Month'):
        Duration = '1 Month'
    if(Duration[40:47] == '2Months'):
        Duration = '2 Months'
    if(Duration[40:47] == '3Months'):
        Duration = '3 Months'
    if(Duration[40:47] == '4Months'):
        Duration = '4 Months'
    if(Duration[40:47] == '5Months'):
        Duration = '5 Months'
    if(Duration[40:47] == '6Months'):
        Duration = '6 Months'
    if(Duration[57:63] == '1Week'):
        Duration = '1 Week'
    if(Duration[57:63] == '2Weeks'):
        Duration = '2 Weeks'
    if(Duration[57:63] == '3Weeks'):
        Duration = '3 Weeks'
    if(Duration[57:63] == '4Weeks'):
        Duration = '4 Weeks'
    if(Duration[57:63] == '5Weeks'):
        Duration = '5 Weeks'
    if(Duration[57:63] == '6Weeks'):
        Duration = '6 Weeks'

    print()
    print("Company: {}".format(Company_name))
    sleep(Time)
    print("Role: {}".format(Role))
    sleep(Time)
    print("Location: {}".format(Location))
    sleep(Time)
    print("Start Date: {}".format(Start_date[18:29]))
    sleep(Time)
    print("Stipend:{}".format(Stipend))
    sleep(Time)
    print("Internship/Job: {}".format(Type))
    sleep(Time)
    print("Duration: {}".format(Duration))
    x=x+1


#Page-9
html_text = requests.get('https://internshala.com/internships/'+user_text+'-internship/page-9/').text
soup = BeautifulSoup(html_text, 'lxml')
Interns = soup.find_all('div',class_='container-fluid individual_internship visibilityTrackerItem')
for Intern in Interns:
    Company_name = Intern.find('div',class_='heading_6 company_name').text.strip()
    Role = Intern.find('div',class_='heading_4_5 profile').text.strip()
    Location = Intern.find('div',id='location_names').text.strip()
    Start_date = Intern.find('div',id='start-date-first').text.strip()
    Stipend = Intern.find('span',class_='stipend').text
    Type = Intern.find('div',class_='status status-small status-inactive').text.strip()
    Duration = Intern.find('div',class_='other_detail_item_row').text.strip().replace(' ','')
    if (Duration[57:64] == '1Month') :
        Duration = '1 Month'
    if (Duration[57:64] == '2Months') :
        Duration = '2 Months'
    if (Duration[57:64] == '3Months') :
        Duration = '3 Months'
    if (Duration[57:64] == '4Months') :
        Duration = '4 Months'
    if (Duration[57:64] == '5Months') :
        Duration = '5 Months'
    if (Duration[57:64] == '6Months') :
        Duration = '6 Months'
    if(Duration[40:47] == '1Month'):
        Duration = '1 Month'
    if(Duration[40:47] == '2Months'):
        Duration = '2 Months'
    if(Duration[40:47] == '3Months'):
        Duration = '3 Months'
    if(Duration[40:47] == '4Months'):
        Duration = '4 Months'
    if(Duration[40:47] == '5Months'):
        Duration = '5 Months'
    if(Duration[40:47] == '6Months'):
        Duration = '6 Months'
    if(Duration[57:63] == '1Week'):
        Duration = '1 Week'
    if(Duration[57:63] == '2Weeks'):
        Duration = '2 Weeks'
    if(Duration[57:63] == '3Weeks'):
        Duration = '3 Weeks'
    if(Duration[57:63] == '4Weeks'):
        Duration = '4 Weeks'
    if(Duration[57:63] == '5Weeks'):
        Duration = '5 Weeks'
    if(Duration[57:63] == '6Weeks'):
        Duration = '6 Weeks'

    print()
    print("Company: {}".format(Company_name))
    sleep(Time)
    print("Role: {}".format(Role))
    sleep(Time)
    print("Location: {}".format(Location))
    sleep(Time)
    print("Start Date: {}".format(Start_date[18:29]))
    sleep(Time)
    print("Stipend:{}".format(Stipend))
    sleep(Time)
    print("Internship/Job: {}".format(Type))
    sleep(Time)
    print("Duration: {}".format(Duration))
    x=x+1

#Page-10
html_text = requests.get('https://internshala.com/internships/'+user_text+'-internship/page-10/').text
soup = BeautifulSoup(html_text, 'lxml')
Interns = soup.find_all('div',class_='container-fluid individual_internship visibilityTrackerItem')
for Intern in Interns:
    Company_name = Intern.find('div',class_='heading_6 company_name').text.strip()
    Role = Intern.find('div',class_='heading_4_5 profile').text.strip()
    Location = Intern.find('div',id='location_names').text.strip()
    Start_date = Intern.find('div',id='start-date-first').text.strip()
    Stipend = Intern.find('span',class_='stipend').text
    Type = Intern.find('div',class_='status status-small status-inactive').text.strip()
    Duration = Intern.find('div',class_='other_detail_item_row').text.strip().replace(' ','')
    if (Duration[57:64] == '1Month') :
        Duration = '1 Month'
    if (Duration[57:64] == '2Months') :
        Duration = '2 Months'
    if (Duration[57:64] == '3Months') :
        Duration = '3 Months'
    if (Duration[57:64] == '4Months') :
        Duration = '4 Months'
    if (Duration[57:64] == '5Months') :
        Duration = '5 Months'
    if (Duration[57:64] == '6Months') :
        Duration = '6 Months'
    if(Duration[40:47] == '1Month'):
        Duration = '1 Month'
    if(Duration[40:47] == '2Months'):
        Duration = '2 Months'
    if(Duration[40:47] == '3Months'):
        Duration = '3 Months'
    if(Duration[40:47] == '4Months'):
        Duration = '4 Months'
    if(Duration[40:47] == '5Months'):
        Duration = '5 Months'
    if(Duration[40:47] == '6Months'):
        Duration = '6 Months'
    if(Duration[57:63] == '1Week'):
        Duration = '1 Week'
    if(Duration[57:63] == '2Weeks'):
        Duration = '2 Weeks'
    if(Duration[57:63] == '3Weeks'):
        Duration = '3 Weeks'
    if(Duration[57:63] == '4Weeks'):
        Duration = '4 Weeks'
    if(Duration[57:63] == '5Weeks'):
        Duration = '5 Weeks'
    if(Duration[57:63] == '6Weeks'):
        Duration = '6 Weeks'

    print()
    print("Company: {}".format(Company_name))
    sleep(Time)
    print("Role: {}".format(Role))
    sleep(Time)
    print("Location: {}".format(Location))
    sleep(Time)
    print("Start Date: {}".format(Start_date[18:29]))
    sleep(Time)
    print("Stipend:{}".format(Stipend))
    sleep(Time)
    print("Internship/Job: {}".format(Type))
    sleep(Time)
    print("Duration: {}".format(Duration))
    x=x+1


#Page-11
html_text = requests.get('https://internshala.com/internships/'+user_text+'-internship/page-11/').text
soup = BeautifulSoup(html_text, 'lxml')
Interns = soup.find_all('div',class_='container-fluid individual_internship visibilityTrackerItem')
for Intern in Interns:
    Company_name = Intern.find('div',class_='heading_6 company_name').text.strip()
    Role = Intern.find('div',class_='heading_4_5 profile').text.strip()
    Location = Intern.find('div',id='location_names').text.strip()
    Start_date = Intern.find('div',id='start-date-first').text.strip()
    Stipend = Intern.find('span',class_='stipend').text
    Type = Intern.find('div',class_='status status-small status-inactive').text.strip()
    Duration = Intern.find('div',class_='other_detail_item_row').text.strip().replace(' ','')
    if (Duration[57:64] == '1Month') :
        Duration = '1 Month'
    if (Duration[57:64] == '2Months') :
        Duration = '2 Months'
    if (Duration[57:64] == '3Months') :
        Duration = '3 Months'
    if (Duration[57:64] == '4Months') :
        Duration = '4 Months'
    if (Duration[57:64] == '5Months') :
        Duration = '5 Months'
    if (Duration[57:64] == '6Months') :
        Duration = '6 Months'
    if(Duration[40:47] == '1Month'):
        Duration = '1 Month'
    if(Duration[40:47] == '2Months'):
        Duration = '2 Months'
    if(Duration[40:47] == '3Months'):
        Duration = '3 Months'
    if(Duration[40:47] == '4Months'):
        Duration = '4 Months'
    if(Duration[40:47] == '5Months'):
        Duration = '5 Months'
    if(Duration[40:47] == '6Months'):
        Duration = '6 Months'
    if(Duration[57:63] == '1Week'):
        Duration = '1 Week'
    if(Duration[57:63] == '2Weeks'):
        Duration = '2 Weeks'
    if(Duration[57:63] == '3Weeks'):
        Duration = '3 Weeks'
    if(Duration[57:63] == '4Weeks'):
        Duration = '4 Weeks'
    if(Duration[57:63] == '5Weeks'):
        Duration = '5 Weeks'
    if(Duration[57:63] == '6Weeks'):
        Duration = '6 Weeks'

    print()
    print("Company: {}".format(Company_name))
    sleep(Time)
    print("Role: {}".format(Role))
    sleep(Time)
    print("Location: {}".format(Location))
    sleep(Time)
    print("Start Date: {}".format(Start_date[18:29]))
    sleep(Time)
    print("Stipend:{}".format(Stipend))
    sleep(Time)
    print("Internship/Job: {}".format(Type))
    sleep(Time)
    print("Duration: {}".format(Duration))
    x=x+1


#Page-12
html_text = requests.get('https://internshala.com/internships/'+user_text+'-internship/page-12/').text
soup = BeautifulSoup(html_text, 'lxml')
Interns = soup.find_all('div',class_='container-fluid individual_internship visibilityTrackerItem')
for Intern in Interns:
    Company_name = Intern.find('div',class_='heading_6 company_name').text.strip()
    Role = Intern.find('div',class_='heading_4_5 profile').text.strip()
    Location = Intern.find('div',id='location_names').text.strip()
    Start_date = Intern.find('div',id='start-date-first').text.strip()
    Stipend = Intern.find('span',class_='stipend').text
    Type = Intern.find('div',class_='status status-small status-inactive').text.strip()
    Duration = Intern.find('div',class_='other_detail_item_row').text.strip().replace(' ','')
    if (Duration[57:64] == '1Month') :
        Duration = '1 Month'
    if (Duration[57:64] == '2Months') :
        Duration = '2 Months'
    if (Duration[57:64] == '3Months') :
        Duration = '3 Months'
    if (Duration[57:64] == '4Months') :
        Duration = '4 Months'
    if (Duration[57:64] == '5Months') :
        Duration = '5 Months'
    if (Duration[57:64] == '6Months') :
        Duration = '6 Months'
    if(Duration[40:47] == '1Month'):
        Duration = '1 Month'
    if(Duration[40:47] == '2Months'):
        Duration = '2 Months'
    if(Duration[40:47] == '3Months'):
        Duration = '3 Months'
    if(Duration[40:47] == '4Months'):
        Duration = '4 Months'
    if(Duration[40:47] == '5Months'):
        Duration = '5 Months'
    if(Duration[40:47] == '6Months'):
        Duration = '6 Months'
    if(Duration[57:63] == '1Week'):
        Duration = '1 Week'
    if(Duration[57:63] == '2Weeks'):
        Duration = '2 Weeks'
    if(Duration[57:63] == '3Weeks'):
        Duration = '3 Weeks'
    if(Duration[57:63] == '4Weeks'):
        Duration = '4 Weeks'
    if(Duration[57:63] == '5Weeks'):
        Duration = '5 Weeks'
    if(Duration[57:63] == '6Weeks'):
        Duration = '6 Weeks'

    print()
    print("Company: {}".format(Company_name))
    sleep(Time)
    print("Role: {}".format(Role))
    sleep(Time)
    print("Location: {}".format(Location))
    sleep(Time)
    print("Start Date: {}".format(Start_date[18:29]))
    sleep(Time)
    print("Stipend:{}".format(Stipend))
    sleep(Time)
    print("Internship/Job: {}".format(Type))
    sleep(Time)
    print("Duration: {}".format(Duration))
    x=x+1

#Page-13
html_text = requests.get('https://internshala.com/internships/'+user_text+'-internship/page-13/').text
soup = BeautifulSoup(html_text, 'lxml')
Interns = soup.find_all('div',class_='container-fluid individual_internship visibilityTrackerItem')
for Intern in Interns:
    Company_name = Intern.find('div',class_='heading_6 company_name').text.strip()
    Role = Intern.find('div',class_='heading_4_5 profile').text.strip()
    Location = Intern.find('div',id='location_names').text.strip()
    Start_date = Intern.find('div',id='start-date-first').text.strip()
    Stipend = Intern.find('span',class_='stipend').text
    Type = Intern.find('div',class_='status status-small status-inactive').text.strip()
    Duration = Intern.find('div',class_='other_detail_item_row').text.strip().replace(' ','')
    if (Duration[57:64] == '1Month') :
        Duration = '1 Month'
    if (Duration[57:64] == '2Months') :
        Duration = '2 Months'
    if (Duration[57:64] == '3Months') :
        Duration = '3 Months'
    if (Duration[57:64] == '4Months') :
        Duration = '4 Months'
    if (Duration[57:64] == '5Months') :
        Duration = '5 Months'
    if (Duration[57:64] == '6Months') :
        Duration = '6 Months'
    if(Duration[40:47] == '1Month'):
        Duration = '1 Month'
    if(Duration[40:47] == '2Months'):
        Duration = '2 Months'
    if(Duration[40:47] == '3Months'):
        Duration = '3 Months'
    if(Duration[40:47] == '4Months'):
        Duration = '4 Months'
    if(Duration[40:47] == '5Months'):
        Duration = '5 Months'
    if(Duration[40:47] == '6Months'):
        Duration = '6 Months'
    if(Duration[57:63] == '1Week'):
        Duration = '1 Week'
    if(Duration[57:63] == '2Weeks'):
        Duration = '2 Weeks'
    if(Duration[57:63] == '3Weeks'):
        Duration = '3 Weeks'
    if(Duration[57:63] == '4Weeks'):
        Duration = '4 Weeks'
    if(Duration[57:63] == '5Weeks'):
        Duration = '5 Weeks'
    if(Duration[57:63] == '6Weeks'):
        Duration = '6 Weeks'

    print()
    print("Company: {}".format(Company_name))
    sleep(Time)
    print("Role: {}".format(Role))
    sleep(Time)
    print("Location: {}".format(Location))
    sleep(Time)
    print("Start Date: {}".format(Start_date[18:29]))
    sleep(Time)
    print("Stipend:{}".format(Stipend))
    sleep(Time)
    print("Internship/Job: {}".format(Type))
    sleep(Time)
    print("Duration: {}".format(Duration))
    x=x+1

#Page-14
html_text = requests.get('https://internshala.com/internships/'+user_text+'-internship/page-14/').text
soup = BeautifulSoup(html_text, 'lxml')
Interns = soup.find_all('div',class_='container-fluid individual_internship visibilityTrackerItem')
for Intern in Interns:
    Company_name = Intern.find('div',class_='heading_6 company_name').text.strip()
    Role = Intern.find('div',class_='heading_4_5 profile').text.strip()
    Location = Intern.find('div',id='location_names').text.strip()
    Start_date = Intern.find('div',id='start-date-first').text.strip()
    Stipend = Intern.find('span',class_='stipend').text
    Type = Intern.find('div',class_='status status-small status-inactive').text.strip()
    Duration = Intern.find('div',class_='other_detail_item_row').text.strip().replace(' ','')
    if (Duration[57:64] == '1Month') :
        Duration = '1 Month'
    if (Duration[57:64] == '2Months') :
        Duration = '2 Months'
    if (Duration[57:64] == '3Months') :
        Duration = '3 Months'
    if (Duration[57:64] == '4Months') :
        Duration = '4 Months'
    if (Duration[57:64] == '5Months') :
        Duration = '5 Months'
    if (Duration[57:64] == '6Months') :
        Duration = '6 Months'
    if(Duration[40:47] == '1Month'):
        Duration = '1 Month'
    if(Duration[40:47] == '2Months'):
        Duration = '2 Months'
    if(Duration[40:47] == '3Months'):
        Duration = '3 Months'
    if(Duration[40:47] == '4Months'):
        Duration = '4 Months'
    if(Duration[40:47] == '5Months'):
        Duration = '5 Months'
    if(Duration[40:47] == '6Months'):
        Duration = '6 Months'
    if(Duration[57:63] == '1Week'):
        Duration = '1 Week'
    if(Duration[57:63] == '2Weeks'):
        Duration = '2 Weeks'
    if(Duration[57:63] == '3Weeks'):
        Duration = '3 Weeks'
    if(Duration[57:63] == '4Weeks'):
        Duration = '4 Weeks'
    if(Duration[57:63] == '5Weeks'):
        Duration = '5 Weeks'
    if(Duration[57:63] == '6Weeks'):
        Duration = '6 Weeks'

    print()
    print("Company: {}".format(Company_name))
    sleep(Time)
    print("Role: {}".format(Role))
    sleep(Time)
    print("Location: {}".format(Location))
    sleep(Time)
    print("Start Date: {}".format(Start_date[18:29]))
    sleep(Time)
    print("Stipend:{}".format(Stipend))
    sleep(Time)
    print("Internship/Job: {}".format(Type))
    sleep(Time)
    print("Duration: {}".format(Duration))
    x=x+1


#Page-15
html_text = requests.get('https://internshala.com/internships/'+user_text+'-internship/page-15/').text
soup = BeautifulSoup(html_text, 'lxml')
Interns = soup.find_all('div',class_='container-fluid individual_internship visibilityTrackerItem')
for Intern in Interns:
    Company_name = Intern.find('div',class_='heading_6 company_name').text.strip()
    Role = Intern.find('div',class_='heading_4_5 profile').text.strip()
    Location = Intern.find('div',id='location_names').text.strip()
    Start_date = Intern.find('div',id='start-date-first').text.strip()
    Stipend = Intern.find('span',class_='stipend').text
    Type = Intern.find('div',class_='status status-small status-inactive').text.strip()
    Duration = Intern.find('div',class_='other_detail_item_row').text.strip().replace(' ','')
    if (Duration[57:64] == '1Month') :
        Duration = '1 Month'
    if (Duration[57:64] == '2Months') :
        Duration = '2 Months'
    if (Duration[57:64] == '3Months') :
        Duration = '3 Months'
    if (Duration[57:64] == '4Months') :
        Duration = '4 Months'
    if (Duration[57:64] == '5Months') :
        Duration = '5 Months'
    if (Duration[57:64] == '6Months') :
        Duration = '6 Months'
    if(Duration[40:47] == '1Month'):
        Duration = '1 Month'
    if(Duration[40:47] == '2Months'):
        Duration = '2 Months'
    if(Duration[40:47] == '3Months'):
        Duration = '3 Months'
    if(Duration[40:47] == '4Months'):
        Duration = '4 Months'
    if(Duration[40:47] == '5Months'):
        Duration = '5 Months'
    if(Duration[40:47] == '6Months'):
        Duration = '6 Months'
    if(Duration[57:63] == '1Week'):
        Duration = '1 Week'
    if(Duration[57:63] == '2Weeks'):
        Duration = '2 Weeks'
    if(Duration[57:63] == '3Weeks'):
        Duration = '3 Weeks'
    if(Duration[57:63] == '4Weeks'):
        Duration = '4 Weeks'
    if(Duration[57:63] == '5Weeks'):
        Duration = '5 Weeks'
    if(Duration[57:63] == '6Weeks'):
        Duration = '6 Weeks'

    print()
    print("Company: {}".format(Company_name))
    sleep(Time)
    print("Role: {}".format(Role))
    sleep(Time)
    print("Location: {}".format(Location))
    sleep(Time)
    print("Start Date: {}".format(Start_date[18:29]))
    sleep(Time)
    print("Stipend:{}".format(Stipend))
    sleep(Time)
    print("Internship/Job: {}".format(Type))
    sleep(Time)
    print("Duration: {}".format(Duration))
    x=x+1

#Page-16
html_text = requests.get('https://internshala.com/internships/'+user_text+'-internship/page-16/').text
soup = BeautifulSoup(html_text, 'lxml')
Interns = soup.find_all('div',class_='container-fluid individual_internship visibilityTrackerItem')
for Intern in Interns:
    Company_name = Intern.find('div',class_='heading_6 company_name').text.strip()
    Role = Intern.find('div',class_='heading_4_5 profile').text.strip()
    Location = Intern.find('div',id='location_names').text.strip()
    Start_date = Intern.find('div',id='start-date-first').text.strip()
    Stipend = Intern.find('span',class_='stipend').text
    Type = Intern.find('div',class_='status status-small status-inactive').text.strip()
    Duration = Intern.find('div',class_='other_detail_item_row').text.strip().replace(' ','')
    if (Duration[57:64] == '1Month') :
        Duration = '1 Month'
    if (Duration[57:64] == '2Months') :
        Duration = '2 Months'
    if (Duration[57:64] == '3Months') :
        Duration = '3 Months'
    if (Duration[57:64] == '4Months') :
        Duration = '4 Months'
    if (Duration[57:64] == '5Months') :
        Duration = '5 Months'
    if (Duration[57:64] == '6Months') :
        Duration = '6 Months'
    if(Duration[40:47] == '1Month'):
        Duration = '1 Month'
    if(Duration[40:47] == '2Months'):
        Duration = '2 Months'
    if(Duration[40:47] == '3Months'):
        Duration = '3 Months'
    if(Duration[40:47] == '4Months'):
        Duration = '4 Months'
    if(Duration[40:47] == '5Months'):
        Duration = '5 Months'
    if(Duration[40:47] == '6Months'):
        Duration = '6 Months'
    if(Duration[57:63] == '1Week'):
        Duration = '1 Week'
    if(Duration[57:63] == '2Weeks'):
        Duration = '2 Weeks'
    if(Duration[57:63] == '3Weeks'):
        Duration = '3 Weeks'
    if(Duration[57:63] == '4Weeks'):
        Duration = '4 Weeks'
    if(Duration[57:63] == '5Weeks'):
        Duration = '5 Weeks'
    if(Duration[57:63] == '6Weeks'):
        Duration = '6 Weeks'

    print()
    print("Company: {}".format(Company_name))
    sleep(Time)
    print("Role: {}".format(Role))
    sleep(Time)
    print("Location: {}".format(Location))
    sleep(Time)
    print("Start Date: {}".format(Start_date[18:29]))
    sleep(Time)
    print("Stipend:{}".format(Stipend))
    sleep(Time)
    print("Internship/Job: {}".format(Type))
    sleep(Time)
    print("Duration: {}".format(Duration))
    x=x+1


#Page-17
html_text = requests.get('https://internshala.com/internships/'+user_text+'-internship/page-17/').text
soup = BeautifulSoup(html_text, 'lxml')
Interns = soup.find_all('div',class_='container-fluid individual_internship visibilityTrackerItem')
for Intern in Interns:
    Company_name = Intern.find('div',class_='heading_6 company_name').text.strip()
    Role = Intern.find('div',class_='heading_4_5 profile').text.strip()
    Location = Intern.find('div',id='location_names').text.strip()
    Start_date = Intern.find('div',id='start-date-first').text.strip()
    Stipend = Intern.find('span',class_='stipend').text
    Type = Intern.find('div',class_='status status-small status-inactive').text.strip()
    Duration = Intern.find('div',class_='other_detail_item_row').text.strip().replace(' ','')
    if (Duration[57:64] == '1Month') :
        Duration = '1 Month'
    if (Duration[57:64] == '2Months') :
        Duration = '2 Months'
    if (Duration[57:64] == '3Months') :
        Duration = '3 Months'
    if (Duration[57:64] == '4Months') :
        Duration = '4 Months'
    if (Duration[57:64] == '5Months') :
        Duration = '5 Months'
    if (Duration[57:64] == '6Months') :
        Duration = '6 Months'
    if(Duration[40:47] == '1Month'):
        Duration = '1 Month'
    if(Duration[40:47] == '2Months'):
        Duration = '2 Months'
    if(Duration[40:47] == '3Months'):
        Duration = '3 Months'
    if(Duration[40:47] == '4Months'):
        Duration = '4 Months'
    if(Duration[40:47] == '5Months'):
        Duration = '5 Months'
    if(Duration[40:47] == '6Months'):
        Duration = '6 Months'
    if(Duration[57:63] == '1Week'):
        Duration = '1 Week'
    if(Duration[57:63] == '2Weeks'):
        Duration = '2 Weeks'
    if(Duration[57:63] == '3Weeks'):
        Duration = '3 Weeks'
    if(Duration[57:63] == '4Weeks'):
        Duration = '4 Weeks'
    if(Duration[57:63] == '5Weeks'):
        Duration = '5 Weeks'
    if(Duration[57:63] == '6Weeks'):
        Duration = '6 Weeks'

    print()
    print("Company: {}".format(Company_name))
    sleep(Time)
    print("Role: {}".format(Role))
    sleep(Time)
    print("Location: {}".format(Location))
    sleep(Time)
    print("Start Date: {}".format(Start_date[18:29]))
    sleep(Time)
    print("Stipend:{}".format(Stipend))
    sleep(Time)
    print("Internship/Job: {}".format(Type))
    sleep(Time)
    print("Duration: {}".format(Duration))
    x=x+1

#Page-18
html_text = requests.get('https://internshala.com/internships/'+user_text+'-internship/page-18/').text
soup = BeautifulSoup(html_text, 'lxml')
Interns = soup.find_all('div',class_='container-fluid individual_internship visibilityTrackerItem')
for Intern in Interns:
    Company_name = Intern.find('div',class_='heading_6 company_name').text.strip()
    Role = Intern.find('div',class_='heading_4_5 profile').text.strip()
    Location = Intern.find('div',id='location_names').text.strip()
    Start_date = Intern.find('div',id='start-date-first').text.strip()
    Stipend = Intern.find('span',class_='stipend').text
    Type = Intern.find('div',class_='status status-small status-inactive').text.strip()
    Duration = Intern.find('div',class_='other_detail_item_row').text.strip().replace(' ','')
    if (Duration[57:64] == '1Month') :
        Duration = '1 Month'
    if (Duration[57:64] == '2Months') :
        Duration = '2 Months'
    if (Duration[57:64] == '3Months') :
        Duration = '3 Months'
    if (Duration[57:64] == '4Months') :
        Duration = '4 Months'
    if (Duration[57:64] == '5Months') :
        Duration = '5 Months'
    if (Duration[57:64] == '6Months') :
        Duration = '6 Months'
    if(Duration[40:47] == '1Month'):
        Duration = '1 Month'
    if(Duration[40:47] == '2Months'):
        Duration = '2 Months'
    if(Duration[40:47] == '3Months'):
        Duration = '3 Months'
    if(Duration[40:47] == '4Months'):
        Duration = '4 Months'
    if(Duration[40:47] == '5Months'):
        Duration = '5 Months'
    if(Duration[40:47] == '6Months'):
        Duration = '6 Months'
    if(Duration[57:63] == '1Week'):
        Duration = '1 Week'
    if(Duration[57:63] == '2Weeks'):
        Duration = '2 Weeks'
    if(Duration[57:63] == '3Weeks'):
        Duration = '3 Weeks'
    if(Duration[57:63] == '4Weeks'):
        Duration = '4 Weeks'
    if(Duration[57:63] == '5Weeks'):
        Duration = '5 Weeks'
    if(Duration[57:63] == '6Weeks'):
        Duration = '6 Weeks'

    print()
    print("Company: {}".format(Company_name))
    sleep(Time)
    print("Role: {}".format(Role))
    sleep(Time)
    print("Location: {}".format(Location))
    sleep(Time)
    print("Start Date: {}".format(Start_date[18:29]))
    sleep(Time)
    print("Stipend:{}".format(Stipend))
    sleep(Time)
    print("Internship/Job: {}".format(Type))
    sleep(Time)
    print("Duration: {}".format(Duration))
    x=x+1


#Page-19
html_text = requests.get('https://internshala.com/internships/'+user_text+'-internship/page-19/').text
soup = BeautifulSoup(html_text, 'lxml')
Interns = soup.find_all('div',class_='container-fluid individual_internship visibilityTrackerItem')
for Intern in Interns:
    Company_name = Intern.find('div',class_='heading_6 company_name').text.strip()
    Role = Intern.find('div',class_='heading_4_5 profile').text.strip()
    Location = Intern.find('div',id='location_names').text.strip()
    Start_date = Intern.find('div',id='start-date-first').text.strip()
    Stipend = Intern.find('span',class_='stipend').text
    Type = Intern.find('div',class_='status status-small status-inactive').text.strip()
    Duration = Intern.find('div',class_='other_detail_item_row').text.strip().replace(' ','')
    if (Duration[57:64] == '1Month') :
        Duration = '1 Month'
    if (Duration[57:64] == '2Months') :
        Duration = '2 Months'
    if (Duration[57:64] == '3Months') :
        Duration = '3 Months'
    if (Duration[57:64] == '4Months') :
        Duration = '4 Months'
    if (Duration[57:64] == '5Months') :
        Duration = '5 Months'
    if (Duration[57:64] == '6Months') :
        Duration = '6 Months'
    if(Duration[40:47] == '1Month'):
        Duration = '1 Month'
    if(Duration[40:47] == '2Months'):
        Duration = '2 Months'
    if(Duration[40:47] == '3Months'):
        Duration = '3 Months'
    if(Duration[40:47] == '4Months'):
        Duration = '4 Months'
    if(Duration[40:47] == '5Months'):
        Duration = '5 Months'
    if(Duration[40:47] == '6Months'):
        Duration = '6 Months'
    if(Duration[57:63] == '1Week'):
        Duration = '1 Week'
    if(Duration[57:63] == '2Weeks'):
        Duration = '2 Weeks'
    if(Duration[57:63] == '3Weeks'):
        Duration = '3 Weeks'
    if(Duration[57:63] == '4Weeks'):
        Duration = '4 Weeks'
    if(Duration[57:63] == '5Weeks'):
        Duration = '5 Weeks'
    if(Duration[57:63] == '6Weeks'):
        Duration = '6 Weeks'

    print()
    print("Company: {}".format(Company_name))
    sleep(Time)
    print("Role: {}".format(Role))
    sleep(Time)
    print("Location: {}".format(Location))
    sleep(Time)
    print("Start Date: {}".format(Start_date[18:29]))
    sleep(Time)
    print("Stipend:{}".format(Stipend))
    sleep(Time)
    print("Internship/Job: {}".format(Type))
    sleep(Time)
    print("Duration: {}".format(Duration))
    x=x+1

#Page-20
html_text = requests.get('https://internshala.com/internships/'+user_text+'-internship/page-20/').text
soup = BeautifulSoup(html_text, 'lxml')
Interns = soup.find_all('div',class_='container-fluid individual_internship visibilityTrackerItem')
for Intern in Interns:
    Company_name = Intern.find('div',class_='heading_6 company_name').text.strip()
    Role = Intern.find('div',class_='heading_4_5 profile').text.strip()
    Location = Intern.find('div',id='location_names').text.strip()
    Start_date = Intern.find('div',id='start-date-first').text.strip()
    Stipend = Intern.find('span',class_='stipend').text
    Type = Intern.find('div',class_='status status-small status-inactive').text.strip()
    Duration = Intern.find('div',class_='other_detail_item_row').text.strip().replace(' ','')
    if (Duration[57:64] == '1Month') :
        Duration = '1 Month'
    if (Duration[57:64] == '2Months') :
        Duration = '2 Months'
    if (Duration[57:64] == '3Months') :
        Duration = '3 Months'
    if (Duration[57:64] == '4Months') :
        Duration = '4 Months'
    if (Duration[57:64] == '5Months') :
        Duration = '5 Months'
    if (Duration[57:64] == '6Months') :
        Duration = '6 Months'
    if(Duration[40:47] == '1Month'):
        Duration = '1 Month'
    if(Duration[40:47] == '2Months'):
        Duration = '2 Months'
    if(Duration[40:47] == '3Months'):
        Duration = '3 Months'
    if(Duration[40:47] == '4Months'):
        Duration = '4 Months'
    if(Duration[40:47] == '5Months'):
        Duration = '5 Months'
    if(Duration[40:47] == '6Months'):
        Duration = '6 Months'
    if(Duration[57:63] == '1Week'):
        Duration = '1 Week'
    if(Duration[57:63] == '2Weeks'):
        Duration = '2 Weeks'
    if(Duration[57:63] == '3Weeks'):
        Duration = '3 Weeks'
    if(Duration[57:63] == '4Weeks'):
        Duration = '4 Weeks'
    if(Duration[57:63] == '5Weeks'):
        Duration = '5 Weeks'
    if(Duration[57:63] == '6Weeks'):
        Duration = '6 Weeks'
    if(Stipend == 'Not provided'):
        Stipend = ' Not provided'

    print()
    print("Company: {}".format(Company_name))
    sleep(Time)
    print("Role: {}".format(Role))
    sleep(Time)
    print("Location: {}".format(Location))
    sleep(Time)
    print("Start Date: {}".format(Start_date[18:29]))
    sleep(Time)
    print("Stipend:{}".format(Stipend))
    sleep(Time)
    print("Internship/Job: {}".format(Type))
    sleep(Time)
    x=x+1

#page-21
html_text = requests.get('https://internshala.com/internships/'+user_text+'-internship/page-21/').text
soup = BeautifulSoup(html_text, 'lxml')
Interns = soup.find_all('div',class_='container-fluid individual_internship visibilityTrackerItem')
for Intern in Interns:
    Company_name = Intern.find('div',class_='heading_6 company_name').text.strip()
    Role = Intern.find('div',class_='heading_4_5 profile').text.strip()
    Location = Intern.find('div',id='location_names').text.strip()
    Start_date = Intern.find('div',id='start-date-first').text.strip()
    Stipend = Intern.find('span',class_='stipend').text
    Type = Intern.find('div',class_='status status-small status-inactive').text.strip()
    Duration = Intern.find('div',class_='other_detail_item_row').text.strip().replace(' ','')
    if (Duration[57:64] == '1Month') :
        Duration = '1 Month'
    if (Duration[57:64] == '2Months') :
        Duration = '2 Months'
    if (Duration[57:64] == '3Months') :
        Duration = '3 Months' 
    if (Duration[57:64] == '4Months') :
        Duration = '4 Months'
    if (Duration[57:64] == '5Months') :
        Duration = '5 Months'
    if (Duration[57:64] == '6Months') :
        Duration = '6 Months'
    if(Duration[40:47] == '1Month'):
        Duration = '1 Month'
    if(Duration[40:47] == '2Months'):
        Duration = '2 Months'
    if(Duration[40:47] == '3Months'):
        Duration = '3 Months'
    if(Duration[40:47] == '4Months'):
        Duration = '4 Months'
    if(Duration[40:47] == '5Months'):
        Duration = '5 Months'
    if(Duration[40:47] == '6Months'):
        Duration = '6 Months'
    if(Duration[57:63] == '1Week'):
        Duration = '1 Week'
    if(Duration[57:63] == '2Weeks'):
        Duration = '2 Weeks'
    if(Duration[57:63] == '3Weeks'):
        Duration = '3 Weeks'
    if(Duration[57:63] == '4Weeks'):
        Duration = '4 Weeks'
    if(Duration[57:63] == '5Weeks'):
        Duration = '5 Weeks'
    if(Duration[57:63] == '6Weeks'):
        Duration = '6 Weeks'
    if(Stipend == 'Not provided'):
        Stipend = ' Not provided'

    print()
    print("Company: {}".format(Company_name))
    sleep(Time)
    print("Role: {}".format(Role))
    sleep(Time)
    print("Location: {}".format(Location))
    sleep(Time)
    print("Start Date: {}".format(Start_date[18:29]))
    sleep(Time)
    print("Stipend:{}".format(Stipend))
    sleep(Time)
    print("Internship/Job: {}".format(Type))
    sleep(Time)
    x=x+1

print()
print("No of companies scraped : {}".format(x))
end = time.time()
elapsed_time = end - start
minutes = elapsed_time/60
print("Elapsed time : {} seconds".format(elapsed_time))
print("Elapsed time : {} minutes".format(minutes))