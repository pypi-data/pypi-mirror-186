class Countries:
    def __init__(self, countries_data: dict):
        self.iso_code: str = countries_data.get('isoCode')
        self.name: str = countries_data.get('name')
        self.native: str = countries_data.get('native')
        self.phone: str = countries_data.get('phone')
        self.continent: str = countries_data.get('continent')
        self.capital: str = countries_data.get('capital')
        self.currency: str = countries_data.get('currency')
        self.languages: list[str] = countries_data.get('languages')
        self.emoji: str = countries_data.get('emoji')
        self.emoji_u: str = countries_data.get('emojiU')


class CountryList:
    def __init__(self, country_list_data: dict):
        self.countries: list[Countries] = [Countries(item) for item in country_list_data.get('countries')]
