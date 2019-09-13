import pagespeed

api_key = ""

try:
    ps = pagespeed.PageSpeed(api_key)
    url_list = ["http://developers.google.com", "http://google.com"]
    for i in range(0, len(url_list)):
        res = ps.analyse(url_list[i])
        res.pretty_print()
except ValueError as e:
    print(e)
