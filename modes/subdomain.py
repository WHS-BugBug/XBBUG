import subprocess

def clean_up(subdomains):
    subdomain_list = []
    for url in subdomains:
        if url.startswith('http'):
            subdomain_list += [url]
    return subdomain_list

def subfinder_command(url):
    print("[+] subfinder start")
    basic_subfinder_command = f"/bin/subfinder -d {url} -silent | tee subdomains.txt"
    subdomains = subprocess.run(basic_subfinder_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("[+] subfinder result:")
    print(subdomains.stdout)

def httpx_command(domains_file):
    print("[+] httpx start")
    if domains_file:
        basic_httpx_command = f"/bin/httpx -l {domains_file} -silent -follow-redirects -mc 200"
    else:
        basic_httpx_command = f"/bin/httpx -l subdomains.txt -silent -follow-redirects -mc 200"
    clear_subdomains = subprocess.run(basic_httpx_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("[+] httpx result:")
    clean_subdomains = clean_up(clear_subdomains.stdout.split())
    
    for url in clean_subdomains:
        print(url)

    return clean_subdomains

def subdomain(url, domains_file):
    subfinder_command(url)
    subdomain_list = httpx_command(domains_file)
    
    return subdomain_list
