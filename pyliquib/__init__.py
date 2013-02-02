import logging
import threading
import time

from constants import *
from pyliquib.inlinejs import InlineJsChangeSet
from pyliquib.pycallback import PyCallbackChangeSet

logger = logging.getLogger('pyliquib')

def run(db, change_sets):
	__run(db, change_sets)

def pycall(id, author, callback, comment=''):
	return PyCallbackChangeSet(id, author, callback, comment)

def js(id, author, js, comment=''):
	return InlineJsChangeSet(id, author, js, comment)

def __run(db, change_sets, lock=threading.RLock()):
	with lock:
		try:
			if not __acquire_liquib_lock(db):
				raise ValueError("Couldn't acquire database lock. Please check the %s collection" % LIQUIB_LOCK)

			__ensure_id_index(db)

			processed_ids = set()
			for cs in change_sets:
				# MongoDB unique index isn't enough for checking id uniqueness because
				# a second occurrence of an id will be skipped as it is already processed
				# even if it's a different change set
				if cs.id in processed_ids:
					raise ValueError("Duplicate id: %s" % cs.id)

				cs.execute(db)
				processed_ids.add(cs.id)
		finally:
			__release_liquib_lock(db)

def __ensure_id_index(db):
	db[LIQUIB_LOG].ensure_index('id', 1, unique=True)

def __acquire_liquib_lock(db, sleep_time_secs=10):
	logger.info('Acquiring lock...')
	lock_collection = db[LIQUIB_LOCK]
	lock = lock_collection.find_one()
	if not lock:
		lock = {'locked': True}
		lock_collection.insert(lock)
		return True
	else:
		for i in range(1, 6):
			if lock['locked']:
				logger.info('Database is locked. Waiting for %d seconds.', sleep_time_secs)
				time.sleep(sleep_time_secs)
			else:
				lock_collection.update({}, {"$set": {'locked': True}})
				return True
	return False

def __release_liquib_lock(db):
	db[LIQUIB_LOCK].update({}, {"$set": {'locked': False}})