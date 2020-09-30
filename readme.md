# IMDB Task

● Problem Description:

. Create a RESTful API for movies(something similar to IMDB). For this we would like you to use:

1. MySql or SQLlite to store data
2. Any Python Framework for implementing the APIs.

There need to be 2 levels of access:
admin = who can add, remove or edit movies.
users = who can just view the movies.

. There should also be a decent implementation to search for movies.

. Document your code well so that we can test the API with ease.

. For your convenience I have attached some data that you can use to populate your database

. Try and deploy this on Heroku. Ensure that you parse the JSON file and ingest it into the application deployed on Heroku.

. Feel free to add features!

------------------------------------------------------------------------------------------------------------------------
Implementation as Follows :

Framework for API :

    . Django
    . Django REST Framework

Database for API :
    
    .SQLlite (for Heroku server, as it doesn't support MySQL)
    
Project Link Of Heroku :

https://imdb-task--fynd.herokuapp.com/ __

Admin Credentials:
**username - chopra**
**password - 133001**
 
----
* **Question:**
    `Once deployed suppose this application became very famous and started to receive a ton of traffic. 
    Your application now contains metadata about 5M movies and receives 15M API hits per day both from anonymous 
    as well as authenticated users. 
    Suggest an architecture to scale up this system to 5x of these specs. 
    You can also think of potential bottlenecks at all layers of the stack and how will you solve for these.`
    
    **Answer**
    
    * Load Balancer
        we can use services like AWS Elastic Load Balancer or HA Proxy, through which we deploy code on multiple server.
    
    * Database
    
        Each web server must serve same content, hence should talk to same database. 
        If many web server talking to one db server, it will become bottle neck. 
        Even if there is one web server, sometimes db server may become bottle neck. 
        mysql server supports master-slave and master-master configuration.And we can index multiple columns for fast
        searching and sorting.
    
        * In master-slave one server is master where data is written and it is replicated to multiple slave servers. 
        In this case write is done on master and read from slaves. 
        This is useful when very few write happens on database but many reads. 
        typically less than 10-15% of write but depends on the use case.
    
        * In master-master is similar to above but all are masters, any data written to any server gets replicated to other servers. 
        Read and write can be done on any server. This is useful for applications which have high writes.
        Above is for mysql but similar kind of scalability is supported by other database servers too.
    
    * Redis Server(caching)

        For data shown in homepage, we can store in redis. Like the first 10 movies in the redis server
    
    * Elastic Search
    
        For search we can use elastic search, name of the movie we can store in it