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

