# timeshift_gpx

Useful for grouping multiple rides in Strava to enable comparison with Strava's Flyby tool.

Setup (tested with python 2.7):
1. virtualenv venv
1. pip install beautifulsoup4
1. pip install lxml

Run:
1. download GPX data from Strava (e.g. Morning_Ride.gpx)
1. note the start time of the other ride in the comparison (e.g. 2018-08-25T11:05:35Z);
   pick a shifted start time that's close, but not the same (e.g. one minute off)
1. python adjust_start.py Morning_Ride.gpx '2018-08-25T11:06:35Z'
1. mv Morning_Ride.gpx_ Morning_Ride2.gpx
1. edit gpx.trk.name to make the name distinct from the other ride in the comparison
1. upload Morning_Ride2.gpx
1. use Strava Flyby

