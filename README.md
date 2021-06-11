# Worldtimepy
###### v0.1.1
Worldtime-py is a Python wrapper for **![WorldtimeAPI](http://worldtimeapi.org/)**. It is able to search through the endpoints of the API to find the closest location if the exact one could not be found. It reduces the strain and the difficulty of getting the time for the location desired.

**![WorldtimeAPI](http://worldtimeapi.org/)** is a JSON API for obtaining the current time in, and related data about, a timezone. It gives data such as the UTC offset, whether that timezone is in Daylight Savings Time (DST), **![UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time)** offset, etc.


## Installing
This library can be installed by using `pip install worldtimepy`. Doing so will automatically install all requirements.
## Requirements
This library requires you to have ![requests](https://docs.python-requests.org/en/master/), ![unidecode](https://pypi.org/project/Unidecode/), and ![countryinfo](https://pypi.org/project/countryinfo/). All of those can be installed using `pip`.

## Using the wrapper
### *class* **worldtime.WorldTime()**
This is the main class through which you should interact with the API.

##### _**`.locations`**_

> Has all existing locations from WorldtimeAPI.

*return* **list**
<br>

##### _**`.from_ip(ip: str='') -> TimeInfo` optional argument: ip**_

> Takes an IP and returns a corresponding TimeInfo object with timezone information for that IP. If no IP is provided, it will use the requesting IP.

*return* **TimeInfo**
<br>

##### _**`.find_by_name(name: str) -> list`**_

> Takes a string and returns a list of strings for all locations that contain that name.

*return* **list**
<br>

##### _**`.search(name: str) -> str`**_

> Takes a country name or a city name and tries to find it in the database. It returns a string that can be used by `get_location()`.

Warning: This function iterates through different databases to try and locate the query. It may be slow.

*return* **string**
<br>

##### _**`.get_location(location: str) -> object`**_

> Takes a proper location taken from `search` or `find_by_name` and returns a _**TimeInfo**_ object.

*return* **TimeInfo**
<br>

##### _**`.refresh()`**_

> Gathers new data for `self.locations`.

*No return*
<br>

### *class* **timeinfo.TimeInfo(to_get=0, ip: bool=False)**
This class takes a location found through one of the other methods and makes an object with information for that timezone.
You can use any location from *worldtime.WorldTime().locations* here.

Alternatively, if you set *ip* to True, you may provide an IPv4 address on *to_get* to get time information for that IP. If ip is set to True and nothing is given to *to_get*, the machine's IP will be used.

Printing or turning this object into a string returns a prettier string containing time information.
```bash
2021-06-11 00:14:14.378300 UTC-0700
```

##### _**`.result`**_

> Full json pulled from the API.

*return* **dict**
<br>

##### _**`.week_day`**_

> Returns current day of the week.

*return* **int**
<br>

##### _**`.year_day`**_

> Returns current day of the year.

*return* **int**
<br>

##### _**`.week_number`**_

> Returns current number of the week of the year.

*return* **int**

<br>

##### _**`.datetime`**_

> Returns an aware ![datetime object](https://docs.python.org/3/library/datetime.html).

*return* **datetime**
<br>

##### _**`.datetime_str`**_

> Returns a string version of a datetime object.

*return* **str**

<br>

##### _**`.abbreviation`**_

> Returns a string representing the abbreviated format of the timezone. E.g. 'PST'

*return* **str**

<br>

##### _**`.is_dst`**_

> Returns whether timezone is in daylight savings time.

*return* **bool**

##### _**`.dst_offset`**_
##### _**`.dst_from`**_
##### _**`.dst_until`**_

 <br>
 
##### _**`.unixtime`**_

> Returns a unix like time integer.

*return* **int**
<br>

##### _**`.utc`**_

> Returns the UTC time..

*return* **str**

##### _**`.utc_offset`**_
##### _**`.raw_offset`**_

