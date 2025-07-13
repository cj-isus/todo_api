import asyncio
import asyncpg

async def test_connection():
    conn = await asyncpg.connect(
        user='todo_user',
        password='12345',
        database='todo_db',
        host='localhost',
        port=5432
    )
    print("Successfully connected to PostgreSQL!")
    await conn.close()

asyncio.run(test_connection())