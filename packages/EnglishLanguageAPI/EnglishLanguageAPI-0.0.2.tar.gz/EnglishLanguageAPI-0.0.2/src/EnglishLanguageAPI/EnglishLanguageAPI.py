#!/usr/bin/env python
# coding: utf-8

# # English Vocabulary Database Buildup
# The trick to reading the dictionary is locating your word within an easily indexed store of words and scanning 
# their associated definition into your pool of resources; much like it's python counterpart, the structure is a 
# {key:value} store.
# 
# To interpet the dictionary website as a {k:v} dictionary object the English Language API has been written to scrape 
# any given words entry from raw html through it's meta tags.
# 

# ## Module Imports
# 
#   - [Python Logging](#constants-definition): Logging is always useful; and steps should be taken to include it wherever you can.
# 
#   - [Python Requests](#build-query-url): The class object makes a request to a URL similar to ```https://dictionary.com/browse/{_search_tag}```.
# 
#   - [Beautiful Soup](#retrieve-description-from-data): BS4 is used to extract key points from the request data. 

# In[ ]:


import requests
import logging
from bs4 import BeautifulSoup


# ## Constants Definition
# 
#   - Logging : The logfile is set to output to a file, ```./analysis.log```, unless otherwise stated.
# 
#   - Dictionary: An English Language dictionary with a built-in [URL querying system](#build-query-url).

# In[ ]:


logfile = "./analysis.log"
logging.basicConfig(filename=logfile, encoding="utf-8", level=logging.DEBUG)

# English language dictionary with an easily navigable URL schema.
englishDictionary = "https://dictionary.com"

# English language synonyms database, with URL similar to the dictionaries.
englishThesaurus = "https://thesaurus.com"


# ## English Language API
# The average use-case consists of establishing the EnglishLanguageAPI with a given word and calling the
# .Description method on it, so if one were to look up "cherries", the definition would be listed thusly:
# ```
# cherries = EnglishLanguageAPI("cherries")
# cherriesDescription = cherries.Description()
# ```

# ### Initialize Class Variables
# Self-Contained variables are established for the extendable building of modular URLs to search through the
# dictionary in a variety of ways. So far the use of the following routes has been confirmed:  
#   - ```SearchRoute```: ```/browse```
# 
# The class accepts a positional search keyword that is recognized internally as ```SearchTag```.
# Caution is taken to prevent more than one word being given as input.
# For example ```"blue cherries"``` will tell the API to search for ```"blue"```, and not ```"cherries"```.
# 
# The external source being referenced is set to ```BaseURL``` for reference by local members.

# In[ ]:


class EnglishLanguageAPI:
    """
    The EnglishLanguageAPI class accepts a single word and searches the dictionary for a matching description.
    """

    def __init__(self, SearchTag, dictionary=True):
        """
        The searchTag is a callers search request given as a raw text string which is then formatted to 
        the dictionary.com built-in api standards.
        By default the search tag is compared against the thesaurus unless explicitly told to check the dictionary.
        """

        # Define the logger and log current module.
        logging.getLogger(); logging.info("\n\n  --Using English Language API.--\n")

        # Set EnglishLanguage flag to True.
        EnglishLanguage = True; logging.debug("English Language is set to True.")

        # Set URL search tags according to research findings.
        self.SearchRoute = "browse"

        # Set base URL to either dictionary or thesaurus website.
        if dictionary: self.BaseURL = englishDictionary
        else:
            logging.warning(f"Thesaurus functionality is not scrape-compatible with Dictionary.")
            logging.warning("Reverting to Dictionary functionality.")
            self.BaseURL = englishDictionary# TODO: Research thesaurus page structure.

        logging.debug(f"Using {self.BaseURL}.")

        # Single word search. TODO: Handle multiple words.
        self.SearchTag = SearchTag.split()[0].lower()
        logging.info(
            f"Searching {self.BaseURL.split('/')[-1].split('.')[0]} for word: {self.SearchTag}."
        )

    # ### Build Query URL
    # The modular URL system allows for direct querying of a page, given a known word.  The ```/browse``` sub-path
    # accepts a _single_, **singlular** word to [index the dictionary](#request-html-data-from-source) for a proper
    # [description](#retrieve-description-from-data).

    # In[ ]:


    def SearchRequestURL(self) -> str:
        """
        Prepare a URL that leads directly to the search terms.
        For the dictionary.com domain, we simply use forward slashes.
          -- All lower-case, of course.
        """
        return str(
            f"{self.BaseURL.lower()}/"
            f"{self.SearchRoute.lower()}/"
            f"{self.SearchTag.lower()}"
        )


    # ### Request HTML Data From Source
    # After recieving a [proper URL](#build-query-url) to request a page from, the system makes the request and passes the resulting content
    # to a [```BeautifulSoup```](#retrieve-description-from-data) object to be scraped for content.

    # In[ ]:


    def RawPageResults(self) -> BeautifulSoup:
        """
        Packages the search query into a BS4.BeautifulSoup object to
        be scraped by EnglishLanguageAPI.pageDescription().
        """
        return BeautifulSoup(
            requests.get(self.SearchRequestURL())\
                    .content,
            "html.parser"
        )


    # ### Retrieve Description From Data
    # The page being requested by [```EnglishLanguageAPI.RawPageResults```](#request-html-data-from-source) is now scraped for a description of the original
    # input by finding a meta-tag within the page source named 'description'.
    # 
    # The description is then stripped of any unneccessarily repetitive strings, such as itself and leftover text options
    # from the original page.
    # 
    # With the description string properly sanitized, it is [given back to the caller](#return-findings-to-caller).

    # In[ ]:


    def ScrapeResults(self) -> str:
        """
        Search the BS4 object for the search tags description in the metatags header.
        The resulting text is stripped of repetitive patterns and given back as a string.
  
        The html meta tag named 'description' usually contains a pretty solid meaning
        for the word we're trying to describe, so we'll use it with our noun.

        The description also typically carries a few repetitive strings, such as the
        noun itself followd by the _word_ description as well as an option to 'See more.'
        from the original interactive page.  These will be stripped from the string
        before being returned.
        """

        _page = self.RawPageResults()

        _description = \
            _page.find("meta", {"name": "description"})\
                 .get("content")

        _description = _description.replace(f"{self.SearchTag.title()} definition, ", "")
        _description = _description.replace(" See more.", "")
        _description = _description.capitalize()

        logging.info(f"Found description for {self.SearchTag}:\n{_description}\n\n")
        return _description


    # ### Return Findings to Caller
    # All of this is delivered to the end user through the use of the ```Description``` method attached to the
    # [```EnglishLanguageAPI```](#english-language-api) object initialized with the given input word.

    # In[ ]:
 

    def Description(self) -> ScrapeResults:
        """
         The final wrapper for conducting a search within the english dictionary or thesaurus.
        """
        return self.ScrapeResults()

    def Title(self):
        return self.SearchTag.capitalize()
