from typing import List
from requests_html import AsyncHTMLSession

asession = AsyncHTMLSession()

async def retrieve1() -> List[str]:
	response = await asession.get('https://www.bbc.co.uk/') # type: ignore
	
	await response.html.arender()

	titles = response.html.find('.ssrcss-6arcww-PromoHeadline > span')

	return [title.text for title in titles]

async def retrieve2() -> List[str]:
	response = await asession.get('https://www.diy.com/search?term=hammer') # type: ignore
	
	await response.html.arender()

	names = response.html.find('[data-test-id=productTitle]')

	return [name.text for name in names]

print(asession.run(retrieve1, retrieve2))


