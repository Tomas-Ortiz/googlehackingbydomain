# Google Hacking By Domain

- "GoogleHackingByDomain" is a pentest tool that allows you to automate advanced Google queries from a domain name.
- It provides 11 different options to search for sensitive information and security vulnerabilities.
  1. Subdomains
  2. Directory Listing
  3. Login and registration pages
  4. Files
  5. Keywords
  6. Default pages
  7. Software versions
  8. Error messages
  9. Databases
  10. Email addresses and phone numbers
  11. Employees
- In the results shown, the magenta color represents the title, the green the link and the yellow the description.
- Queries are executed in Spanish and English.
- The results obtained are saved in a text file, in the same path where the script is located.
- Google's "Custom Search API" is used. This API is limited to 100 free queries per day.
- Due to limited queries, the first page of results is returned. Only for some queries the first two pages of results are returned.
- This tool works for Windows and Linux.
- Due to the nature of Google searches, it is possible to obtain unwanted, repetitive or false positive results.

For this tool to work you must generate and obtain an API Key for "Custom Search API" and create a Programmable Search Engine. The steps are described below.

1. Download the script on your computer <br/>
          - git clone https://github.com/Tomas-Ortiz/googlehackingbydomain

2. Access the downloaded folder <br/>
          - cd googlehackingbydomain

3. Install the required modules <br/>
          - pip install google-api-python-client colorama

4. Generate API Key for "Custom Search API" <br/>
          - https://developers.google.com/custom-search/v1/introduction

5. Create a Programmable Search Engine and get the Search Engine ID (CX) <br/>
          - https://programmablesearchengine.google.com/controlpanel/create 

6. Insert your API Key and search engine ID into the variables indicated in the source code of the script (API_KEY and CX) <br/>

7. Finally, you can use the tool <br/>
          - python3 GoogleHackingByDomain.py 

8. Additionally, you can use the google console to control enabled APIs, credentials, queries, usage and so on <br/>
          - https://console.cloud.google.com/apis/dashboard

<br/>
Some screenshots showing how the tool works are attached below. <br/>
<br/>

<img src="https://user-images.githubusercontent.com/56492312/210282729-c98f75b2-86d4-483c-8c3c-d93f8664f948.png" width=65% height=65%>

<img src="https://user-images.githubusercontent.com/56492312/210282782-4b4ca83c-4311-4c0c-bd96-a095fab4f81c.png" width=65% height=65%>

<img src="https://user-images.githubusercontent.com/56492312/210284407-3b09422e-e9c3-4767-89f7-d1db9d36024a.png" width=65% height=65%>

<img src="https://user-images.githubusercontent.com/56492312/210285537-572eb5c1-5adc-434b-9e18-89710281e95b.png" width=65% height=65%>

<img src="https://user-images.githubusercontent.com/56492312/210284749-ca864fc1-ddc6-4bb9-bed5-1c9f3b5c889c.png" width=75% height=75%>

<img src="https://user-images.githubusercontent.com/56492312/210285212-d6bf538c-bc43-48bc-8363-85dab5c97f4c.png" width=70% height=70%>

<img src="https://user-images.githubusercontent.com/56492312/210284198-e3d947aa-b359-441b-ad18-3306e8d2c460.png" width=70% height=70%>

<img src="https://user-images.githubusercontent.com/56492312/210282540-5b0b5321-a9c2-4886-9387-bb5ca9b836e2.png" width=65% height=65%>

<img src="https://user-images.githubusercontent.com/56492312/210283158-05ab0eb8-a66b-4ede-9001-99832e3b08fe.png" width=65% height=65%>
