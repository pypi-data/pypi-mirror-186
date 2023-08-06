from urllib.request import urlopen
import json
from .lang import get_valid_ip


def get_country():
    IP = get_valid_ip()
    url = 'http://ipinfo.io/' + IP + '/json'
    response = urlopen(url)
    data = json.load(response)
    # city = data['city']
    # region = data['region']
    country = data['country']
    # location = data['loc']
    # org = data['org']
    return country
