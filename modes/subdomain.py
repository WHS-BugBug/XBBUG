import subprocess

def subfinder_command(url):
    print("[+] subfinder start")
    basic_subfinder_command = f"/bin/subfinder -d {url} -silent | tee subdomains.txt"
    subdomains = subprocess.run(basic_subfinder_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("[+] subfinder result:")
    print(subdomains.stdout)

def httpx_command():
    print("[+] httpx start")
    basic_httpx_command = f"/bin/httpx -l subdomains.txt -silent -follow-redirects -mc 200"
    clear_subdomains = subprocess.run(basic_httpx_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("[+] httpx result:")
    print(clear_subdomains.stdout)
    print(clear_subdomains.stdout.split())

    return clear_subdomains.stdout.split()

def subdomain(url):
    subfinder_command(url)
    subdomain_list = httpx_command()
    
    return subdomain_list
