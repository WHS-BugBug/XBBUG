# XBBUG 사용법 가이드

## 사용 옵션

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

## 서브도메인 수집 후 XSS 탐지

옵션: `-u` 또는 `--url`

subfinder와 httpx 도구를 사용하여 서브도메인 탐지를 진행한 후 XSS 취약점 스캐닝을 진행합니다.

`python3 Xbbug.py -u example.com`

## 서브도메인 파일을 지정 후 XSS 탐지

옵션: `-l` 또는 `--list`

서브도메인 파일을 지정하여 XSS 취약점 스캐닝을 진행합니다.

`python Xbbug.py -l subdomain.txt`

## 단일 URL에 대해 XSS 탐지

옵션: `-ds` 또는 `--do-not-search-subdomains`

서브도메인을 탐색하지 않고 해당 단일 도메인만 XSS 취약점 스캐닝을 진행합니다.

`python Xbbug.py -u example.com -ds`

## Katana 크롤링 깊이 설정

옵션: `-d` 또는 `--depth`| 기본값: `3`

이 옵션을 사용하면 Katana 도구의 크롤링 깊이를 지정할 수 있다.

`python Xbbug.py -u example.com -d 5`

## Dalfox Delay 설정

옵션: `-rd` 또는 `--delay`| 기본값: `0`

이 옵션을 사용하면 Dalfox 도구에서 동일한 호스트로 보내는 간격을 지정할 수 있다.(1000==1s)

`python Xbbug.py -u example.com -rd 2000`

## Dalfox 사용자 헤더 설정

옵션: `-H` 또는 `--header`

이 옵션을 사용하면 Dalfox 도구에서 사용자 헤더를 추가할 수 있다.

`python Xbbug.py -u example.com -H "Cookie: asd=qwer"`

## Dalfox worker 수 설정

옵션: `-w` 또는 `--worker`| 기본값: `100`

이 옵션을 사용하면 Dalfox 도구에서 worker 수를 설정할 수 있다.

`python Xbbug.py -u example.com -w 200`
