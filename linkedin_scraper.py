# example https://github.com/linkedtales/scrapedin https://github.com/joeyism/linkedin_scraper  https://github.com/ericfourrier/scrape-linkedin and https://github.com/federicohaag/LinkedInScraping
# or use bubble instead here: https://forum.bubble.io/t/linkedin-sign-a-user-up/20

!pip install kora
!pip install linkedin_scraper

from kora.selenium import wd
from linkedin_scraper import Person, actions
driver = wd

email = "ed@lazygenius.co.uk"
password = "Lazygenius123"
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
#person = Person("https://www.linkedin.com/in/edbayes", driver=driver)

#person = Person("https://www.linkedin.com/in/edbayes", driver=wd)
#person.experiences

#Open login page
wd.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

#Enter login info:
elementID = wd.find_element_by_id('username')
elementID.send_keys('bayesbayes@gmail.com')

elementID = wd.find_element_by_id('password')
elementID.send_keys('Doorknob123')
elementID.submit()

wd.get("https://www.linkedin.com/in/edbayes/")

print(wd.page_source)  # results
