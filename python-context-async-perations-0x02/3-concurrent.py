import asyncio
import aiosqlite

db_file = "../python-generators-0x00/ALX_prodev"

async def async_fetch_users(query):
    async with aiosqlite.connect(db_file) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(query) as cursor:
            return await cursor.fetchall()

async def async_fetch_older_users(query):
    async with aiosqlite.connect(db_file) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(query) as cursor:
            return await cursor.fetchall()

async def fetch_concurrently():
    users, older_users = await asyncio.gather(
            async_fetch_users("SELECT * FROM user_data;"),
            async_fetch_older_users("SELECT * FROM user_data WHERE age > 50;")
            )
    print("All users", [dict(row) for row in users])
    print("Older users", [dict(row) for row in older_users])

asyncio.run(fetch_concurrently())
