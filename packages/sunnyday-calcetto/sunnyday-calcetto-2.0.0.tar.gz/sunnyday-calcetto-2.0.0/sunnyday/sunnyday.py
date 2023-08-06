import requests


class Weather:

    """
        Create a WEather object, taking as an input an apikey, a city name or lan and let coordinates.

        Package use example:
        # Create a Weather object using the city name:
        # The apikey below is not guaranteed to work.
        # Get your own apikey from openweathermap.org.
        # And wait a couple of hours for the apikey to get activated
        # The apikey could be activated even within minutes

        >>> weather = Weather(apikey='c4bcb6957g9e0b1ae584263c62fb5d3b', city='Vlore')

        # Using latitude and longitude coordinates
        >>> weather = Weather(apikey='c4bcb6957g9e0b1ae584263c62fb5d3b', lat=40, lon= -4)

        # Get complete weather data for the next 12 hours
        >>> weather.next_12h()

        # Simplified data for the next 12h
        >>> weather.next_12h_simplified()

        # Sample url to get sky condition items
        http://openweathermap.org/img/wn/10d@2x.png
    """

    def __init__(self, apikey, city=None, lat=None, lon=None):
        self.apikey = apikey
        self.city = city
        if city:
            url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=metrics'
            r = requests.get(url)
            self.data = r.json()
        elif lat and lon:
            url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apikey}&units=metrics'
            r = requests.get(url)
            self.data = r.json()
        else:
            raise TypeError("Provide either a city or lat and lon arguments")

        if self.data['cod'] != "200":
            raise ValueError(self.data["message"])

    def next_12h(self):
        """
            Returns 3-hour data for the next 12 hours as a dict.
        """
        return self.data['list'][:4]

    def next_12h_simplified(self):
        """
            Returns date, temperature, and sky condition every 3-hours for the next 12 hours as a touple of touples
        """
        simple_data = []
        for dicty in self.data['list'][:4]:
            simple_data.append((dicty['dt_txt'], dicty['main']['temp'],
                                dicty['weather'][0]['description'], dicty['weather'][0]['icon']))
        return simple_data
