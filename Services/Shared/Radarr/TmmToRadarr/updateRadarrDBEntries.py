import sqlite3
from sqlite3 import Error
import csv
from pathlib import Path
from datetime import datetime

base_path = Path(__file__).parent

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

def getMoviesData():
    # open csv file
    # read movie and tmdbId into a list
    file_path = (base_path / "./Exported/movielist.csv").resolve()
    allMoviesData = []

    with open(file_path, mode='r') as infile:
        reader = csv.reader(infile)
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
            # print(line)
            allMoviesData.append(line)

    return allMoviesData

def update_task(conn, task):
    """
    update path for each matching tvdbId
    :param conn:
    :param task:
    """
    sql = ''' UPDATE Movies
              SET Path = ?
              WHERE TmdbId = ?'''

    # print(sql)
    cur = conn.cursor()
    cur.execute(sql, task)
    result = cur.rowcount
    conn.commit()
    return result

def main():
    database = (base_path / "./nzbdrone.db").resolve()

    print("=================== ", datetime.now(), " ===================")

    # create a database connection
    print("Opening database: nzbdrone.db...")
    conn = create_connection(database)
    print("Getting movies data from TMM export csv list...")
    allMoviesData = getMoviesData()
    numberOfMoviesToUpdate = len(allMoviesData)
    numberOfMoviesUpdated = 0

    print("Updating records in database...")
    with conn:
        for movieData in allMoviesData:
            result = update_task(conn, (movieData[2], movieData[1]))
            if (result == 1):
                numberOfMoviesUpdated += 1
            print("Updating record for " +
                  movieData[0] + ": " + (("NOPE", "OK")[result == 1]))
            
    conn.close()
    print("Movies updated: " + str(numberOfMoviesUpdated) + "/" + str(numberOfMoviesToUpdate))
    
if __name__ == '__main__':
    main()
