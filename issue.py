import aiohttp
import asyncio
import os
from gidgethub.aiohttp import GitHubAPI


async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, os.getenv('GH_ACCOUNT'), oauth_token=os.getenv('GH_AUTH'))
        user = 'mariatta'
        repo = 'strange-relationship'
        issue = 64
        await gh.patch(f'/repos/{user}/{repo}/issues/{issue}',
              data={
                  'state': 'closed'
              })


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
