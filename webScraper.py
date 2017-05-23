import requests
from bs4 import BeautifulSoup

def webscrpr():
    page = requests.get("http://www.accuweather.com/en/us/briarcliff-manor-ny/10510/may-weather/2146224") 
    soup = BeautifulSoup(page.content)
    text = soup.findAll("td",{"class":"today"})
    data = text[0].get_text().split('\n')
    #print data
    #print type(data)
    newdict = {}
    newdict['day_and_Date'] = data[2]
    newdict['max_temp'] = data[6]
    newdict['min_temp'] = data[7]
    newdict['weather_condition'] = data[9]
    newdict['historical'] = data[12]
    print newdict

webscrpr()


