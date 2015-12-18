from .base import FunctionalTest


class SearchTopicTest(FunctionalTest):

    def test_can_see_search_form(self):

        # Smith goes to the website
        home_page = self.live_server_url + '/'
        self.browser.get(home_page)

        # He notices the page title mentions Topic Search
        self.assertIn('Topic Search', self.browser.title)

        # He also sees the search text box and  button
        self.assertTrue(self.check_element_exists_by_id('id_tb_search_term'))
        self.assertTrue(self.check_element_exists_by_id('id_btn_search_go'))

        # He is interested in the term 'python', so he types that in the search box and clicks 'Search' button
        self.fill_text_box_by_id('id_tb_search_term', 'python')
        btn_search = self.browser.find_element_by_id('id_btn_search_go')
        btn_search.click()

        # He is directed to search results page
        current_url = self.browser.current_url
        self.assertRegex(current_url, r'topic_search/search_result/?')

        # He sees tweets for that topic
        content = self.browser.page_source
        self.assertIn("Twitter Search Result:", content)
        self.assertIn("python", content.lower())

        # He refreshes the browser and the results for the same term are refreshed
        self.browser.get(current_url)
        content = self.browser.page_source
        self.assertIn("Twitter Search Result:", content)
        self.assertIn("python", content.lower())

