from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith has heard about a cool new online to-do app
        #She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        #She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        #invited to enter a to-do item right away

        # she types "Buy peacock feathers" int a text box (tying fly-fishing lures hobby)

        #When she hits enter, page updates, page lists
        #"1: Buy peacock featehrs" as a item

        #There is still a text box inviting her to add anotehr item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)

        #The page updates, shows both items on list

        #Edither wonders whether the site will remember her list. Then she sees that a
        #site has generated a unique URL for her -- there is some
        #explanatory text to that effect.

        #She visits that URL - her to-do list is still there.

        #Satisfied, she goes back to sleep
        

if __name__== '__main__':
    unittest.main(warnings='ignore')




 

