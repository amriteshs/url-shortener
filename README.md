# url-shortener
Web-based URL shortener

**STEPS TO RUN THE APPLICATION**

1.) Unzip the url-shortener.zip file.

2.) Run the following commands:  
(a) With Docker (PRE-REQUISITES: Docker Desktop should be installed and running)
```
cd url-shortener/
docker compose up -d --build
docker compose exec web python manage.py migrate
```    
(b) Without Docker
```
cd url-shortener/src/urlshortener
python manage.py migrate
python manage.py runserver
```

3.) Open localhost:8000 in a web browser. 

4.) In the text field, enter a URL to be shortened and click on the "Generate Short URL" button. This will generate a short URL for the original URL. To view the list of short URLs generated by the user and the number of times they have been used, click on the "See All URLs" button, which will display the data in a tabular format. 


**RUNNING THE TESTS**

To run the unit tests, navigate to the directory containing the manage.py file and run the following commands:
```
python manage.py test
```
