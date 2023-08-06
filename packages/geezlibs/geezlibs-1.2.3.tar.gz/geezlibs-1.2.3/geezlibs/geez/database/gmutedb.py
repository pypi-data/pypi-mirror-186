import motor.motor_asyncio

from config import MONGO_URL

cli = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

gmuteh = cli["GMUTE"]


async def is_gmuted(sender_id):
    kk = await gmuteh.find_one({"sender_id": sender_id})
    return bool(kk)


async def gmute(sender_id, reason="#GMuted"):
    await gmuteh.insert_one({"sender_id": sender_id, "reason": reason})


async def ungmute(sender_id):
    await gmuteh.delete_one({"sender_id": sender_id})
