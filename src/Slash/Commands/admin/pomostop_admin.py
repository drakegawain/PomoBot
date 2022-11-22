import asyncio
import nextcord
from ..pomostop import command_pomostop as adminstop

async def stop(ctx:nextcord.Interaction, SM):
    LOOP = asyncio.get_event_loop()
    LOOP.run_until_complete(adminstop(ctx, SM))
    return