the url of route planner: http://127.0.0.1:5002/planner

the web client sends the adresses in text form to the route planner, the route planner reads the current location from the redis database,
and the database sends all of the coordinates into the drone controller



(13.21008, 55.71106)                         (current coordinates)
(13.194348072345456, 55.70884481202657)       (coordinates of the from adress)
(13.191688376722102, 55.7107413)            (coordinates of the to adress)

The route planner got the current coordinates by reading them from the redis database, the other coordinates were sent as adressess in text form from
the script in index.html and turned into coordinates using nominatim
The pi controller got the coordinates as arguments when the route planner started the pi controller.

