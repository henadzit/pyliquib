# PyLiquib

A tool for MongoDB migrations with PyMongo.

## Overview
Pyliquib was inspired by Liquibase which is a java tool for migrations on relational databases. Pyliquib is
a migration tool for MongoDB and pymongo based applications.

## Usage
Define an iterable object of change sets and submit it to `pyliquib.run` along with a reference to
the database you want to maintain. Pyliquib tracks already executed change sets, so, only new change sets will
be executed.

For now pyliquib supports two types of change sets. They are a python callback and inline javascript code.
A python callback is created by a call of `pycall` with `id`, `author` and reference to python function
which should take a `pymongo.database.Database` as an argument. An inline js change set is created by
a call of `js` with `id`, `author` and a string object containing javascript code which will be executed
on the MongoDB side.

Define change sets:

    from pyliquib import pycall, run, js
    change_sets = (
        pycall('1',             # change set id which must be unique
            'user@example.com', # author of the change set
            __1,                # python function which takes a db reference
            'A comment. It's optional.'),
        js('2', 'user2@example.com',
            'db.users.update({}, {password_hash: {"$set": null}}, {multi: true})') # a plain javascript code which will be
                                                                    # executed on the MongoDB side once
		pycall('3', 'user@example.com', __3, always=True) # set always=True if you need the change set is run each time
    )

Run pyliquib:

	run(MongoClient().test, change_sets)

Extend change_sets when you need new migrations. That's it.

## Implementation notes

Pyliquib uses two collections for service purposes. LIQUIB_LOCK is used for preventing concurrent issues.
LIQUIB_LOG is used for tracking already executed change sets.

## Examples

See the example package for examples. It's pretty simple.