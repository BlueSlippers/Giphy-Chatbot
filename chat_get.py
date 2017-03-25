

import mechanize
import cache

def return_output_html(string):
    br = mechanize.Browser()
    br.set_handle_robots(False)

    br.open(cache.base_url)

    # User-Agent (this is cheating, ok?)
    br.addheaders = [('User-agent',
                      'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    br.select_form(nr=0)
    br.form['ENTRY'] = string

    response = br.submit()
    new_url = response.geturl()

    cache.base_url = new_url




