from .CONSTANTS import ENDPOINT, IP_ENDPOINT
import requests as r
import datetime

class TimeInfo():
    def __init__(self, to_get=0, ip: bool=False):
        if ip:
            if to_get == 0:
                self.result = r.get(IP_ENDPOINT).json()
            else:
                self.result = r.get(IP_ENDPOINT + to_get).json()
        else:
            self.result = r.get(ENDPOINT + to_get).json()

        self.week_day = self.result['day_of_week']
        self.year_day = self.result['day_of_year']
        self.week_number = self.result['week_number']

        # Daylight savings
        self.is_dst = self.result['dst']
        self.dst_offset = self.result['dst_offset']
        self.dst_from = self.result['dst_from']
        self.dst_until = self.result['dst_until']

        self.unixtime = self.result['unixtime']
        self.utc = self.result['utc_datetime']
        self.utc_offset = self.result['utc_offset']
        self.raw_offset = self.result['raw_offset']
        self.abbreviation = self.result['abbreviation']

        # Aware datetime object
        self.datetime = datetime.datetime.strptime(self.result['datetime'], '%Y-%m-%dT%H:%M:%S.%f%z')
        self.datetime_str = self.result['datetime']

    def __str__(self):
        return self.datetime.strftime('%Y-%m-%d %H:%M:%S.%f UTC%z')


if __name__ == '__main__':
    test = TimeInfo('America/Vancouver')
    print(test.result)
    print(test.datetime.tzinfo)
    print(test)