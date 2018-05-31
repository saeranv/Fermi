import csv
import datetime
import os
import requests # this library makes html requests much simpler


"""
Source: http://oco-carbon.com/coding/wunderground-data-to-csv/
Credit Jamie Bull
"""

# Add your API key (from wunderground) here
api_key = "58d02ed0e924a9b4"
station_ids = ["KDCA"]#,"KDCWASHI167"] # add more stations here if required
csv_path = "C:/Users/631/Desktop"
state = "DC"
city = "Washington"

for station_id in station_ids:
    #print station_id
    csv_path = os.path.abspath(os.path.join(csv_path, station_id))
    print "Fetching data for station ID: {}" .format(station_id)
    try:
		# initialise your csv file
        outfile = open('%s.csv' % csv_path, 'wb')
        writer = csv.writer(outfile)
        headers = ['date','temperature']#,'wind speed'] # edit these as required
        writer.writerow(headers)

        # enter the first and last day required here
        start_date = datetime.date(2016,1,1)
        end_date = datetime.date(2016,2,20)

        date = start_date
        while date <= end_date:
            print date, end_date

            # format the date as YYYYMMDD
            date_string = date.strftime('%Y%m%d')
            # build the url
            # to get airport data(?)
            url = "http://api.wunderground.com/api/{}/history_{}/q/{}/{}.json".format(api_key,date_string,state,city)
            #url = ("http://api.wunderground.com/api/%s/history_%s/q/%s.json" % (api_key, date_string, station_id))
            # make the request and parse json
            data = requests.get(url).json()
            # build your row
            #print data['response']['features']['history']
            #print 'chkthis', data['history'].has_key('observations')#data.has_key('history')
            for history in data['history']['observations']:
                row = []
                row.append(str(history['date']['pretty']))
                row.append(str(history['tempm']))
                #row.append(str(history['wspdm']))
                writer.writerow(row)
            # increment the day by one
            date += datetime.timedelta(days=1)
            #"""
    except Exception as e:
        print 'failed wunderground extraction', e
        # tidy up
        #os.remove(csv_path)

outfile.close()

print "Done!"
