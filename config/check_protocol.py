from modes.requester import requester

def check_protocol(target):
    if not target.startswith('http'):
        try:
            requester('https://' + target)
            target = 'https://' + target
        except:
            target = 'http://' + target
            
    return target