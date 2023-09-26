from pagination import intern_page_limit

user_text = str(input('Enter a tech stack to extract : '))
stored_text = user_text
modified_user_text = user_text.replace('-' , ' ').title()

# print(stored_text)
user_input = [
    'information technology','Information technology','it','It','IT',
    'computer vision','Computer vision','cv' , 'CV',
    'machine learning','Machine learning','Ml','ML','ml',
    'data science','Data science',
    'artificial intelligence','Artificial intelligence','AI','ai',
    'android app development','Android app development','android','Android',
    'ios app development','ios app','Ios app','ios',"Ios","IOS",
    'web development','Web development',
    'full stack development','Full stack development','Full stack developer','full stack developer',
    'front end development','Front end development','front end developer','Front end developer','front end','Front end','frontend','Frontend',
    'backend','backend development','Backend development','Backend',
    'flutter','flutter development','Flutter development','Flutter',
    'angular js','Angular js','angular.js',
    'php','php development','Php development','PHP','Php',
    'node js' ,'Node js','nodejs','Nodejs',
    'mobile app development','Mobile app development',
    'blockchain','Blockchain', 
    ]



# tech stack interns
if(user_text == 'information technology' or user_text == 'Information technology' or user_text == 'it' or user_text == 'It' or user_text =='IT'):
    user_text = 'information-technology'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))


elif(user_text == 'computer vision' or user_text == 'Computer vision' or user_text == 'cv' or user_text == 'CV'):
    user_text = 'computer-vision'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

elif(user_text == 'machine learning' or user_text == 'Machine learning' or user_text == 'Ml' or user_text == 'ML' or user_text == 'ml'):
    user_text = 'machine-learning'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

elif(user_text == 'data science' or user_text == 'Data science'):
    user_text = 'data-science'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    modified_user_text = user_text.replace('-' , ' ').title()
    int_total_pages = intern_page_limit(link)
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))


elif(user_text == 'artificial intelligence' or user_text == 'Artificial intelligence' or user_text == 'AI' or user_text == 'ai'):
    user_text = 'artificial-intelligence-(ai)'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

elif(user_text == 'android app development' or user_text == 'Android app development' or user_text == 'android' or user_text == 'Android'):
    user_text = 'android-app-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

elif(user_text == 'ios app development' or user_text == 'ios app' or user_text == 'Ios app' or user_text == 'ios' or user_text == "Ios" or user_text == "IOS"):
    user_text == 'ios-app-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').upper()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

elif(user_text == 'web development' or user_text == 'Web development'):
    user_text == 'web-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

elif(user_text == 'full stack development' or user_text == 'Full stack development' or user_text == 'Full stack developer' or user_text == 'full stack developer'):
    user_text = 'full-stack-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

elif(user_text == 'front end development' or user_text == 'Front end development' or user_text == 'front end developer' or user_text == 'Front end developer' or user_text == 'front end' or user_text == 'Front end' or user_text == 'frontend' or user_text == 'Frontend'):
    user_text = 'front-end-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

elif(user_text == 'backend' or user_text == 'backend development' or user_text == 'Backend development' or user_text == 'Backend'):
    user_text = 'backend-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

elif(user_text == 'flutter' or user_text == 'flutter development' or user_text == 'Flutter development' or user_text == 'Flutter'):
    user_text = 'flutter-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

elif(user_text == 'angular js' or user_text == 'Angular js' or user_text == 'angular.js'):
    user_text = 'angular.js-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

elif(user_text == 'php' or user_text == 'php development' or user_text == 'Php development' or user_text == 'PHP' or user_text== 'Php'):
    user_text = 'php-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

elif(user_text == 'node js' or user_text == 'Node js' or user_text == 'nodejs' or user_text == 'Nodejs'):
    user_text = 'node.js-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

elif(user_text == 'mobile app development' or user_text == 'Mobile app development'):
    user_text = 'mobile-app-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

elif(user_text == 'blockchain' or user_text == 'Blockchain'):
    user_text = 'blockchain-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

elif(user_text == 'game development' or user_text == 'Game development'):
    user_text = 'game-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

elif(user_text == 'javascript' or user_text == 'Javascript'):
    user_text = 'javascript-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

elif(user_text == 'wordpress' or user_text == 'Wordpress'):
    user_text = 'wordpress-development'
    # user_text = 'wordpress'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

elif(user_text == 'python' or user_text == 'Python' or user_text == 'PYTHON'):
    user_text = 'python'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , int(int_total_pages)+1):
        str_list.append(str(i))

elif(user_text == 'django' or user_text == 'Django'):
    user_text = 'django'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))


elif(user_text == 'java' or user_text == 'Java'):
    user_text = 'java'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i)) 

elif(user_text == 'software development' or user_text == 'Software development' or user_text == 'Software developer' or user_text == 'software developer' or user_text == 'SDE' or user_text == 'Sde' or user_text == 'sde'):
    user_text = 'software-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

elif(user_text == 'cybersecurity' or user_text == 'Cybersecurity' or user_text == 'Cyber security' or user_text == 'cyber security' or user_text == 'Cyber Security'):
    user_text == 'cyber-security'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , int(int_total_pages)+1):
        str_list.append(str(i))

elif(user_text == 'ui and ux' or user_text == 'ui/ux' or user_text == 'UI/UX' or user_text == 'Ui/ux'):
    user_text = 'ui%2Fux'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , int(int_total_pages)+1):
        str_list.append(str(i))

elif(user_text == 'cs' or user_text == 'CS' or user_text == 'Computer Science' or user_text == 'Computer science'):
    user_text = 'computer-science'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , int(int_total_pages)+1):
        str_list.append(str(i))
    
elif(user_text == 'network engineering' or user_text == 'Network engineering' or user_text == 'Network Engineering'):
    user_text = 'network-engineering'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

# Design
elif(user_text == 'graphic design' or user_text == 'Graphic design'):
    user_text == 'design'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))


# Motion Graphics
elif(user_text == 'motion graphics' or user_text == 'Motion graphics' or user_text == 'Motion Graphics'):
    user_text = 'motion-graphics'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , int(int_total_pages)+1):
        str_list.append(str(i))

# Embedded Systems
elif(user_text == 'Embedded systems' or user_text == 'Embedded Systems' or user_text == 'embedded systems'):
    user_text = 'embedded-systems'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , int(int_total_pages)+1):
        str_list.append(str(i))

# Big Data
elif(user_text == 'big data' or user_text == 'Big data' or user_text == 'Big Data'):
    user_text = 'big-data'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , int(int_total_pages)+1):
        str_list.append(str(i))

# Data Analytics
elif(user_text == 'Data Analytics' or user_text == 'data analytics' or user_text == 'Data analytics'):
    user_text == 'data-analytics'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))


elif(user_text == 'english proficiency'):
    user_text = 'english-proficiency-written'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))


else:
    print("Keyword not found")
    print("please check")
