from django.core.management.base import BaseCommand
import bs4
import requests
from currencies.models import Currency


class Command(BaseCommand):

    def handle(self, *args, **options):
        url = 'https://www.cbr.ru/scripts/XML_daily.asp'
        url_code = requests.get(url)
        soup = bs4.BeautifulSoup(url_code.text, 'lxml')

        names = soup.find_all('name')
        rates = soup.find_all('value')

        for i in range(0, len(names)):
            Currency.objects.get_or_create(
                name=names[i].get_text(),
                rate=float(rates[i].get_text().replace(',', '.'))
                )
