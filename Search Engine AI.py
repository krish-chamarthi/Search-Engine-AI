from exa_py import Exa

exa = Exa('9ab1d440-05cc-42af-8a5e-60090e28c0cc')

query = input('Search here: ')

response = exa.search(
  query,
  num_results=5,
  type='keyword',
  include_domains=['https://www.tiktok.com'],
)

for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print()