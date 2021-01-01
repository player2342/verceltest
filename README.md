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
   * Run the Flask API: the API will be served on 0.0.0.0:8000 by default
  ```sh
  python api/index.py
  ```
  
