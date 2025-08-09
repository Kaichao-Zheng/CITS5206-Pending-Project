from linkedin_scraper import Person, actions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def scrape_profile(linkedin_profile_url, driver):
    """Scrape a person's LinkedIn profile."""
    person = Person(linkedin_profile_url, driver=driver, scrape=True)
    
    pass                                                                    # Salutation
    print("Full Name:", person.name)                                        # FirstName, LastName
    print("Recent Institution:", person.experiences[0].institution_name)    # Organization
    print("Recent Position:", person.experiences[0].position_title)         # Role
    pass                                                                    # Gender
    print("Location:", person.location)                                     # City (if outside AUS), State AUS only, Country
    print("Contacts:", person.contacts)                                     # Business Phone, Mobile Phone, EmailAddress.
    pass                                                                    # Sector

# Match, install, and start a webdriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# LinkedIn login credentials (Assuming no MFA or CAPTCHA is required)
email = "some-email@email.address"
password = "password123"
actions.login(driver, email, password)

# Scrape the LinkedIn profile (~30s per profile)
scrape_profile("https://www.linkedin.com/in/andre-iguodala-65b48ab5", driver)
# Browser closes automatically