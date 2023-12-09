import argparse
from modes.subdomain import subdomain
from modes.katana import katana
from modes.dalfox import dalfox
from config.logo import logo

# 0. basic settings

# main logo
logo()

# argument setting
parser = argparse.ArgumentParser(description='XSS automated detection framework')
parser.add_argument('-u', '--url', required=True, help='input url ex) naver.com, enki.co.kr', dest='url')
parser.add_argument('-ds', '-do-not-search-subdomains', action='store_true', help="Don't search for subdomains")

args = parser.parse_args()

url = args.url
dont_search_subdomains = args.ds

if not dont_search_subdomains:
    subdomain_list = subdomain(url)
    param_list = katana(subdomain_list, dont_search_subdomains)
    dalfox(param_list)
else:
    param_list = katana(url, dont_search_subdomains)
    dalfox(param_list)