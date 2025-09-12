import asyncio
import aiosqlite

db_file = "../python-generators-0x00/ALX_prodev"

async def async_fetch_users():
    async with aiosqlite.connect(db_file) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT * FROM user_data;") as cursor:
            return await cursor.fetchall()

async def async_fetch_older_users():
    async with aiosqlite.connect(db_file) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT * FROM user_data WHERE age > 50;") as cursor:
            return await cursor.fetchall()

async def fetch_concurrently():
    users, older_users = await asyncio.gather(
            async_fetch_users(),
            async_fetch_older_users()
            )
    print("All users", [dict(row) for row in users])
    print("Older users", [dict(row) for row in older_users])

asyncio.run(fetch_concurrently())
