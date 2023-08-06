from tinydb import TinyDB, Query
from credzer.lib.model import Datamodel

MAGIC_HASH="31d6cfe0d16ae931b73c59d7e0c089c0"

def cme():
    pass
def msf():
    pass
def ntlm(db,file):
    db = TinyDB(db)
    NewEntriesCount=0
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            splited = line.split(':')
            username = splited[0].lower()
            full_username=username
            domain=""
            if("\\" in username):
                username=full_username.split('\\')[1].lower()
                domain=full_username.split('\\')[0]
            full_hash=splited[2]+":"+splited[3]
            lm_hash=splited[2].lower()
            nt_hash=splited[3].lower()
            Entry = Query()
            if((db.search(Entry.username==username) and db.search(Entry.domain==domain)) or db.search(Entry.nt_hash==nt_hash)):
                pass
            else:
                datas = Datamodel(domain,username,full_username,lm_hash,nt_hash,"","")
                db.insert(datas.insertObject())
                NewEntriesCount+=1
        print("Add %s new entries" %(NewEntriesCount))
    pass

def hashcat_ntlm_potfile(db,file):
    db=TinyDB(db)
    NewEntriesCount=0
    Updated=0
    with open(file) as f:
        lines=f.readlines()
        for line in lines:
            if(not MAGIC_HASH in line):
                revLine=line.split(':')[::-1]
                clearPassword=revLine[0].strip()
                if(len(revLine[1])==32 and int(revLine[1],16)):
                    nt_hash=revLine[1].lower()
                    Entry = Query()
                    entries=db.search(Entry.nt_hash==nt_hash)
                    for entry in entries:
                        db.update({'clear_password':clearPassword},Entry.nt_hash==nt_hash)
                        Updated+=1
    print("[U] Updated : %s "%(Updated))
    pass

def ntlmv2(db,file):
    db=TinyDB(db)
    NewEntriesCount=0
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            username = line.split(':')[0].lower()
            domain = line.split(':')[2]
            full_username=domain+"\\"+username
            challenge = line.split(':')[3]
            response = line.split(':')[4]+":"+line.split(':')[5]
            ntlmv2 = challenge+":"+response
            ntlmv2= ntlmv2.strip().lower()
            Entry = Query()
            if(db.search(Entry.ntlmv2==ntlmv2) and db.search(Entry.clear_password=="")):
                pass
            else:
                datas = Datamodel(domain,username,full_username,"","",ntlmv2,"")
                db.upsert(datas.insertObject(),Entry.username==username)
                NewEntriesCount+=1
    print("Add %s new entries" %(NewEntriesCount))

def hashcat_ntlmv2_potfile(db,file):
    db=TinyDB(db)
    NewEntriesCount=0
    Updated=0
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            if(len(line.split(':'))==7):
                Entry=Query()
                username = line.split(':')[0].lower()
                domain = line.split(':')[2]
                full_username=domain+"\\"+username
                challenge = line.split(':')[3]
                response = line.split(':')[4]+":"+line.split(':')[5]
                ntlmv2 = challenge+":"+response
                ntlmv2 = ntlmv2.strip().lower()
                clear_password=line.split(':')[::-1][0].strip()
                datas = Datamodel(domain,username,full_username,"","",ntlmv2,clear_password)
                db.upsert(datas.insertObject(),Entry.ntlmv2==ntlmv2)
                NewEntriesCount+=1
    print("Updated %s "%(NewEntriesCount))
    pass