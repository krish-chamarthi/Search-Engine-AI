from exa_py import Exa

exa = Exa('Your Exa Key Here')

query = input('Search here: ')

response = exa.search(
  query,
  num_results=5,
  type='keyword',
  include_domains=['https://www.tiktok.com'],
)

urls_seen = set()
duplicates = []

for result in response.results:
  if result.url in urls_seen:
    duplicates.append(result.url)
  else:
    urls_seen.add(result.url)
    print(f'Title: {result.title}')
    print(f'URL: {result.url}')
    print()

if duplicates:
  print("Duplicate URLs found:")
  for url in duplicates:
    print(url)
else:
  print("No duplicate URLs found.")
