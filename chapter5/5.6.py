from datetime import datetime
someday = datetime(1998, 2, 28, hour=0, minute=0, second=0, microsecond=0)
print(someday.strftime("%Y,%m,%d"))
print(someday.strftime("%Y-%B-%d"))
print(someday.strftime("%A:%B:%Y"))