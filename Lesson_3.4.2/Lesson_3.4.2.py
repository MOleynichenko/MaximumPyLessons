import requests
from bs4 import BeautifulSoup

def get_course_info(id):
    url = 'https://www.cbr.ru/scripts/XML_daily.asp'
    r = requests.get(url)
    xml_parser = BeautifulSoup(r.content, 'xml')
    try:
        currency = xml_parser.find('Valute', {'ID': id})
        nominal = currency.find("Nominal").text
        name = currency.find("Name").text
        value = currency.find("Value").text
        return f"({nominal} шт.) {name} стоит(ят) {value}руб."
    except AttributeError:
        return f"Такого id({id}) несуществует."
print(get_course_info(input("Id:\n")))