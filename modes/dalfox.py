import subprocess

def dalfox(param_list, delay):
    if delay:
        print("[+] dalfox start")
        for url in param_list:
            basic_dalfox_command = f'/bin/dalfox url "{url}" -d {delay}--waf-evasion --skip-mining-all --silence'
            print(f"[+] query: {basic_dalfox_command}")
            dalfox_result = subprocess.run(basic_dalfox_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print("[+] dalfox_result:")
            print(dalfox_result.stdout)
    else:
        print("[+] dalfox start")
        for url in param_list:
            basic_dalfox_command = f'/bin/dalfox url "{url}" --waf-evasion --skip-mining-all --silence'
            print(f"[+] query: {basic_dalfox_command}")
            dalfox_result = subprocess.run(basic_dalfox_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print("[+] dalfox_result:")
            print(dalfox_result.stdout)