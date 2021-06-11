from .CONSTANTS import ENDPOINT
from .timeinfo import TimeInfo
# External libraries
import requests
import unidecode
from countryinfo import CountryInfo

class WorldTime():
    """ To avoid abusing the rate of worldtimeAPI, this class limits the number
    of requests it makes for some methods If you wish to refresh the request, 
    please use the 'refresh' method """

    def __init__(self):
        self.locations = requests.get(ENDPOINT).json()
        # self.regions = set(map(splitting, self.request))
    
    def from_ip(self, ip: str=''):
        """"""
        if ip == '':
            return TimeInfo(ip=True)
        try:
            new_ip = ip.split('.')
            for i in new_ip:
                int(i)
        except ValueError:
            raise TypeError('Invalid IP entered. Please ensure it is a valid IPv4 address')
        return TimeInfo(to_get=ip, ip=True)

    def find_by_name(self, name: str) -> set:
        """ Returns a list of strings for all locations with that name. """
        name = name.title()
        name = unidecode.unidecode(name).replace(' ', '_')
        return [location for location in self.locations if name in location]

    def get_closest(self, array: list, name: str) -> int:
        """ Matches the closest string. Helper function """
        new_list = [place.split('/')[1] for place in array]
        answer = 0
        len_str = len(name)
        for i in range(1, len(new_list)):
            if abs(len(new_list[i]) - len_str) < abs(len(new_list[answer]) - len_str):
                answer = i
            
        return answer
    
    def search(self, name: str) -> str:
        """ Takes a country name or a city and tries to find it in the database.
        Returns a proper location to be used in get_location if found, otherwise 
        returns an empty string."""

        location = self.find_by_name(name)
        if len(location) != 1:
            try:
                country = CountryInfo(name)
                if len(self.find_by_name(country.capital())) == 1:
                    return self.find_by_name(country.capital())[0]

                for province in country.provinces():
                    current_province = self.find_by_name(province)
                    if len(current_province) != 0:
                        if len(current_province) > 1:
                            return current_province[self.get_closest(current_province, name)]
                        return current_province[0]

                for bordering in country.borders():
                    current_country = CountryInfo(bordering)
                    if len(self.find_by_name(current_country.capital())) == 1:
                        return self.find_by_name(current_country.capital())[0]

                    for province in current_country.provinces():
                        current_province = self.find_by_name(province)
                        if len(current_province) != 0:
                            return current_province[0]
            except:
                pass

        elif len(location) == 1:
            return location[0]
        else:
            return ''


    def get_location(self, location: str) -> object:
        "Takes a location and returns a TimeInfo object."
        if location not in self.locations:
            raise ValueError('Invalid location. For valid locations look at the locations attribute.')
        else:
            return TimeInfo(location)

    def refresh(self):
        self.locations = requests.get(ENDPOINT).json()


if __name__ == '__main__':
    worldtime = WorldTime()
    print(worldtime.from_ip('8.8.8.8'))
    # time = worldtime.find_by_name('Bahia')
    # print(worldtime.search('São Paulo'))
    # worldtime.get_closest(['America/Bahia', 'America/Bahia_drogas'], 'Bahia')
    # print(worldtime.get_location(time[0]))
    # print(worldtime.search('Brasil'))
    # print('Bahia' in 'America/Bahia')