## Python Pagespeed Batch Request
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fkevsersrca%2Fpypagespeed.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fkevsersrca%2Fpypagespeed?ref=badge_shield)


Example:

```python

import pagespeed

api_key = ""

try:
    ps = pagespeed.PageSpeed(api_key)
    url_list = ["http://developers.google.com", "http://example.com"]
    for i in range(0, len(url_list)):
        res = ps.analyse(url_list[i])
        res.pretty_print()
except ValueError as e:
    print(e)


```


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fkevsersrca%2Fpypagespeed.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fkevsersrca%2Fpypagespeed?ref=badge_large)