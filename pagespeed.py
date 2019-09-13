import requests, re
from responses import DesktopPageSpeed, MobilePageSpeed


class PageSpeed(object):
    """Google PageSpeed analysis client
    Attributes:
        api_key (str): Optional API key for client account.
        endpoint (str): Endpoint for HTTP request
    """

    def __init__(self, api_key):
        if api_key == "":
            raise ValueError("Api Key Not Found..")
        self.api_key = api_key
        self.endpoint = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed'

    def analyse(self, url, filter_third_party_resources=False, screenshot=False,
                strategy='desktop'):
        """Run PageSpeed test
        Args:
            url (str): The URL to fetch and analyse.
            filter_third_party_resources (bool, optional): Indicates if third party
                resources should be filtered out before PageSpeed analysis. (Default: false)
            locale (str, optional): The locale used to localize formatted results.
            rule (list, optional): A PageSpeed rule to run; if none are given, all rules are run
            screenshot (bool, optional): Indicates if binary data containing a screenshot should
                be included (Default: false)
            strategy (str, optional): The analysis strategy to use. Acceptable values: 'desktop', 'mobile'
        """
        if self.validate(url) == False:
            raise ValueError('invalid url input: {0}'.format(url))

        params = {
            'filter_third_party_resources': filter_third_party_resources,
            'screenshot': screenshot,
            'strategy': strategy,
            'url': url
        }

        strategy = strategy.lower()
        if strategy not in ('mobile', 'desktop'):
            raise ValueError('invalid strategy: {0}'.format(strategy))

        raw = requests.get(self.endpoint, params=params)

        if strategy == 'mobile':
            response = MobilePageSpeed(raw)
        else:
            response = DesktopPageSpeed(raw)

        return response

    def validate(self, url):
        pattern = re.compile("^(http:\/\/|https:\/\/)[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$")
        e = pattern.match(url)
        return bool(e)