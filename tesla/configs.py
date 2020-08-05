#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#############################################
# @Author: jlei1
# @Date:   2020-06-21
# @Last Modified By:   jlei1
# @Last Modified Time: 2020-06-22
#############################################

QUERY_LIMIT = 20000
EVENT_START = '2017-01-01'
EVENT_END = '2017-12-31'
EVENT_COUNT_URL = f'https://earthquake.usgs.gov/fdsnws/event/1/count?starttime={EVENT_START}&endtime={EVENT_END}'
EVENT_DTL_URL = f'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={EVENT_START}&endtime={EVENT_END}&limit={QUERY_LIMIT}'

HEADERS = {
"Content-Type": "application/json",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

# for only question 5 
QUERY_4_Q5 = """
SELECT * 
  FROM earthquakes 
 WHERE mag=(SELECT MAX(mag) FROM earthquake);
"""

# one-time query, do not run it once more
QUERY_4_Q6_1 = """
CREATE TABLE earthquake_frequency AS
SELECT 
       mag,
       hour_of_day,
       num_of_earthquake
  FROM (
		SELECT 
		       STRFTIME("%H", DATETIME(time/1000.0, 'unixepoch', 'localtime')) AS hour_of_day,
		       CASE WHEN mag < 1 THEN '0-1'
		            WHEN mag >= 1 and mag < 2 THEN '1-2'
		            WHEN mag >= 2 and mag < 3 THEN '2-3'
		            WHEN mag >= 3 and mag < 4 THEN '3-4'
		            WHEN mag >= 4 and mag < 5 THEN '4-5'
		            WHEN mag >= 5 and mag < 6 THEN '5-6'
		            WHEN mag >= 6 THEN '>6' 
		        END AS mag,
               COUNT(1) AS num_of_earthquake
          FROM earthquakes
         WHERE mag >= 0
         GROUP BY STRFTIME("%H", DATETIME(time/1000.0, 'unixepoch', 'localtime')),
                  CASE WHEN mag < 1 THEN '0-1'
		             WHEN mag >= 1 and mag < 2 THEN '1-2'
		             WHEN mag >= 2 and mag < 3 THEN '2-3'
		             WHEN mag >= 3 and mag < 4 THEN '3-4'
		             WHEN mag >= 4 and mag < 5 THEN '4-5'
		             WHEN mag >= 5 and mag < 6 THEN '5-6'
		             WHEN mag >= 6 THEN '>6' 
		         END
	   ) aa
ORDER BY mag, num_of_earthquake DESC;
"""

# final query
QUERY_4_Q6_2 = """
SELECT aa.mag, 
       aa.hour_of_day AS hour_of_highest_possibility
  FROM earthquake_frequency aa
  JOIN (SELECT mag, MAX(num_of_earthquake) max_num FROM earthquake_frequency GROUP BY mag) bb
    ON aa.mag = bb.mag AND aa.num_of_earthquake = bb.max_num
 GROUP BY aa.mag, aa.hour_of_day
 ORDER BY aa.mag ASC;
"""

# for viz
QUERY_4_Q6_3 = """
SELECT 
       mag,
       hour_of_day,
       num_of_earthquake
  FROM (
		SELECT 
		       STRFTIME("%H", DATETIME(time/1000.0, 'unixepoch', 'localtime')) AS hour_of_day,
		       CASE WHEN mag < 1 THEN '0-1'
		            WHEN mag >= 1 and mag < 2 THEN '1-2'
		            WHEN mag >= 2 and mag < 3 THEN '2-3'
		            WHEN mag >= 3 and mag < 4 THEN '3-4'
		            WHEN mag >= 4 and mag < 5 THEN '4-5'
		            WHEN mag >= 5 and mag < 6 THEN '5-6'
		            WHEN mag >= 6 THEN '>6' 
		        END AS mag,
               COUNT(1) AS num_of_earthquake
          FROM earthquakes
         WHERE mag >= 0
         GROUP BY STRFTIME("%H", DATETIME(time/1000.0, 'unixepoch', 'localtime')),
                  CASE WHEN mag < 1 THEN '0-1'
		             WHEN mag >= 1 and mag < 2 THEN '1-2'
		             WHEN mag >= 2 and mag < 3 THEN '2-3'
		             WHEN mag >= 3 and mag < 4 THEN '3-4'
		             WHEN mag >= 4 and mag < 5 THEN '4-5'
		             WHEN mag >= 5 and mag < 6 THEN '5-6'
		             WHEN mag >= 6 THEN '>6' 
		         END
	   ) aa
 ORDER BY mag, hour_of_day, num_of_earthquake;
"""