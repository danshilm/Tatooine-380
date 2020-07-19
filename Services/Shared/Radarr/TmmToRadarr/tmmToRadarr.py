import sqlite3
from sqlite3 import Error
import csv
from pathlib import Path
from datetime import datetime
import requests
import sys

base_path = Path(__file__).parent
database = (base_path / "./nzbdrone.db").resolve()
RADARR_API_KEY = "RADARR_API_KEY_HERE"
RADARR_API_URL = "http://localhost:7878/api/command"

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def get_movies_data_from_tmm():
    """
    open csv file
    csv file structure: [0 => title, 1 => TmdbId, 2 => path]
    read movie data into a list
    """
    file_path = (base_path / "./Exported/movielist.csv").resolve()
    allMoviesData = []

    with open(file_path, mode='r') as infile:
        reader = csv.reader(infile, delimiter='|')
        allMoviesData = []
        for line in reader:
            # ignore line separator and last empty line
            if line[0] == 'sep=' or not line[0]:
                continue
            # I have a directory only for 4K movies that I don't share on Plex but use TMM to manage them, so they show up in the exported list if I mis-select when exporting in TMM
            # this is just a safeguard 
            if "/media/TheVault/PlexMediaServer/Movies-4K/" in line[2]:
                continue
            line[2] = line[2].replace(
                "/media/TheVault/PlexMediaServer/Movies/", "/data/movies/")
            allMoviesData.append(line)

    return allMoviesData

def query_for_radarr_ids(conn, movies):
    """
    query db for id, path, title, TmdbId
    returns a list [0 => TmdbId, 1 => Title, 2 => Path, 3 => Id]
    """
    sql = '''SELECT "TmdbId", "Title", "Path", "Id" FROM Movies WHERE '''

    for i, movie in enumerate(movies):
        if i == (len(movies)-1):
            sql += "\"TmdbId\" = '" + movie[1] + "';"
        else:
            sql += "\"TmdbId\" = '" + movie[1] + "' OR "

    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    return rows

def trigger_radarr_rescan(radarrMovieId):
    headers = {'X-Api-Key': RADARR_API_KEY}
    payload = {'name': 'RefreshMovie', 'movieId': radarrMovieId}

    r = requests.post(RADARR_API_URL, json=payload, headers=headers)

def update_task(conn, task):
    """
    update path for each matching tvdbId
    :param conn:
    :param task:
    """
    sql = ''' UPDATE Movies
              SET Path = ?
              WHERE TmdbId = ?'''

    cur = conn.cursor()
    cur.execute(sql, task)
    result = cur.rowcount
    conn.commit()
    return result

def updateRadarrEntries():
    # create a database connection
    print("Opening database: nzbdrone.db...")
    conn = create_connection(database)
    print("Getting movies data from TMM export csv list...")
    allMoviesDataFromTMM = get_movies_data_from_tmm()
    numberOfMoviesToUpdate = len(allMoviesDataFromTMM)
    numberOfMoviesUpdated = 0

    print("Updating records in database...")
    with conn:
        for movieData in allMoviesDataFromTMM:
            result = update_task(conn, (movieData[2], movieData[1]))
            if (result == 1):
                numberOfMoviesUpdated += 1
            print("Updating record for " +
                  movieData[0] + ": " + (("NOPE", "OK")[result == 1]))

    conn.close()
    print("Movies updated: " + str(numberOfMoviesUpdated) + "/" + str(numberOfMoviesToUpdate))

def rescanUpdatedRadarrMovies():
    # create a database connection
    print("Opening database: nzbdrone.db...")
    conn = create_connection(database)
    print("Getting movies data from TMM export csv list...")
    allMoviesDataFromTMM = get_movies_data_from_tmm()
    print("Getting movies ids from Radarr...")
    allMoviesData = query_for_radarr_ids(conn, allMoviesDataFromTMM)
    numberOfMoviesToUpdate = len(allMoviesData)
    numberOfMoviesUpdated = 0

    print("Triggering Rescan for movies...")
    with conn:
        for movieData in allMoviesData:
            trigger_radarr_rescan(movieData[3])

    conn.close()
    print("Done")

if __name__ == '__main__':
    globals()[sys.argv[1]]()
