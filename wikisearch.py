import pywikibot

site = pywikibot.Site('en', 'wikipedia') # Site to run the bot on.

page = pywikibot.Page(site, 'Wikipedia:Sandbox')

page.text = page.text.replace('foo', 'bar')
page.save('Replacing "foo" with "bar"') # saves the page