bus-routes
==========

the API folder stores the api that would return a json for every GET request sent in a format.

Ex: A get request to the url: " http://routes1.herokuapp.com/start/end " will return the bus number(s) that connects start and end. Visiting the url from the browser will give the same result.


	requests.get('http://routes1.herokuapp.com/Ruby Hospital/Howrah')

	{
	  "number": [
	    107
	  			]
	}
	
specification
--------------

* The web app is somewhat ready but still I will be pushing in changes frequently to make it more efficient.
[webapp](http://busrecord.herokuapp.com/)

* I have used Flask(API) , [Mongodb](http://www.mongodb.org/) {database}. It is hosted on [Mongolab](https://mongolab.com/welcome/). The basic version gave me enough freedom to use it for my database.

* The database still does not have all entries yet, working on it :) 

* Feel free to make any necessary change if desired.



