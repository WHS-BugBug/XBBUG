# XBBUG Guide English ver.

## Usage options

```
usage: Xbbug.py [-h] [-u URL] [-l LIST] [-ds] [-d DEPTH] [-rd DELAY] [-H HEADER] [-w WORKER]

XSS automated detection framework

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Input url ex) naver.com, enki.co.kr
  -l LIST, --list LIST  Input The file of the domains
  -ds, --do-not-search-subdomains
                        Don't search for subdomains
  -d DEPTH, --depth DEPTH
                        Maximum depth to crawl of katana (default=3)
  -rd DELAY, --delay DELAY
                        Milliseconds between send to same host of dalfox (1000==1s)
  -H HEADER, --header HEADER
                        Add custom headers of dalfox
  -w WORKER, --worker WORKER
                        Number of worker in Dalfox (default=100)
```

## XSS detection after subdomain collection

Option: `-u` or `--url`

Performing subdomain discovery using subfinder and httpx tools, followed by XSS vulnerability scanning.

`python3 Xbbug.py -u example.com`

## Detect XSS after specifying a subdomain file

Option: `-l` or `--list`

Conducting XSS vulnerability scanning by specifying a subdomain file.

`python Xbbug.py -l subdomain.txt`

## Detect XSS for a single URL

Option: `-ds` or `--do-not-search-subdomains`

Conducting XSS vulnerability scanning for a specific single domain without exploring subdomains.

`python Xbbug.py -u example.com -ds`

## Katana crawl depth setting

Option: `-d` or `--depth`| Default: `3`

This option allows you to specify the crawling depth of the Katana tool.

`python Xbbug.py -u example.com -d 5`

## Dalfox Delay setting

Option: `-rd` or `--delay`| Default: `0`

This option allows you to specify the interval between requests sent to the same host in the Dalfox tool.(1000==1s)

`python Xbbug.py -u example.com -rd 2000`

## Dalfox user header setting

Option: `-H` or `--header`

This option allows you to add custom headers in the Dalfox tool.

`python Xbbug.py -u example.com -H "Cookie: asd=qwer"`

## Dalfox worker count setting

Option: `-w` or `--worker`| Default: `100`

This option allows you to set the number of workers in the Dalfox tool.

`python Xbbug.py -u example.com -w 200`
