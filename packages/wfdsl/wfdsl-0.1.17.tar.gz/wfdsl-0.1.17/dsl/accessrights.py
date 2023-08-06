class AccessRights:
    NotSet = 0x00
    Read = 0x01
    Write = 0x02
    Owner = 0x07
    Request = 0x8
    
    @staticmethod
    def hasRight(rights, checkRight):
        if checkRight == 0:
            return rights == 0
        return (rights & checkRight) == checkRight
    
    @staticmethod
    def requested(rights):
        return AccessRights.Requested(rights, AccessRights.Request)
    
    @staticmethod
    def readRequested(rights):
        return AccessRights.Requested(rights) and (AccessRights.Requested(rights, AccessRights.Read) or AccessRights.Requested(rights, AccessRights.Write))
    
    @staticmethod
    def writeRequested(rights):
        return AccessRights.Requested(rights) and AccessRights.Requested(rights, AccessRights.Write)
    
    @staticmethod
    def rights_to_string(checkRights):
        if checkRights & AccessRights.Owner:
            return "Owner"
        
        rightStr = ""
        if checkRights & AccessRights.Request:
            rightStr = "Request"
        else:
            if checkRights & AccessRights.Read:
                rightStr = "Read"
            if checkRights & AccessRights.Write:
                rightStr += "Write"
            
        return rightStr