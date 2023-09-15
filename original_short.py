import requests
from bs4 import BeautifulSoup
from time import sleep
import time
 
Time  = 0.01
x = 0
user_text = str(input("Enter a Tech stack to extract : "))
start = time.time() 
temp = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']
for i in range(len(temp)):
    url = 'https://internshala.com/internships/'+user_text+'-internship/page-'+temp[i]+'/'
    html_text = requests.get(url).text
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
        if(Duration[39:46] == '1Month'):
            Duration = '1 Month'
        if(Duration[39:46] == '2Months'):
            Duration = '2 Months'
        if(Duration[39:46] == '3Months'):
            Duration = '3 Months'
        if(Duration[39:46] == '4Months'):
            Duration = '4 Months'
        if(Duration[39:46] == '5Months'):
            Duration = '5 Months'
        if(Duration[39:46] == '6Months'):
            Duration = '6 Months'
        if(Duration[35:42] == '1Month'):
            Duration = '1 Month'
        if(Duration[35:42] == '2Months'):
            Duration = '2 Months'
        if(Duration[35:42] == '3Months'):
            Duration = '3 Months'
        if(Duration[35:42] == '4Months'):
            Duration = '4 Months'
        if(Duration[35:42] == '5Months'):
            Duration = '5 Months'
        if(Duration[35:42] == '6Months'):
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
        if(len(Stipend) == 12):
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
        x = x+1    
end = time.time()
print()
print("No.of Companies scraped : {}".format(x))
elapsed_time = end - start
minutes = elapsed_time/60
print("Elapsed time(seconds) : {} seconds".format(elapsed_time))
print("Elapsed time(Minutes) : {} minutes".format(minutes))