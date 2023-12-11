import subprocess
from config.check_protocol import check_protocol, check_protocol_list

def clean_up(subdomains):
    subdomain_list = []
    for url in subdomains:
        if url.startswith('http'):
            subdomain_list += [url]
    return subdomain_list

def katana(subdomains, dont_search_subdomains, depth, domains_file):
    print("[+] katana start")
    
    if not dont_search_subdomains:
        if domains_file:
            subdomain_list = check_protocol_list(subdomains)
        else:
            subdomain_list = clean_up(subdomains)
    else:
        subdomains = check_protocol(subdomains)
        subdomain_list = [subdomains]
    
    param_list = []

    for url in subdomain_list:
        basic_katana_command = f"/bin/katana -u {url} -iqp -d {depth} -f qurl -silent -ef jpg,jpeg,png,gif,pdf,svg,json,css,swf,js,webp,woff,woff2,eot,ttf,otf,mp4,txt -cs {url} -aff"
        print(f"[+] query: {basic_katana_command}")
        param_urls = subprocess.run(basic_katana_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("[+] katana result:")
        print(param_urls.stdout)

        param_list += param_urls.stdout.split()

    return param_list