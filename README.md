<center><h1>XBBUG</h1></center>
The XBBUG is an open source framework that automatically scans for Cross Site Scripting(XSS) vulnerabilities.

The XBBUG framework uses Subfinder, httpx, Katana, and Dalfox tools.

The XBBUG Framework supports:

-   Find subdomains using subfinder and httpx tools.
-   Find endpoints and parameters using Katana tools.
-   Detect XSS vulnerabilities using the Dalfox tool.

<center><h2>Flowchart</h2></center>
<center><img src="./assets/XBBUG Flowchart.png" alt="XBBUG Flowchart"></center>
<br/>

<center><h2>Getting started</h2></center>

```sh
sh setup.sh
```

<center><h2>XBBUG Framework Guide</h2></center>

-   [guide-ko-documentation](./GUIDE_ko.md)
-   [guide-en-documentation](./GUIDE_en.md)

#### (1) Find subdomains.

<center><img src="./assets/subfinder_httpx.gif" alt="XBBUG Flowchart"></center>

#### (2) Find endpoints and parameters.

<center><img src="./assets/Katana.gif" alt="XBBUG Flowchart"></center>

#### (3) Detect XSS vulnerabilities.

<center><img src="./assets/Dalfox.gif" alt="XBBUG Flowchart"></center>

<center><h2>Reference</h2></center>

-   subfinder(https://github.com/projectdiscovery/subfinder)

-   httpx(https://github.com/projectdiscovery/httpx)

-   katana(https://github.com/projectdiscovery/katana)

-   Dalfox(https://github.com/hahwul/dalfox)

<center><h2>Contact</h2></center>

-   whitehacker.roronoa@gmail.com

<center><h2>Contributor</h2></center>

-   Jeongwoo Lee ([@Roronoawjd](https://github.com/Roronoawjd))
-   Seongmin Yoon ([@Potato12351](https://github.com/Potato12351))
-   Hongjun Seo ([@hjthink2](https://github.com/hjthink2))
-   Yeonjun Park ([@yeo0n](https://github.com/yeo0n))
-   Seunghwan Lee ([@EL55](https://github.com/EL55))
-   Minjun Bae ([@bmj4004](https://github.com/bmj4004))
-   PL: Sanghyun Lee ([@isanghyeon](https://github.com/isanghyeon))
-   Mentor: Joowon Kim ([@arrester](https://github.com/arrester))

<center><h2>Acknowledgement</h2></center>

This work was supported by Korea Information Technology Research Institute (KITRI) WhiteHat School Program 1st.

**[Project Name: Bug bounty optimization through web automation tool analysis]**
