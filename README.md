# Zsub
This is a website subdomoin Finder tool it can find 10 milion + subdomins . 
The Website Subdomain Finder is a simple and effective tool designed to help users discover subdomains associated with a given domain name. This tool performs automated subdomain enumeration and returns a list of possible subdomains for a target website, making it useful for security professionals, website administrators, and developers looking to understand the structure of a website more deeply.

Features:

Automated Subdomain Discovery:
The tool uses multiple techniques and APIs to find all available subdomains for a given domain.
Multiple Source Integration: It pulls information from multiple online sources, DNS records, and common subdomain patterns.
Easy to Use: A user-friendly interface or command-line interface (CLI) to quickly input a target domain and retrieve subdomains.
Fast Results: Returns results in a matter of seconds with minimal user input.
Open-Source: Fully open-source and available for modification, enabling users to contribute or improve the tool.

Technologies Used:
Python (or specify the programming language you're using)
Requests Library: For making HTTP requests to online APIs and services.
DNS Query Tools: To extract DNS records and associated subdomains.

How It Works:
The user inputs a target domain into the tool.
The tool queries different APIs, search engines, and DNS records to enumerate subdomains.
Results are displayed in a list format, showing the discovered subdomains.


Usage:  
" Zsub.py -h " For Help 
" Zsub.py -d " To Select terget Domain 
" Zsub.py -w " Adding WORDLIST Of Subdomins 

Installation:

Clone the repository:

    https://github.com/shazed-x/zsub.git

Install dependencies:

    pip install -r requirements.txt

Run the tool:

    python3 Zsub.py -d exampul.com -w Subdomain.txt

![screenshots] :

![Zsub_ss_1.png](<https://media-hosting.imagekit.io//700e556a3ca947ac/Zsub_ss_1.png?Expires=1835463836&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=hYBZKULvFVwDRNZPZisHOJMoerr16nbme6laYkeDoo2gdDxc3dhREDEanAkkjbTlZdLffxDTZyG4-bvVULb39sSxN4b-QES8RKJkCZ87SFZi~GNv0im9tF-HSJQpxyn4tkup3jM~Hq-lreM6pcFAN~aJbcv1kfakqymxFxQgSG~5IWoiluEsOWO0dGnhYWSJLpWQsHxNwznZHDqQ6meH01WyKobW2jIc0NHEQfY~pPV7rorqH6Hw9qOQg0Pp0PRvR0V0lPmL0XIulsgjjEgkVCirQTJatSER0FpR6kQSeQtMAJ3BvBL2UhbkUeEL0CQVyBdnzReVFBvhXv8dFd-RPw__>)
![Zsub_ss_2.png](<https://media-hosting.imagekit.io//f2f653d7a2ea405c/Zsub_ss_2.png?Expires=1835463836&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=3DkHzPbs2LXMZqBYhwuKnlaaZXdCqo6RSxJ2LwNxUzM3PzJcO44YtuMevnDQjdNJCdJ-3dhsfFpCt4xSBwLF8421mNNbHs2jvBWBvHDp~OZqHWq5w-BykahCVxIQ3JH4RV7PjVsDUt~WQqc1Zvq6r82hFTEApHMz8z1Os6uy0r9nrfPjw3voQNFmHvun6j9dalIztQLiLJ5cUavThb7qqHt9vnHExcqrCTHFBsbE3ku450M1NXctt0iWUKOrduE0iqAHI5lpND-rRlkSqF2ac7FVd69BLU8UsLYsAfrA7Ymlgim6AT3Syo8MNKMdmQ2vTmuZtm37T1m~Il6QzbZ4Gw__>)
![Zsub_ss_3.png](<https://media-hosting.imagekit.io//005b4c9e4acc4069/Zsub_ss_3.png?Expires=1835463836&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=JfGDa740Pp8GwRjlKnueGqSOaqJYEihTpCHKmvM-ZZNv72ps8i2jRUOVsU3f6qqMmLXDhW3nYfm3fBVinVSvCsjhvynvuyByOyeduQCLWx5fpoFbbu7TgCeUGdLZDzVCu0GQs~GM7I6wsdSxNwdqnYy8wOSehuaVDXK6xogkSXVAcMP1X~OXUgcpOz1w5DfNqo1v~--IRajjVk52TH2EB2fOwxEMOz7NC0aD6zBFBmUPq0OkBqqAHi21B7xdH~G-PCD9Cb-tD8KhLsD89RJeKk~1YeyZ~IhnAETLyVM-i8NvIvGh1hFqfVbRhFLq70-PPUCy-VFD6NV~4YHHy~1MOg__>)
![Zsub_ss_4.png](<https://media-hosting.imagekit.io//a620ea2370c84686/Zsub_ss_4.png?Expires=1835463836&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=n0fn129i53EueMLta2CE5zzNzGI49fJkVPxuPoMZUS-bWoVS~IVJ~RB1H9LcF2jR7nkszBUD~Qpg~6n~XwkZ1rm837e8FUm-Q1P-E3NnQZtX0lSUMUxCjR9FjHmSigXs1gqDLo6mx3f~f1F1JQqumobfp3RgtB1yFYjp3OrAdZlCrHHAqEvP74P3kP4f69OFTul~POLVNRXLoVYHUXYeyELsEVxUWqV7R45038ICATdCd~-be5HMHeutZMtTMjUwdZBEbvw9CNQ7LR6eBeTWwVrPwklh3bU1JkTSRmwP6bvxHU8z-3NI2ReZJio0ubWX9YXuNB~DG-Hd7Ch50DALQA__>)
![Zsub_ss_5.png](<https://media-hosting.imagekit.io//87b4a8cd6c5a4302/Zsub_ss_5.png?Expires=1835463771&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=QYkk-tgGBHaEAZ7-KAC9LB4kf4fkf9rgJfOA3Z632H9svbIFKK0wtr7rF0A9QJfbGCNcj8-jFic6ujdvHXpwEYGY87nEhmcnPSzs-FmEgtjwPeajQjxz0ou793FcFu6SxWcLD-DACDpQO6urWUlp5GPGDOoY4kogXelrlpwY7M7IOUmxSoyXcAiYEVcaZFA0LRm2ItvWZagJ-nV6c638DAatKFmEYzq4eJxsgQ5WlA-W86lVEFbOpaJbWXspxLPMhng3DQRfvOAjziUMcGACWPcr1RWIsF5c5qgtDn2uTDnwOcr6~NfJJkvVF4ztbC12kB1FSzlpNj1S9NBWJliFAA__>)
### Visitors :
![Visitor Count](https://profile-counter.glitch.me/shazed-x/count.svg)
