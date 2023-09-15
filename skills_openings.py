from bs4 import BeautifulSoup
import requests

def required_skills(url): 
    emp_list=[]
    extracted_skills = [] 
    convert_to_text = requests.get(url).text
    soup = BeautifulSoup(convert_to_text , 'lxml')
    skills = soup.find_all('span' , class_='round_tabs')
    skills = list(skills)

    if(len(skills) == 0):
        extracted_skills = 'Unavailable'
        return extracted_skills
    else:
        for i in range(len(skills)):
            emp_list.append(skills[i].text)
        
        if 'Certificate' in emp_list:
            extracted_skills = emp_list[0:emp_list.index('Certificate')]
            extracted_skills = ', '.join(extracted_skills) # converts list to a string
            return extracted_skills
        
        else:
            extracted_skills = 'Not mentioned'
            return extracted_skills

def openings(url):
    total_openings = 0
    convert_to_text = requests.get(url).text
    soup = BeautifulSoup(convert_to_text , 'lxml')
    vacancies = soup.find_all('div' , class_='text-container') 
    vacancies = list(vacancies)
    for vacancy in vacancies:
        try:
            total_openings = int(vacancy.text.strip())
            return total_openings
        except:
            pass

# specific_company_url = 'https://internshala.com/internship/detail/blockchain-development-internship-in-jaipur-at-crony-technovest-opc-private-limited1689135485'
# print(required_skills(specific_company_url))
# print(openings('https://internshala.com/internship/detail/business-development-internship-in-noida-at-ayukul-technologies-private-limited1689605651'))
