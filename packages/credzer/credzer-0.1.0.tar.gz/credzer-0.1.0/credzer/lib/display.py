import json
from tinydb import TinyDB, Query

def display(db,arg):
    db=TinyDB(db)
    if(arg=='cleartext'):
        Entry = Query()
        entries=db.search(Entry.clear_password!="")
        for entry in entries:
            prettyPrint(entry)

def prettyPrint(entry):
    print( "%s\%s:%s"%(entry['domain'],entry['username'],entry['clear_password']))