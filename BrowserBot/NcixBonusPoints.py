'''
Created on Jun 15, 2015

@author: Bryan
'''
'''
TODO

Enter URL from commandline
Enter email addresses from commandline
Deal with popup
'''


from splinter import Browser

# Set browser to use
browser = Browser('firefox')
browser.visit('http://secure.ncix.com/newsletterrewards.cfm?claimno=2163869')
# Enters email address
browser.find_by_xpath('/html/body/table/tbody/tr/td/form/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/input[1]').type('sprigglespriggle@gmail.com')
# Finds Captcha
captcha = browser.find_by_xpath('/html/body/table/tbody/tr/td/form/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/font[3]').first.value
# Enters Captcha
browser.find_by_xpath('/html/body/table/tbody/tr/td/form/table/tbody/tr[1]/td/div/table/tbody/tr[2]/td/input[2]').type(str(captcha))
# Clicks 'Claim Bonus' button
browser.find_by_xpath('/html/body/table/tbody/tr/td/form/table/tbody/tr[1]/td/div/table/tbody/tr[3]/td/input[1]').first.click()