from selenium import webdriver
from time import sleep
import random, string


class InstaBot:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get(
            "https://app.sli.do/event/6aAe6GNFBC4ccewQM1sneM/live/questions"
        )
        # self.driver.find_element_by_xpath("//textarea[contains(aria-label(), 'Input field for your question')]").click()
        sleep(5)
        textarea = self.driver.find_element("id", "question-field")
        sleep(2)
        while True:
            x = "".join(random.choice(string.printable) for _ in range(50))
            sleep(2)
            textarea.send_keys(x)
            self.driver.find_element(
                "css selector", "[aria-label='Ask the speaker'"
            ).click()
            sleep(2)
            self.driver.find_element(
                "css selector", "button[type='submit']"
            ).click()
        # print(type(textarea))


InstaBot()
