import requests
from bs4 import BeautifulSoup
from gov_scraper_person import Person

# Function to parse the organisations from the response
def parseOrganisations(response, element, elementClass):
    soup = BeautifulSoup(response.content, "html.parser")
    return soup.find_all(element, class_=elementClass)

# Function to fetch the page and print the status
def getPage(baseURL):
    response = requests.get(baseURL)
    if response.status_code == 200:
        return response
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")

baseURL = 'https://www.directory.gov.au'
page = getPage(baseURL + '/commonwealth-entities-and-companies')
results = parseOrganisations(page, "td", "views-field views-field-title")

for result in results:
    a_tag = result.find("a")  # Find the <a> tag within the <td>
    if a_tag:
        organisation = result.text.strip()
        href = a_tag["href"]  # Extract the href attribute
        organisation_page = getPage(baseURL + href)
        organisation_results = parseOrganisations(organisation_page, "section", "views-element-container")
        for organisation_result in organisation_results:
            if organisation_result.find(lambda tag: "Key People" in tag.get_text()):
                people = organisation_result.find_all("li", class_="list-group-item")
                for person in people:
                    person_obj = Person()

                    person_obj.addOrganisation(organisation)

                    position_element = person.find("a")
                    person_position = position_element.text.strip()
                    person_obj.addPosition(person_position)

                    name_element = position_element.find_next("a")
                    person_name = name_element.text.strip()
                    person_obj.addName(person_name)

                    phone_element = person.find('a', attrs={"data-original-title": "Phone Number"})
                    if phone_element:
                        person_phone = phone_element.get_text(strip=True)
                        person_obj.addPhone(person_phone)
                    
                    email_element = person.find('a', attrs={"data-original-title": "Email"})
                    if email_element:
                        person_email = email_element.get_text(strip=True)
                        person_obj.addEmail(person_email)

                    
                    # Print the person's details
                    print(f"Name: {person_obj.name}, Organisation: {person_obj.organisation}, Position: {person_obj.position}, Phone: {person_obj.phone}, Email: {person_obj.email}")
        

