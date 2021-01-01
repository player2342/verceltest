## Run the API in dev environment

* Clone the repository from github
  ```sh
  git clone https://github.com/player2342/verceltest.git
  ```
  * Install the dependencies
  ```sh
  pip install -r requirements.txt
  ```
   * Update these variables `base_key, table_name, air_table_api_key` from `api/index.py` to match with your Airtable API informations.
   * Run the Flask API: the API will be served on http://localhost:8000/api by default
  ```sh
  python api/index.py
  ```
  ## API test

* Update the `url` variable in `index.html` to match with the server url.
* And make sure that the form intput names match exactly your airtable fields. For example, if you have Job field in airtable you must have an input like <input name="Job"> and it’s case sensitive
* Finally open `index.html` file in the browser or serve it with a static web server.
