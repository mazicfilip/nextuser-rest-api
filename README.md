# Websites REST API

Websites REST API Test code

* Create virtual environment venv in nextuser-rest-api directory and activate it
    ```console
  source venv/bin/activate
    ```
* Install requirements from requirements.txt file
  ```console
  pip install -r requirements.txt
  ```
* Migrate database
    ```console
  python3 manage.py migrate
    ```
* Create superuser user
    ```console
  python3 manage.py createsuperuser
    ```
* Run application on port 8080
    ```console
  python3 manage.py runserver 8080
    ```
  
* Go to http://localhost:8080/admin/ login and create new API Key. Upon creating an API key from the admin, the full API key is shown only once in a success message banner. This is what should be passed in authorization headers. After creation, only the prefix of the API key is shown in the admin site, mostly for identification purposes. If you lose the full API key, you'll need to regenerate a new one.
* Pass API key via the Authorization header. It must be formatted as follows:
```
Authorization: Api-Key <API_KEY>
```
* Test application