from uuid import UUID

def IsValidGuid(guid, version = 4):
    try:
        Guid =UUID(guid, version=4)
    except ValueError:
        return False
    return str(Guid) == guid