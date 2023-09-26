import re
import time
from time import sleep
import requests
from bs4 import BeautifulSoup
# from shared_data import intern_count 
# from user_prompt import *
from user_prompt import user_text , modified_user_text , str_list
# from skills_openings import required_skills , openings



with open('file.txt' , 'w') as file:
        file.write(str(modified_user_text) + " Internships" + "\n")
        file.write("\n")
        file.close()


Time  = float(input("Enter time : "))
x = 0
sleep(Time)
print()
print("Extracting {} internships".format(modified_user_text))

start = time.time()
for i in range(len(str_list)):

    url = 'https://internshala.com/internships/' + user_text + '-internship/page-' + str_list[i] + '/'

    # Total_intern_in_website = intern_count(url)
    html_text = requests.get(url)

    if(html_text.status_code == 200):
        # print("Status code : {}".format(html_text.status_code))
        # print("Connection established....")

        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml') 
        Interns = soup.find_all('div' , class_='container-fluid individual_internship visibilityTrackerItem')
        

        for Intern in Interns:
            Company_name = Intern.find('h4',class_='heading_6 company_name').text.strip()
            Role = Intern.find('h3',class_='heading_4_5 profile').text.strip()
            Location = Intern.find('div',id='location_names').text.strip()
            Start_date = Intern.find('div',id='start-date-first').text.strip()
            Stipend = Intern.find('span',class_='stipend')
            Post_Info = Intern.find('div',class_='posted_by_container').text.strip()
            Duration = Intern.find('div',class_='other_detail_item_row').text.strip().replace(' ','')
            Hiring = Intern.find('div',class_='actively_hiring_badge')

            link = Intern.find('a')['href']
            link = 'https://internshala.com' + link 
            # total_skills = required_skills(link)
            # No_of_openings = openings(link)
            total_skills = ''
            No_of_openings = ''
            
            if(Hiring == None):
                Hiring = 'Info uavailable'
            else:
                Hiring = Intern.find('div',class_='actively_hiring_badge').text.lstrip().rstrip()
            
            if Start_date:
                Start_date = re.findall(r'I[a-z]*' , Start_date)
                Start_date = "".join(Start_date)
            else:
                Start_date = "Not Provided"

            if Duration:
                Duration = str(re.findall(r'[\d][A-z]*' , Duration)[0])
                Duration = Duration[0] + " " + Duration[1:]
            else:
                Duration = "Not Provided"
            
            if Stipend:
                Stipend = Stipend.text
            else:
                Stipend = 'N/A'
            # if(len(Stipend) == 12):
            #     Stipend = ' Not provided'
            if(Stipend == 'Unpaid'):
                Stipend = 'Unpaid'
            # if(Stipend == ''):
            #     Stipend = 'N/A'
        
            if(len(total_skills) == 0):
                total_skills = 'Unavailable/Not mentioned'
            if(No_of_openings == 0):
                No_of_openings = 'Not mentioned'

            x = x + 1 # counting companies

            with open('file.txt', 'a') as f:
                f.write("Compnay {} ".format(x) + '\n')
                f.write( 'Company : ' + Company_name + '\n')
                f.write('Role : ' + Role + '\n')
                # f.write('Required Skills : '+ total_skills + '\n')
                f.write('Location : ' + Location + '\n')
                f.write('Start Date : ' + Start_date + '\n')
                f.write('Stipend : ' + Stipend.lstrip() + '\n')
                f.write('Posted ' + Post_Info + '\n')
                f.write('Duration : ' + Duration + '\n')
                # f.write('Openings : {}'.format(No_of_openings) + '\n')
                f.write('Hiring Info : ' + Hiring + '\n')
                f.write('Link : {}'.format(link) + '\n')
                f.write('\n')
                f.close()
        
            print()
            print("Company: {}".format(Company_name))
            sleep(Time)
            print("Role: {}".format(Role))
            sleep(Time)
            # print("Required Skills : {}".format(total_skills))
            # sleep(Time)
            print("Location: {}".format(Location))
            sleep(Time)
            print("Start Date: {}".format(Start_date))
            sleep(Time)
            print("Stipend: {}".format(Stipend))
            sleep(Time)
            print("Duration: {}".format(Duration))
            sleep(Time)
            # print("Openings : {}".format(No_of_openings))
            # sleep(Time)
            print("Posted {}".format(Post_Info))
            sleep(Time)
            print("Hiring Info : {}".format(Hiring))
            sleep(Time)
            print("Apply here : {}".format(link))
    
    elif(html_text.status_code != 200):
        print("Status code : {}".format(html_text.status_code))
        print("Error in establishing connection.")
        print("Check the internet connection or check the URL")
end = time.time()
print()
# print("No.of Companies scraped : {}".format(x))

# print("Total No.of {} internships shown on Internshala website = {}".format(modified_user_text , Total_intern_in_website))
print("Total No.of {} internships scraped = {}".format(modified_user_text , x))
seconds = end - start
minutes = seconds/60
round_off_sec = round(seconds , 2)
print()
print("Elapsed time(seconds) : {} seconds".format(round(seconds , 2)))
print("Elapsed time(Minutes) : {} minutes".format(round(minutes , 2)))


with open("file.txt" , 'a') as f:
    f.write("No.of Companies scraped : {}".format(x))
    f.write("\n")
    f.write("Scraped in {} seconds".format(round_off_sec))
    f.write("\n")
    # f.write(str(Interns))
    f.close()

