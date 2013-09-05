import time
from pymongo import MongoClient
from pyliquib import pycall, run


def __1(db):
    time.sleep(10)

# run the file with few threads
if __name__ == '__main__':
    change_sets = (
        pycall('1', 'user@example.com', __1, 'A sleeper'),
    )

    run(MongoClient().test, change_sets)