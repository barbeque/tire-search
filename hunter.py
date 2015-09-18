import requests
import time

url = "https://wl.tireconnect.ca/tireconnect.php/tireconnect/results?w=%(w)s&h=%(h)s&r=%(r)s&search_by=tire_size&dealer_id=3112&location_id=3158"

width = 155
rim_size = 12

heights = ["NONE",25,30,35,20,40,45,50,55,60,65,70,75,80,85,680,700,710,790,8.5,9.5,10.5,11.5,12.5,13.5,14.5,15.5]

for height in heights:
    print 'Trying %(width)s-%(height)s-%(rim_size)s...' % dict(width = width, height = height, rim_size = rim_size)
    new_url = url % dict(w = width, h = height, r = rim_size)

    r = requests.get(new_url)

    if r.status_code != 200:
        print 'Error code...' % r.status_code

    raw_html = r.text

    if not "no_tires" in raw_html: # the no tires found in this size div
        print "Found some tires holy wow"

    # go to sleep for a bit so we don't pound their server
    time.sleep(1)
