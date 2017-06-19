username = ''   # your username/email
password = ''

































import mechanize
import urllib2
import time
import cookielib
import requests

   # your password

br = mechanize.Browser()

# browser settings (used to emulate a browser)
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_debug_http(False)
br.set_debug_responses(False)
br.set_debug_redirects(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

br.open('https://www.odoo.com/web/login') 

br.select_form(nr=0)
 

br['login'] = username
br['password'] = password
br.submit() 
 
cookies = cookielib.LWPCookieJar()
br.set_cookiejar(cookies)
print cookies
temp_jar=br.set_cookiejar(cookies)
print temp_jar
result = (br.response().read()) 
 
f=file('s.html', 'w')
f.write(result)
f.close()
