# url_shortner1. 
1. Pip install -r requirments.txt

2. Start server by python3 app.py

3. Three api enpoints are provided as
    * SHORTEN URL
    ```
        localhost:5000/shorten_url/
        INPUT (Application/JSON)
        {
            "url":"http://www.google.com"
        }
        Expected Output (Application/JSON)
        {
            {"long_url": "http://localhost:5000/253d1"}
        }
     ```
    *  LONG URL
    ```
        http://localhost:5000/253d1
        Expected Output Redirected Website
    ```
    * Search keyword
     ```
        http://localhost:5000/search_key/google
        Expected Output (Application/JSON)
        [{"long_url": "http://www.google.com", "short_url": "http://localhost:5000/253d1"}]
      ```
