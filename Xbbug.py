import argparse
import random
from modes.subdomain import subdomain
from modes.subdomain import httpx_command
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
parser.add_argument('-u', '--url', help='Input url ex) naver.com, enki.co.kr', dest='url')
parser.add_argument('-l', '--list', type=argparse.FileType('r'), help="Input The file of the domains")
parser.add_argument('-ds', '--do-not-search-subdomains', action='store_true', help="Don't search for subdomains")
parser.add_argument('-d', '--depth', help="Maximum depth to crawl of katana (default=3)", default=3, dest='depth')
parser.add_argument('-rd', '--delay', help="Milliseconds between send to same host of dalfox (1000==1s)", dest='delay', default=0)
parser.add_argument('-H', '--header', help="Add custom headers of dalfox", dest='header', default=f'"User-Agent: {user_agent}"')
parser.add_argument('-w', '--worker', help="Number of worker in Dalfox (default=100)", dest='worker', default=100)

args = parser.parse_args()

if not args.url and not args.list:
    parser.error("Please choose between -u or -l options")

if args.url and args.list:
    parser.error("You cannot select both -u and -l options")

if args.list and args.do_not_search_subdomains:
    parser.error("You cannot select both -l and -ds options")

url = args.url
dont_search_subdomains = args.do_not_search_subdomains
depth = args.depth
delay = args.delay
header = args.header
domains_file = args.list
worker = args.worker

if domains_file:
    print("[+] domains:")
    for url in domains_file:
        print(url.strip())
    print()

    domain_list = httpx_command(domains_file.name)
    param_list = katana(domain_list, dont_search_subdomains, depth)
    dalfox(param_list, delay, header, worker)
else:
    if not dont_search_subdomains:
        subdomain_list = subdomain(url, domains_file)
        param_list = katana(subdomain_list, dont_search_subdomains, depth)
        dalfox(param_list, delay, header, worker)
    else:
        param_list = katana(url, dont_search_subdomains, depth)
        dalfox(param_list, delay, header, worker)
