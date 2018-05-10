import aiohttp
import asyncio
import os
from gidgethub.aiohttp import GitHubAPI


async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, os.getenv('GH_ACCOUNT'), oauth_token=os.getenv('GH_AUTH'))
        user = 'mariatta'
        repo = 'strange-relationship'
        await gh.patch(f'/repos/{user}/{repo}/issues',
              data={
                  'title': 'Thank you!',
                  'body': 'Thank you for the GitHub bot tutorial!'
              })


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
