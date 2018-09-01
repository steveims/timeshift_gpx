# https://gis.stackexchange.com/a/199942
#
# do not set start time to match any existing ride (error)
# also change gpx.trk.name to be unique for the time period (seems necessary for Strava Flyby to show the ride for comparison)

import datetime
from bs4 import BeautifulSoup
import re
import os
import sys

import argparse

tformat = '%Y-%m-%dT%H:%M:%SZ'

parser = argparse.ArgumentParser()
parser.add_argument('gpx_file')
parser.add_argument('start_time', help='specified in UTC with this format: yyyy-mm-ddThh:mm:ssZ')
args = parser.parse_args()



with open(args.gpx_file, 'r') as f:
    xml = f.read()
    bx = BeautifulSoup(xml, 'xml')

    td = datetime.datetime.strptime(bx.metadata.time.text, tformat) - datetime.datetime.strptime(args.start_time, tformat)

    times = bx.find_all('time')
    for stime in times:
        timestr = stime.text
        rawtime = datetime.datetime.strptime(timestr, tformat)
        rawtime = rawtime - td
        stime.string.replace_with(rawtime.strftime(tformat))
    new_filename = args.gpx_file + '_'
    with open(new_filename,'w') as g:
        g.write(bx.prettify())
    print 'converted %s to %s' % (file,new_filename)
    sys.stdout.flush()
print 'done converting'
