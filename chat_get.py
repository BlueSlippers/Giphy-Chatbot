

import mechanize
br = mechanize.Browser()
br.set_handle_robots( False )
br.open("http://elbot_e.csoica.artificial-solutions.com/cgi-bin/elbot.cgi")

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

#br.form = list(br.forms())[0]
#print br.form
for form in br.forms():
    print form

br.select_form(nr = 0)
br.form['ENTRY'] = 'Hello !'
br.submit()
br.response.read()
