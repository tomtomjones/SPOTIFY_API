# Spotify_API Improvements

## Description

Possible improvements to this project, and any further changes that could help grow the project

## Suggested Improvements

- Store the secret key in a system environment variable, I was unsure how this would work in OS other than windows
- Combine the deconstruct modules
- try and utilise one loop to handle the json objects/lists. The structure of the json responses from spotify were all different, again easier to handle with pandas maybe
- Utilise offset calls to fetch more than the default limit of 50 items from the API
- I used as few libraries as i could, but considering how much better Pandas is at handling JSON files, i would use this when adding more API responses
- Implement data snapshots to track changes in playlists and tracks over time
- I believe there is a cap of 100 tracks returned in a playlist, would need to utilize offset calls for this also
- Increase test coverage, i've added very basic tests. But would need to expand to test all extracts
- Include a logging_config.py file for proper debugging and tracking of events. I simply used print() for debugging since this was a smaller project
- in the documentation for limits, i read somewhere you can use snapshot_id to retrieve a 'cached/historical' playlist. this could help when the project is making a lot more API requests. Same for retrieving Album tracks, can send requests for tracks from multiple albums in one call. this wasn't required for this project scope

- Flask front end hosted locally to allow variable inputs like playlists returned limits and different categories. Would allow graphs and other basic BI tooling options. pandas and matplotlib
- Separate test cases into smaller separate modules with relevent test names for better clarity. I think this is better practice than all in one module like i have
- Implement a scheduling mechanism to automatically run the script on a daily basis, collecting stats on followers/playlist size and similar
- Data storage by implementing incremental storage of data, nosql/sqlite? Can perform better querying over time
- Utilise spotipy lirary, giving better metrics to track and analyze the popularity of songs over time
- Enhance error handling by replicating what i did for the make_api_call, providing better error messages and a clearer idea of where it occurred, and tie this in with the logging_config
- I could add a notification mechanism to receive email/text updates and alerts on playlist and track changes.
