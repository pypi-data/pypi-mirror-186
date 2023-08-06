class Datamodel:
    def __init__(self,domain,username,full_username,lm_hash,nt_hash,ntlmv2,clear_password):
        self.domain=domain
        self.username=username
        self.full_username=full_username
        self.lm_hash=lm_hash
        self.nt_hash=nt_hash
        self.ntlmv2=ntlmv2
        self.clear_password=clear_password
    
#    def displayObject(self):
#        return self.username

    def insertObject(self):
        return {"domain":self.domain,"username":self.username,"full_username":self.full_username,"lm_hash":self.lm_hash,"nt_hash":self.nt_hash,"ntlmv2":self.ntlmv2,"clear_password":self.clear_password}

