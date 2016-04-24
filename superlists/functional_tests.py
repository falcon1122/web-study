#_*_ coding:utf8 _*_
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVistorTest(unittest.TestCase):
  
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
#发现网站,打开首页
        self.browser.get('http://localhost:8000')
#用户发现每个title都有To-Do
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)
#应用邀请用户输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')
#input “buy some food”
        inputbox.send_keys('buy some food')
#输入回车更新
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1:buy some food',[row.text for row in rows])
#显示一个文本框，输入其他待办事项
        
        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main()

