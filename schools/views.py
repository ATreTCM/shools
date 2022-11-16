'''from aiohttp import web
import models


async def index(request):
    async with request.app['models'].acquire() as conn:
        cursor = await conn.execute(models.Lesson.select())
        records = await cursor.fetchall()
        lessons = [dict(q) for q in records]
        return web.Response(text=str(lessons))'''

