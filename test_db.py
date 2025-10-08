import asyncio
import asyncpg

async def test_connection():
    try:
        conn = await asyncpg.connect('postgresql://workout:workout@localhost:5433/workout')
        print('Connection successful!')
        result = await conn.fetchval('SELECT 1')
        print(f'Query result: {result}')
        await conn.close()
        print('Connection closed successfully')
    except Exception as e:
        print(f'Connection failed: {e}')

if __name__ == '__main__':
    asyncio.run(test_connection())