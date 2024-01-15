import requests
import datetime as dt
import smtplib

LATITUDE = -33.8698439
LONGITUDE = 151.2082848
_email = "codingclasses86@gmail.com"
_password = "sodrstwotkfizhos"
now = dt.datetime.now()
current_time = now.hour
parameters = {
    'Latitude': LATITUDE,
    'Longitude': LONGITUDE,
    'formatted': 0
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

sunrise = int((response.json()['results']['sunrise']).split('T')[1].split(':')[0])
sunset = int((response.json()['results']['sunset']).split('T')[1].split(':')[0])
print(sunset)

iss_response = requests.get(url='http://api.open-notify.org/iss-now.json')
iss_response.raise_for_status()
data = iss_response.json()['iss_position']
longitude = (data['longitude'])
latitude = data['latitude']
iss_position = (longitude, latitude)
current_position = (LONGITUDE, LATITUDE)
print(iss_position)

if (iss_position == current_position) and (sunset >= current_time or sunrise <= current_time):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=_email, password=_password)
        connection.sendmail(from_addr=_email,
                            to_addrs=_email,
                            msg="ISS in your area")
        print("successfully send")


# tuple1= (1,2,3)
# tuple2=(1,2,4)
# if tuple1 == tuple2:
#     print('match')