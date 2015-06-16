'''
Created on Jun 15, 2015

@author: Bryan

Implements two methods to get user input and process the claim of points from NCIX
Users enter their email and the claim ID
'''
'''
TODO

Add successful claim alert
'''
from splinter import Browser
import requests

def pointSubmitRequests(claimNumber, email):
    # Payload sent to the server as email and URL
    payload = 'email='+email+'&captcha=34114789&submit=+Claim+Bonus+&claimno='+claimNumber
    # Header to tell server form of data, and how to use it
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
               'Accept':' text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Language':' en-US,en;q=0.5',
               'Accept-Encoding':' gzip, deflate',
               'Referer':'http://secure.ncix.com/newsletterrewards.cfm?claimno='+claimNumber,
               'Cookie':' CFID=244; CFTOKEN=CF36DE84-8C3F-4F00-8D03345D255835A2; SECURESERVER=0; bdglobals=AAEAAAD/////AQAAAAAAAAAMAgAAAE1CbHVlRHJhZ29uLCBWZXJzaW9uPTcuMS4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49NzU1MTMzNWRlOWZjM2MzNgUBAAAAFWNvbS5uYXJ5LnV0aWwuSGFzaE1hcAcAAAAKTG9hZEZhY3RvcgdWZXJzaW9uC0tleUNvbXBhcmVyCEhhc2hTaXplBEtleXMGVmFsdWVzDWNhc2VTZW5zaXRpdmUAAAMABQUACwgWU3lzdGVtLk9yZGluYWxDb21wYXJlcggBAgAAAOxROD8GAAAACQMAAAALAAAACQQAAAAJBQAAAAAEAwAAABZTeXN0ZW0uT3JkaW5hbENvbXBhcmVyAQAAAAtfaWdub3JlQ2FzZQABARAEAAAABgAAAAYGAAAACHVybHRva2VuBgcAAAALdGltZWNyZWF0ZWQGCAAAAAhoaXRjb3VudAYJAAAABGNmaWQGCgAAAAlsYXN0dmlzaXQGCwAAAAdjZnRva2VuEAUAAAAGAAAACQwAAAAJDQAAAAkOAAAACQ8AAAAJEAAAAAkRAAAADBIAAABJdmpzbGliLCBWZXJzaW9uPTIuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49YjAzZjVmN2YxMWQ1MGEzYQUMAAAAK2NvbS5uYXJ5eC50YWdmdXNpb24uY2ZtLmVuZ2luZS5jZlN0cmluZ0RhdGENAAAABGRhdGEJZGF0YUJ5dGVzCWRhdGFDaGFycxRtYXliZURhdGVDb252ZXJ0aWJsZRZtYXliZU51bWJlckNvbnZlcnRpYmxlF21heWJlQm9vbGVhbkNvbnZlcnRpYmxlD2NmRGF0YStqYXZhY2FzdBBjZkRhdGErcmVmZXJlbmNlFWNmRGF0YStxdWVyeVRhYmxlRGF0YRJjZkRhdGErcXVlcnlDb2x1bW4RY2ZEYXRhK2V4cHJlc3Npb24RY2ZEYXRhK2lzSW1wbGljaXQXY2ZEYXRhK2ludmFsaWRMb29wSW5kZXgBBwcAAAAAAAQAAAAACgMBAQEKAQ5qYXZhLnV0aWwuTGlzdBIAAAAIAQEBAgAAAAYTAAAANENGSUQ9MjQ0JkNGVE9LRU49Q0YzNkRFODQtOEMzRi00RjAwLThEMDMzNDVEMjU1ODM1QTIKCgEBAQAACgAAAAAAAAAFDQAAACljb20ubmFyeXgudGFnZnVzaW9uLmNmbS5lbmdpbmUuY2ZEYXRlRGF0YQsAAAAEdGltZQpkYXRlU3RyaW5nDGZvcm1hdFN0cmluZxJmb3JtYXRTdHJpbmdQcmVmaXgPY2ZEYXRhK2phdmFjYXN0EGNmRGF0YStyZWZlcmVuY2UVY2ZEYXRhK3F1ZXJ5VGFibGVEYXRhEmNmRGF0YStxdWVyeUNvbHVtbhFjZkRhdGErZXhwcmVzc2lvbhFjZkRhdGEraXNJbXBsaWNpdBdjZkRhdGEraW52YWxpZExvb3BJbmRleAABAQEAAAQAAAAACQoBDmphdmEudXRpbC5MaXN0EgAAAAgBAQECAAAAT1qW/U0BAAAKBhQAAAATeXl5eS1NTS1kZCBISDptbTpzcwYVAAAAAnRzAAAKAAAAAAAAAAUOAAAAK2NvbS5uYXJ5eC50YWdmdXNpb24uY2ZtLmVuZ2luZS5jZk51bWJlckRhdGENAAAACGRvdWJsZU5vBWludE5vBmJJbnRObwhtb2RpZmllZA1pc0phdmFOdW1lcmljBWltYWdlD2NmRGF0YStqYXZhY2FzdBBjZkRhdGErcmVmZXJlbmNlFWNmRGF0YStxdWVyeVRhYmxlRGF0YRJjZkRhdGErcXVlcnlDb2x1bW4RY2ZEYXRhK2V4cHJlc3Npb24RY2ZEYXRhK2lzSW1wbGljaXQXY2ZEYXRhK2ludmFsaWRMb29wSW5kZXgAAAAAAAEAAAQAAAAABggBAQEKAQ5qYXZhLnV0aWwuTGlzdBIAAAAIAQEBAgAAAAAAAAAAAAAACQAAAAEBAAoAAAoAAAAAAAAAAQ8AAAAMAAAABhYAAAADMjQ0CgoBAQEAAAoAAAAAAAAAARAAAAANAAAAfgOv/U0BAAAKBhcAAAATeXl5eS1NTS1kZCBISDptbTpzcwYYAAAAAnRzAAAKAAAAAAAAAAERAAAADAAAAAYZAAAAI0NGMzZERTg0LThDM0YtNEYwMC04RDAzMzQ1RDI1NTgzNUEyCgoBAQEAAAoAAAAAAAAACw==; bdclient_NCIXDOTCOM2003=AAEAAAD/////AQAAAAAAAAAMAgAAAE1CbHVlRHJhZ29uLCBWZXJzaW9uPTcuMS4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49NzU1MTMzNWRlOWZjM2MzNgUBAAAAFWNvbS5uYXJ5LnV0aWwuSGFzaE1hcAcAAAAKTG9hZEZhY3RvcgdWZXJzaW9uC0tleUNvbXBhcmVyCEhhc2hTaXplBEtleXMGVmFsdWVzDWNhc2VTZW5zaXRpdmUAAAMABQUACwgWU3lzdGVtLk9yZGluYWxDb21wYXJlcggBAgAAAOxROD8MAAAACQMAAAALAAAACQQAAAAJBQAAAAAEAwAAABZTeXN0ZW0uT3JkaW5hbENvbXBhcmVyAQAAAAtfaWdub3JlQ2FzZQABARAEAAAAAAAAABAFAAAAAAAAAAs=; _ga=GA1.2.1577653027.1434478597; PAPVisitorId=8e47e20ccb6584208e7662a2axSESpbi; __asc=885e33cf14dfda0e3c35b647872; __auc=885e33cf14dfda0e3c35b647872; _gat=1',
               'Connection':' keep-alive',
               'Content-Type':' application/x-www-form-urlencoded'}
    # Send server data, get response from server
    response = requests.post('http://secure.ncix.com/newsletterrewards.cfm?claimno='+claimNumber, data=payload, headers=headers)
    # Alert received from the server, succeeded if Bonus is claimed or Points Added To Account
    if 'alert("Sorry, you have already claimed the Bonus");' in response.text:
        print 'succeeded'
    else:
        print 'failed'
    
    


def pointSubmit(claimNumber, email):
    # Set browser to use
    browser = Browser('firefox')
    browser.visit('http://secure.ncix.com/newsletterrewards.cfm?claimno='+claimNumber)
    # Enters email address
    browser.find_by_xpath('/html/body/table/tbody/tr/td/form/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/input[1]').type(email)
    # Finds Captcha
    captcha = browser.find_by_xpath('/html/body/table/tbody/tr/td/form/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/font[3]').first.value
    # Enters Captcha
    browser.find_by_xpath('/html/body/table/tbody/tr/td/form/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/input[2]').type(str(captcha))
    # Clicks 'Claim Bonus' button
    browser.find_by_xpath('/html/body/table/tbody/tr/td/form/table/tbody/tr[1]/td/div/table/tbody/tr[3]/td/input[1]').first.click()
    # Dismisseds the alert
    with browser.get_alert() as alert:
        alert.dismiss()

def main():
    email = raw_input("enter your email:    ")
    claimNumber = raw_input("enter Claim Number:    ")
    pointSubmit(claimNumber, email)
    pointSubmitRequests(claimNumber, email)

main()