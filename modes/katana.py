import subprocess
from config.check_protocol import check_protocol

def katana(subdomains, dont_search_subdomains, depth):
    print("[+] katana start")
    
    if not dont_search_subdomains:
            subdomain_list = subdomains
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
    
    print("[+] total katana result: ")
    for u in param_list:
        print(u)

    return param_list