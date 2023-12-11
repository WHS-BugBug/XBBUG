from modes.requester import requester

def check_protocol(target):
    if not target.startswith('http'):
        try:
            requester('https://' + target)
            target = 'https://' + target
        except:
            target = 'http://' + target
            
    return target

def check_protocol_list(target_list):
    subdomain_list = []

    for url in target_list:
        if not url.startswith('http'):
            try:
                requester('https://' + url)
                subdomain_list += ['https://' + url]
            except:
                subdomain_list += ['http://' + url]
        else:
            subdomain_list += [url]

    return subdomain_list