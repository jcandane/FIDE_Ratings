# FIDE_Ratings
Get the Distribution of FIDE Rated Chess Players Worldwide

Although different National Chess Federations and FIDE have different scales for their rating, a universal unit of measuring a players profermence is percentile.

Has two functions to get Percentile or Rating given the other. This program works by downloading a zip file from FIDE website containing
all the plauers data (http://ratings.fide.com/download). It then unzips this file to create a .TXT file that is converted into a NumPy array.

Roughly speaking the FIDE titles correspond to:
WCM ~ top 18.00 percentile
WFM ~ top 11.00 percentile
CM  ~ top  5.00 percentile *also WIM
FM  ~ top  2.00 percentile *also WGM
IM  ~ top  1.00 percentile
GM  ~ top  0.25 percentile
SGM ~ top  0.01 percentile *not offical title
