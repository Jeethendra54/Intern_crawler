from pagination import intern_page_limit

user_text = str(input('Enter a tech stack to extract : '))
stored_text = user_text
modified_user_text = user_text.replace('-' , ' ').title()

# all_intern_link = 'https://internshala.com/internships/'
# if(user_text == '' or user_text == ' ' or user_text == 'all' or user_text == 'All'):
#     all_intern_link = 'https://internshala.com/internships/'
#     str_list = [] 
#     int_total_pages = overall_intern_count(all_intern_link)
#     modified_user_text = user_text.replace('-' , ' ').title()
#     for i in range(1 , (int_total_pages)+1):
#         str_list.append(str(i))



# tech stack interns
if(user_text == 'information technology' or user_text == 'Information technology' or user_text == 'it' or user_text == 'It' or user_text =='IT'):
    user_text = 'information-technology'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))


if(user_text == 'computer vision' or user_text == 'Computer vision' or user_text == 'cv' or user_text == 'CV'):
    user_text = 'computer-vision'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

if(user_text == 'machine learning' or user_text == 'Machine learning' or user_text == 'Ml' or user_text == 'ML' or user_text == 'ml'):
    user_text = 'machine-learning'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

if(user_text == 'data science' or user_text == 'Data science'):
    user_text = 'data-science'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    modified_user_text = user_text.replace('-' , ' ').title()
    int_total_pages = intern_page_limit(link)
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))


if(user_text == 'artificial intelligence' or user_text == 'Artificial intelligence' or user_text == 'AI' or user_text == 'ai'):
    user_text = 'artificial-intelligence-(ai)'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

if(user_text == 'android app development' or user_text == 'Android app development' or user_text == 'android' or user_text == 'Android'):
    user_text = 'android-app-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

if(user_text == 'ios app development' or user_text == 'ios app' or user_text == 'Ios app' or user_text == 'ios' or user_text == "Ios" or user_text == "IOS"):
    user_text == 'ios-app-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').upper()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

if(user_text == 'web development' or user_text == 'Web development'):
    user_text == 'web-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

if(user_text == 'full stack development' or user_text == 'Full stack development' or user_text == 'Full stack developer' or user_text == 'full stack developer'):
    user_text = 'full-stack-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

if(user_text == 'front end development' or user_text == 'Front end development' or user_text == 'front end developer' or user_text == 'Front end developer' or user_text == 'front end' or user_text == 'Front end' or user_text == 'frontend' or user_text == 'Frontend'):
    user_text = 'front-end-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

if(user_text == 'backend' or user_text == 'backend development' or user_text == 'Backend development' or user_text == 'Backend'):
    user_text = 'backend-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

if(user_text == 'flutter' or user_text == 'flutter development' or user_text == 'Flutter development' or user_text == 'Flutter'):
    user_text = 'flutter-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

if(user_text == 'angular js' or user_text == 'Angular js' or user_text == 'angular.js'):
    user_text = 'angular.js-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

if(user_text == 'php' or user_text == 'php development' or user_text == 'Php development' or user_text == 'PHP' or user_text== 'Php'):
    user_text = 'php-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

if(user_text == 'node js' or user_text == 'Node js' or user_text == 'nodejs' or user_text == 'Nodejs'):
    user_text = 'node.js-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

if(user_text == 'mobile app development' or user_text == 'Mobile app development'):
    user_text = 'mobile-app-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

if(user_text == 'blockchain' or user_text == 'Blockchain'):
    user_text = 'blockchain-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

if(user_text == 'game development' or user_text == 'Game development'):
    user_text = 'game-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

if(user_text == 'javascript' or user_text == 'Javascript'):
    user_text = 'javascript-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

# if(user_text == 'wordpress' or user_text == 'Wordpress'):
#     user_text = 'wordpress-development'
#     str_list = []
#     link = 'https://internshala.com/internships/' + user_text + '-internship/'
#     int_total_pages = intern_page_limit(link)
#     modified_user_text = user_text.replace('-' , ' ').title()
#     for i in range(1 , (int_total_pages)+1):
#         str_list.append(str(i))

if(user_text == 'python' or user_text == 'Python' or user_text == 'PYTHON'):
    user_text = 'python'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , int(int_total_pages)+1):
        str_list.append(str(i))

if(user_text == 'django' or user_text == 'Django'):
    user_text = 'django'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))


if(user_text == 'java' or user_text == 'Java'):
    user_text = 'java'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i)) 

if(user_text == 'software development' or user_text == 'Software development' or user_text == 'Software developer' or user_text == 'software developer' or user_text == 'SDE' or user_text == 'Sde' or user_text == 'sde'):
    user_text = 'software-development'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

if(user_text == 'cybersecurity' or user_text == 'Cybersecurity' or user_text == 'Cyber security' or user_text == 'cyber security' or user_text == 'Cyber Security'):
    user_text == 'cyber-security'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , int(int_total_pages)+1):
        str_list.append(str(i))

if(user_text == 'ui and ux' or user_text == 'ui/ux' or user_text == 'UI/UX' or user_text == 'Ui/ux'):
    user_text = 'ui%2Fux'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , int(int_total_pages)+1):
        str_list.append(str(i))

# Engineering Interns
# if(user_text == 'engineering' or user_text == 'Engineering'):
#     user_text = 'engineering'
#     str_list = []
#     link = 'https://internshala.com/internships/' + user_text + '-internship/'
#     int_total_pages = intern_page_limit(link)
#     modified_user_text = user_text.replace('-' , ' ').title()
#     for i in range(1 , int(int_total_pages)+1):
#         str_list.append(str(i))

# if(user_text == 'aerospace' or user_text == 'Aerospace'):
#     user_text = 'aerospace'
#     str_list = []
#     link = 'https://internshala.com/internships/' + user_text + '-internship/'
#     int_total_pages = intern_page_limit(link)
#     modified_user_text = user_text.replace('-' , ' ').title()
#     for i in range(1 , int(int_total_pages)+1):
#         str_list.append(str(i))

# if(user_text == 'mechanical' or user_text == 'Mechanical' or user_text == 'Mechanical Engineering' or user_text == 'Mechanical engineering'):
#     user_text = 'mechanical'
#     str_list = []
#     link = 'https://internshala.com/internships/' + user_text + '-internship/'
#     int_total_pages = intern_page_limit(link)
#     modified_user_text = user_text.replace('-' , ' ').title()
#     for i in range(1 , int(int_total_pages)+1):
#         str_list.append(str(i))

# if(user_text == 'civil' or user_text == 'Civil' or user_text == 'Civil engineering' or user_text == 'Civil Engineering'):
#     user_text = 'civil'
#     str_list = []
#     link = 'https://internshala.com/internships/' + user_text + '-internship/'
#     int_total_pages = intern_page_limit(link)
#     modified_user_text = user_text.replace('-' , ' ').title()
#     for i in range(1 , int(int_total_pages)+1):
#         str_list.append(str(i))

if(user_text == 'cs' or user_text == 'CS' or user_text == 'Computer Science' or user_text == 'Computer science'):
    user_text = 'computer-science'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , int(int_total_pages)+1):
        str_list.append(str(i))
    
# if(user_text == 'Electronics' or user_text == 'electronics' or user_text == 'ec' or user_text == 'EC'):
#     user_text = 'electronics'
#     str_list = []
#     link = 'https://internshala.com/internships/' + user_text + '-internship/'
#     int_total_pages = intern_page_limit(link)
#     modified_user_text = user_text.replace('-' , ' ').title()
#     for i in range(1 , int(int_total_pages)+1):
#         str_list.append(str(i))

# if(user_text == 'Electrical' or user_text == 'electrical' or user_text == 'EEE' or user_text == 'eee'):
#     user_text = 'electrical'
#     str_list = []
#     link = 'https://internshala.com/internships/' + user_text + '-internship/'
#     int_total_pages = intern_page_limit(link)
#     modified_user_text = user_text.replace('-' , ' ').title()
#     for i in range(1 , int(int_total_pages)+1):
#         str_list.append(str(i))

if(user_text == 'network engineering' or user_text == 'Network engineering' or user_text == 'Network Engineering'):
    user_text = 'network-engineering'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

# Design
if(user_text == 'graphic design' or user_text == 'Graphic design'):
    user_text == 'design'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))

# SEO
# if(user_text == 'seo' or user_text == 'Seo' or user_text == 'SEO' or user_text == 'search engine optimization' or user_text == 'Search engine optimization' or user_text == 'Search Engine Optimization'):
#     user_text = 'search-engine-optimization-(seo)'
#     str_list = []
#     link = 'https://internshala.com/internships/' + user_text + '-internship/'
#     int_total_pages = intern_page_limit(link)
#     modified_user_text = user_text.replace('-' , ' ').title()
#     for i in range(1 , (int_total_pages)+1):
#         str_list.append(str(i))

# Teaching
# if(user_text == 'teaching' or user_text == 'Teaching'):
#     user_text = 'teaching'
#     str_list = []
#     link = 'https://internshala.com/internships/' + user_text + '-internship/'
#     int_total_pages = intern_page_limit(link)
#     modified_user_text = user_text.replace('-' , ' ').title()
#     for i in range(1 , int(int_total_pages)+1):
#         str_list.append(str(i))

# Motion Graphics
if(user_text == 'motion graphics' or user_text == 'Motion graphics' or user_text == 'Motion Graphics'):
    user_text = 'motion-graphics'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , int(int_total_pages)+1):
        str_list.append(str(i))

# Embedded Systems
if(user_text == 'Embedded systems' or user_text == 'Embedded Systems' or user_text == 'embedded systems'):
    user_text = 'embedded-systems'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , int(int_total_pages)+1):
        str_list.append(str(i))

# Video Making/Editing
# if(user_text == 'Video making' or user_text == 'video making' or user_text == 'Video Making' or user_text == 'video editing' or user_text == 'Video Editing' or user_text == 'Video editing'):
#     user_text = 'video-making%2Fediting'
#     str_list = []
#     link = 'https://internshala.com/internships/' + user_text + '-internship/'
#     int_total_pages = intern_page_limit(link)
#     modified_user_text = user_text.replace('-' , ' ').title()
#     for i in range(1 , int(int_total_pages)+1):
#         str_list.append(str(i))

# Event Management
# if(user_text == 'event management' or user_text == 'Event Management' or user_text == 'Event management'):
#     user_text = 'event-management'
#     str_list = []
#     link = 'https://internshala.com/internships/' + user_text + '-internship/'
#     int_total_pages = intern_page_limit(link)
#     modified_user_text = user_text.replace('-' , ' ').title()
#     for i in range(1 , int(int_total_pages)+1):
#         str_list.append(str(i))

# Photography
# if(user_text == 'photography' or user_text == 'Photography' or user_text == 'photo' or user_text == 'Photo'):
#     user_text == 'photography'
#     str_list = []
#     link = 'https://internshala.com/internships/' + user_text + '-internship/'
#     int_total_pages = intern_page_limit(link)
#     modified_user_text = user_text.replace('-' , ' ').title()
#     for i in range(1 , int(int_total_pages)+1):
#         str_list.append(str(i))

# Big Data
if(user_text == 'big data' or user_text == 'Big data' or user_text == 'Big Data'):
    user_text = 'big-data'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , int(int_total_pages)+1):
        str_list.append(str(i))

# Film Making
# if(user_text == 'film making' or user_text == 'Film making' or user_text == 'Film Making'):
#     user_text == 'film-making'
#     str_list = []
#     link = 'https://internshala.com/internships/' + user_text + '-internship/'
#     int_total_pages = intern_page_limit(link)
#     modified_user_text = user_text.replace('-' , ' ').title()
#     for i in range(1 , int(int_total_pages)+1):
#         str_list.append(str(i))

# Finance
# if(user_text == 'Finance' or user_text == 'finance'):
#     user_text = 'finance'
#     str_list = []
#     link = 'https://internshala.com/internships/' + user_text + '-internship/'
#     int_total_pages = intern_page_limit(link)
#     modified_user_text = user_text.replace('-' , ' ').title()
#     for i in range(1 , int(int_total_pages)+1):
#         str_list.append(str(i))

# Law
# if(user_text == 'law' or user_text == 'Law'):
#     str_list = ['1' , '2' , '3']


# MBA
# if(user_text == 'mba' or user_text == 'Mba' or user_text == 'MBA'):
#     user_text = 'mba'
#     str_list = []
#     link = 'https://internshala.com/internships/' + user_text + '-internship/'
#     int_total_pages = intern_page_limit(link)
#     modified_user_text = user_text.replace('-' , ' ').title()
#     for i in range(1 , int(int_total_pages)+1):
#         str_list.append(str(i))

# Marketing
# if(user_text == 'Marketing' or user_text == 'marketing' or user_text == 'digital marketing' or user_text == 'Digital marketing'):
#     user_text = 'digital-marketing'
#     str_list = []
#     link = 'https://internshala.com/internships/' + user_text + '-internship/'
#     int_total_pages = intern_page_limit(link)
#     modified_user_text = user_text.replace('-' , ' ').title()
#     for i in range(1 , (int_total_pages)+1):
#         str_list.append(str(i))

# Data Analytics
if(user_text == 'Data Analytics' or user_text == 'data analytics' or user_text == 'Data analytics'):
    user_text == 'data-analytics'
    str_list = []
    link = 'https://internshala.com/internships/' + user_text + '-internship/'
    int_total_pages = intern_page_limit(link)
    modified_user_text = user_text.replace('-' , ' ').title()
    for i in range(1 , (int_total_pages)+1):
        str_list.append(str(i))