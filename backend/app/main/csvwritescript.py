import csv
import bnqretrieval, homebaseretrieval, screwfixretrieval, jewsonretrieval, wickesretrieval, woodiesretrieval, toolstationretrieval, victoriaplumretrieval
from requests_html import AsyncHTMLSession


asession = AsyncHTMLSession()

# links = asession.run(
#     lambda: bnqretrieval.retrieve(asession, term),
#     lambda: bnqretrieval.retrieve(asession, term),
# )

term = input('Enter term: ')


results = asession.run(
    lambda: bnqretrieval.retrieve(term, asession),
    lambda: homebaseretrieval.retrieve(term, asession),
    lambda: jewsonretrieval.retrieve(term, asession),
    lambda: wickesretrieval.retrieve(term, asession),
    lambda: woodiesretrieval.retrieve(term, asession),
    lambda: screwfixretrieval.retrieve(term, asession),
    lambda: toolstationretrieval.retrieve(term, asession),
    lambda: victoriaplumretrieval.retrieve(term, asession),
)


# links = [link for linkresults in links for link in linkresults]

# print(links)

# # async def test(link):
# #     print('banana', link)
# #     return 'a', link

# def test2(link):
#     # print('define', link)
#     return lambda: bnqretrieval.retrieve_page(asession, link)

# results = asession.run(*[
#     # (lambda: bnqretrieval.retrieve_page(asession, link))
#     # (lambda: test(link))
#     test2(link)
#     for link in links
# ])

# results = asession.run(
#     lambda: bnqretrieval.retrieve_page(asession, links[0]),
#     lambda: bnqretrieval.retrieve_page(asession, links[1]),
#     lambda: bnqretrieval.retrieve_page(asession, links[2]),
#     lambda: bnqretrieval.retrieve_page(asession, links[3]),
# )


# links = ['1', '2', '3']

# results = [f() for f in [(lambda: ('b', test(link))) for link in links]]

print(results)
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for set in results:
        writer.writerows(set)   

