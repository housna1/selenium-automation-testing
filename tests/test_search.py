"""
These tests cover DuckDuckGo searches.
"""

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
import pytest

@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, phrase):
  search_page = DuckDuckGoSearchPage(browser)
  result_page = DuckDuckGoResultPage(browser)
  PHRASE = "panda"

  # Given the DuckDuckGo home page is displayed
  search_page.load()

  # When the user searches for "panda"
  search_page.search(PHRASE)

  # then the search result query is "panda"
  assert PHRASE == result_page.search_input_value()

  # And the search result links pertain to "panda"
  titles = result_page.result_link_titles()
  matches = [t for t in titles if PHRASE.lower() in t.lower()]
  print(f"Number of matches before clicking 'More Results': {len(matches)}")
  assert len(matches) > 0

  

  # And the search result title contains "panda"
  assert PHRASE in result_page.title()

  #expand more results
  result_page.click_more_results()
  new_titles= result_page.result_link_titles()
  new_matches = [t for t in new_titles if PHRASE.lower() in t.lower() ]
  assert len(new_matches)> len(matches)
  #Assertion: The test checks that the number of matches has increased, which implies 
  #that clicking "More Results" successfully loaded additional search results containing 
  #the search phrase.

  result_page.click_more_results()
  new_titles_2= result_page.result_link_titles()
  new_matches_2 = [t for t in new_titles if PHRASE.lower() in t.lower() ]
  assert len(new_matches_2)> len(matches)