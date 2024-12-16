"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DuckDuckGoResultPage:
  
  # Locators

  RESULT_LINKS = (By.CSS_SELECTOR, 'ol.react-results--main li a')
   # This CSS selector targets <a> (link) elements that 
   # are children of <li> elements, which are nested inside an <ol> with the class react-results--main.
    # RESULT_LINKS = (By.XPATH, '//ol[@class="react-results--main"]//li//a')
  SEARCH_INPUT = (By.ID, 'search_form_input')

  #New locator for more results
  MORE_RESULTS_BUTTON= (By.ID, 'more-results')

  # Initializer: initialize the browser object

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods

  #New Method to include click more results
  def click_more_results(self):
    button = self.browser.find_element(*self.MORE_RESULTS_BUTTON)
    button.click()
    # Wait for new results to load
    WebDriverWait(self.browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ol.react-results--main li a'))
    )

  def result_link_titles(self):
    links = self.browser.find_elements(*self.RESULT_LINKS)
    titles = [link.text for link in links]
    return titles
  
  def search_input_value(self):
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    value = search_input.get_dom_attribute('value')
    return value

  def title(self):
    return self.browser.title