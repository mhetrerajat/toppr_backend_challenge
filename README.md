# Toppr Backend Challenge

### Usage
Program requires Python 3.5.2

To run api
```
cd api
python3 run.py
```


### Features
1. Possible URLS
	- GET : [https://gotapi.herokuapp.com/stats](https://gotapi.herokuapp.com/stats) : Get GOT Stats
	- GET : [https://gotapi.herokuapp.com/list](https://gotapi.herokuapp.com/list) : Get entire list of battles
	- GET : [https://gotapi.herokuapp.com/list?type=region](https://gotapi.herokuapp.com/list?type=region) : Get distinct region of battles and number of battles at that region
	- GET : [https://gotapi.herokuapp.com/list?type=location](https://gotapi.herokuapp.com/list?type=location) : Get distinct locations of battles and number of battles at that location
	- GET : [https://gotapi.herokuapp.com/count](https://gotapi.herokuapp.com/count) : Get total count of battles
	- GET : [https://gotapi.herokuapp.com/search?name=<YOUR_QUERY>](https://gotapi.herokuapp.com/search?name=) : Search by name
	- GET : [https://gotapi.herokuapp.com/search?king=<YOUR_QUERY>](https://gotapi.herokuapp.com/search?king=) : Search by king
	- GET : [https://gotapi.herokuapp.com/search?type=<YOUR_QUERY>](https://gotapi.herokuapp.com/search?type=) : Search by type
	- GET : [https://gotapi.herokuapp.com/search?location=<YOUR_QUERY>](https://gotapi.herokuapp.com/search?location=) : Search by location
2. API is deployed on heroku.
3. Pylint is used for code analysis.


### Deployment
- API : [GOTApi](https://gotapi.herokuapp.com/)

### Notes
- API is implemented in Python with framework called **Flask**.
