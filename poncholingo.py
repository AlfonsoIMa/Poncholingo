import sqlite3, logging, question

# TODO
"""
JSON with progress / Récords
CLI
"""

# CONSTANTS
VERSION = "v0.1 ALPHA 24_02a"
DOMINANCE = {
    'PERCIBIDO'   :1000,
    'COMPRENDIDO' :2000,
    'DOMINADO'    :3000,
    'PRINCIPIANTE':200,
    'CAMINANTE'   :400,
    'TRATANTE'    :600,
    'REPOSANTE'   :800,
    'DOMINANTE'   :000,
}
CURSOR = ''
logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(message)s', datefmt = '%m/%d/%Y %I:%M:%S %p')
log = logging.getLogger().setLevel(logging.INFO)

def main() -> int:
    logging.info(f'Initializing Poncholingo {VERSION}')
    try:
        CURSOR = initialize_database('poncholingo.sqlite', 'poncholingo_db.sql')
        while True:
            choice = select_training()
            if(choice == 0):
                # logging.info("User chose to exit. Exiting…")
                CURSOR.connection.commit()
                CURSOR.connection.close()
                break
            elif(choice == 1):
                question.ask_nouns()
    except Exception as e:
        raise e
    return 0

def select_training() -> int:
    while True:
        try:
            choice = int(input("Select Option:\n1.- Train Nouns"))
            break
        except ValueError as e:
            pass
    return choice

def initialize_database(database: str, init_query: str) -> sqlite3.Cursor:
    connection = sqlite3.connect(database)
    cursor     = connection.cursor()
    with open(init_query, 'r') as queries:
        for query in queries.readlines():
            # logging.info(f"Running: {query}")
            cursor.execute(query)
        connection.commit()
    return cursor

if __name__ == '__main__':
    main()