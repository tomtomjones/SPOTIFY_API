# Spotify API Project

This project is a Python application that interacts with the Spotify Web API to fetch information about playlists and tracks. Playlists are retrieved from a given category, limits can be set in the code. The project returns 6 datasets, extracted as csv.gz files. 
My result dataset files are available under the data directory.
- Playlist returned limit can be set in the playlist_limit variable in main.py.
- Playlist category can be set in the playlist_category variable in main.py.

- My answers to the SQL challenge are stored in /docs, and the Python question 2 write up can be found here also.
 
## Project Structure

The project follows what i believe to be a standard Python project structure:

```
spotify_api_project/
├── data/
│   ├── artists_records.csv.gz
│   ├── category_playlist_records.csv
│   ├── playlist_records.csv
│   ├── playlist_track_id_records.csv
│   ├── track_artist_id_records.csv
│   ├── tracks_records.csv
│   └── json_samples/
│       └── response.json
├── tests/
│   ├── __init__.py
│   └── test_spotify_api.py
├── docs/
│   ├── python_improvements.py
│   └── sql_answers/
│       ├── sql_question_1.sql
│       └── sql_question_2.sql
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── compress_csv_handler.py
│   ├── csv_handler.py
│   ├── deconstruct_category.py
│   ├── deconstruct_playlist.py
│   ├── tocken_auth.py
│   ├── scratchpad.py
│   └── config/
│       ├── __init__.py
│       ├── config.ini.template
│       └── logging_config.py
├── README.md
├── requirements.txt
├── .gitignore
└── setup.py
```
- `data/`: Contains my dataset solution files. json_samples are used during testing, ignore
- `tests/`: Includes unit tests for some very basic Spotify API functionalities.
- `main.py`: Run this script. Details below. The main Python script that interacts with the Spotify Web API. 
- `README.md`: This file, providing an overview of the project and instructions for running and testing the application.
- `requirements.txt`: A list of Python dependencies required to run the project.
- `.gitignore`: Specifies which files or directories should be ignored
- `config/`: Holds configuration files, to setup the absolute path regardless of machine and the sets up the config.ini in config.util.

## Setup and Installation

1. Clone the repository:

```bash
git clone https://github.com/tomtomjones/spotify_api.git
```

2. Create and activate a virtual environment :

```bash
# cd spotify_api
python -m venv venv
source venv/bin/activate  # On Windows, use `soruce venv\Scripts\activate`
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Obtain Spotify API credentials:

   Get the client ID and client secret from the Spotify app. Update these credentials in the `config.ini.template` file. Rename this file to config.ini

## Running the Application

Run the application by executing the `main.py` script:

```bash
python src/main.py
```

## Running Tests

To run the unit tests, execute the following command:

```bash
python -m unittest discover tests
```



## Contributions

You break you fix
