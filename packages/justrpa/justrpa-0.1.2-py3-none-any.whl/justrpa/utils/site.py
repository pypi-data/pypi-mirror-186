def get_site_short(site:str)->str:
    site_map = {
        "United States":"US",
        "United Kingdom":"UK",
        "Japan":"JP",
        "Germany":"DE",
        "Italy":"IT",
        "Canada":"CA",
        "Mexico":"MX",
        "Australia":"AU",
        "France":"FR",
        "Spain":"ES",
        "Netherlands":"NL",
        "Sweden":"SE",
        "Switzerland":"CH",
        "Poland":"PL"
    }
    if site not in site_map:
        return site.replace(" ", "")
    return site_map[site]

def get_amazon_home_url(site:str)->str:
    url_map = {
        "United States":"https://sellercentral.amazon.com/",
        "United Kingdom":"https://sellercentral.amazon.co.uk/",
        "Japan":"https://sellercentral-japan.amazon.com/"
    }
    if site in ["Italy", "United Kingdom", "France", "Spain", "Poland", "Sweden","Netherlands"]:
        site = "United Kingdom"
    elif site in ["Germany", "Canada", "Mexico", "United States"]:
        site = "United States"
    if site not in url_map:
        site = "United States"
    return url_map[site]

def get_site_short_cn(site:str)->str:
    site_map = {
        "United States":"美国",
        "Japan":"日本",
        "United Kingdom":"英国",
        "Canada":"加拿大",
        "Germany":"德国",
        "France":"法国",
        "Italy":"意大利"
    }
    if site not in site_map:
        return get_site_short(site)
    return site_map[site]