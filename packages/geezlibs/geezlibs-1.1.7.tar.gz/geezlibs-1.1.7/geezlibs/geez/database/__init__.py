import motor.motor_asyncio

from config import MONGO_URL
cli = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

from geezlibs.geez.database.gbandb import *
from geezlibs.geez.database.gmutedb import *
from geezlibs.geez.database.pmpermitdb import *
from geezlibs.geez.database.rraid import *