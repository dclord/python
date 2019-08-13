import requests
import json
import turtle
import time

print("-------- ISS Crew --------")
url = "http://api.open-notify.org/astros.json"

response = requests.get(url)
result = response.json()
print('People in Space: ', result['number'])

people = result['people']
for p in people:
		print(p['name'] + " - " + p['craft'])

print("\n", "-------- ISS Location --------")
print("\n", "-------- ISS Location --------")

locurl = "http://api.open-notify.org/iss-now.json"
locresponse = requests.get(locurl)
locresult = locresponse.json()

location =locresult['iss_position']
lat = location['latitude']
lon = location['longitude']
print('Latitude ', lat)
print('Longitude ', lon)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90 )
screen.bgpic('map.gif')

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(float(lon), float(lat))

# Wigan Location
lat = 53.5451
lon = -2.6325

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()

url = "http://api.open-notify.org/iss-pass.json"
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
response = requests.get(url)
result = response.json()

over = result['response'][1]['risetime']
style = ('Arial', 12, 'bold')
location.write(time.ctime(over), font=style)

turtle.exitonclick()
