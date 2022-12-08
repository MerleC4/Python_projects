
import requests
from bs4 import BeautifulSoup
import re

def validLink(link):
    """ Ensures that the link meets our defined criteria.

    Args:
        link (str): Google link of string.
    """

    if 'google' in link:
        return False
    if 'yelp' in link:
        return False
    if 'expertise' in link:
        return False
    return True

def getGoogleLinks(URL):
    """ Returns all of the URLs found on the first google website search.

    Args:
        link (str): Google link of string.
    """

    reqs = requests.get(URL)
    soup2 = BeautifulSoup(reqs.text, 'html5lib')
    urls = []
    for link in soup2.find_all('a'):
        # print(link.get('href'))
        if "/url?q=" in link.get('href'):
            newLink = link.get('href')[7:link.get('href').index('&sa=')]
            if (validLink(newLink)):
                # print(newLink)
                urls.append(newLink)
    return urls

def webscraper(URL):
    """ Scrapes the website for phone numbers.

    Args:
        link (str): Link of specific website.
    """


    try:
        r = requests.get(URL, timeout=1)
    except:
        return None
    #print(URL)
    reObj = re.compile(r"(\([0-9]{3}\)[\s-]?|[0-9]{3}-)[0-9]{3}-[0-9]{4}")
    soup = BeautifulSoup(r.content, 'html5lib')
    # print(soup.get_text())
    if "403 Access Denied" in soup.get_text():
        return None
    if "403 Forbidden" in soup.get_text():
        return None
    # phonelist = soup.get_text().replace(" ", "").find_all(reObj)
    phoneList = re.findall("\(\d{3}\)\d{3}-\d{4}", soup.get_text().replace(" ", ""))
    phoneList2 = re.findall("\(\d{3}\)\d{3}–\d{4}", soup.get_text().replace(" ", ""))
    phoneList3 = re.findall("\d{3}–\d{3}–\d{4}", soup.get_text().replace(" ", ""))
    phoneList4 = re.findall("\d{3}-\d{3}-\d{4}", soup.get_text().replace(" ", ""))
    phoneSet = [*set(phoneList)]
    phoneSet2 = [*set(phoneList2)]
    phoneSet3 = [*set(phoneList3)]
    phoneSet4 = [*set(phoneList4)]
    phoneSet = phoneSet + phoneSet2 + phoneSet3 + phoneSet4
    if '(999)999-9999' in phoneSet:
        phoneSet.remove('(999)999-9999')
    if '999-999-9999' in phoneSet:
        phoneSet.remove('999-999-9999')
    if '(000)000-0000' in phoneSet:
        phoneSet.remove('(000)000-0000')
    if '000-000-0000' in phoneSet:
        phoneSet.remove('000-000-0000')

    if len(phoneSet) == 0 or len(phoneSet) > 5:
        return None

    if "-" in soup.title.get_text().split('|')[0]:
        return None

    return [soup.title.get_text(), phoneSet, URL]


def makeURL(service, location):
    """ Creates the google query link.

    Args:
        service (str): Service user wants.
        location (str): Location user wants.
    """

    URL2 = "https://www.google.com/search?q="
    for val in service:
        if val == " ":
            URL2 += "+"
        else:
            URL2 += val
    URL2 += "+near+"
    for val in location:
        if val == " ":
            URL2 += "+"
        else:
            URL2 += val

    return URL2

def starter(service, location):
    """ Runs the code.

    Args:
        service (str): Service user wants.
        location (str): Location user wants.
    """

    
    URL = makeURL(service, location)
    
    links = getGoogleLinks(URL)

    finalResults = []
    for val in links:
        newList = webscraper(val)
        if newList:
            result = [newList[0], newList[1], newList[2]]

            finalResults.append(result)

    for result in finalResults:
        print(result[0])
        print(result[1])
        print(result[2])
        print()
    # print(finalResults)
    return finalResults


def main():
    service = input("Enter service you are looking for: ")
    location = input("Enter location (City): ")
    starter(service, location)

main()