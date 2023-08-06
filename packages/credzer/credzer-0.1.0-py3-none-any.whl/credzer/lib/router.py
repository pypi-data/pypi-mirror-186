from tinydb import TinyDB, Query
from credzer.lib.parser import cme, msf, ntlm, ntlmv2, hashcat_ntlm_potfile, hashcat_ntlmv2_potfile
from credzer.lib.display import display

def router(args):
    source=""
    if(args.source):
        source=args.source[0]
    
    if(args.source and not args.file):
        print("File location is expected")
        exit(-1)
    else:
        #Source Args
        if(source=='cme'):
            cme()
        if(source=='ntlm'):
            ntlm(args.database,args.file)
        if(source=='hashcat_ntlm'):
            hashcat_ntlm_potfile(args.database,args.file)
        if(source=='hashcat_ntlmv2'):
            hashcat_ntlmv2_potfile(args.database,args.file)
        if(source=='ntlmv2'):
            ntlmv2(args.database,args.file)

    #Search Args
    if(args.search=='cleartext'):
        display(args.database,'cleartext')
        