import asyncio
from src.Slash.Commands.pomostop import command_pomostop as adminstop

async def stop(ctx, SM):
    LOOP = asyncio.get_event_loop()
    LOOP.run_until_complete(adminstop(ctx, SM))
    return