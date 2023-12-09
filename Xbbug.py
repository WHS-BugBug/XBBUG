import argparse
import random
from modes.subdomain import subdomain
from modes.katana import katana
from modes.dalfox import dalfox
from config.logo import logo
from modes.requester import load_user_agents

# 0. basic settings

# main logo
logo()

user_agents = load_user_agents()
user_agent = random.choice(user_agents)

# argument setting
parser = argparse.ArgumentParser(description='XSS automated detection framework')
parser.add_argument('-u', '--url', required=True, help='input url ex) naver.com, enki.co.kr', dest='url')
parser.add_argument('-ds', '-do-not-search-subdomains', action='store_true', help="Don't search for subdomains")
parser.add_argument('-d', '-depth', help="maximum depth to crawl of katana (default 3)", default=3, dest='depth')
parser.add_argument('-rd', '-delay', help="Milliseconds between send to same host of dalfox (1000==1s)", dest='delay', default=0)
parser.add_argument('-H', '-header', help="Add custom headers of dalfox", dest='header', default=f"User-Agent: {user_agent}")

args = parser.parse_args()

url = args.url
dont_search_subdomains = args.ds
depth = args.depth
delay = args.delay
header = args.header

if not dont_search_subdomains:
    subdomain_list = subdomain(url)
    param_list = katana(subdomain_list, dont_search_subdomains, depth)
    dalfox(param_list, delay, header)
else:
    param_list = katana(url, dont_search_subdomains, depth)
    dalfox(param_list, delay, header)
