


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from time import sleep


# def waiting_func(by_variable, attribute):
#     try:
#         WebDriverWait(self.driver, 10).until(lambda x: x.find_element(by=by_variable,  value=attribute))
#     except (NoSuchElementException, TimeoutException):
#         print('{} {} not found'.format(by_variable, attribute))
#         exit()
#TODO Implement wait instead of sleep()
#TODO Devide into methods for more readeable codee


class InstaBot:
    def __init__(self, us, pw):#takes the username and password of the user as parameters
        NO_POSTS_TO_LIKE = 20 #the number of top posts of the feed that we will look through
        CheckTheList = False #determines if we look at specific usernames or all the posts
        self.password = pw
        self.username = us
        width, height = pyautogui.size()
        self.driver = webdriver.Chrome()
        liked = 0
        postsToLike = ["euroleague", "nba", "bleacherreport", "overtime"]

        
        self.driver.get("https://www.instagram.com/")
        self.driver.set_window_size(width, height)#Fullsize window
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        sleep(1.5)
        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
        sleep(1)
        sleep(2)
        i = 0
        sleep(2)
        #logged in and on the main page
        path = []
        SCROLL_PAUSE_TIME = 1

        # Get scroll height
        article_path = []
        path = []
        uniqueElementsFound = []
        while len(uniqueElementsFound) < 20:
            # Scroll down to bottom
            
        #WORKS
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            
            article_path = self.driver.find_elements_by_xpath("//*[contains(@class, 'L_LMM SgTZ1')]")
            for article in article_path:
                if article not in uniqueElementsFound:
                    uniqueElementsFound.append(article)
                    usernameElement = article.find_element_by_xpath(".//*[contains(@class, 'FPmhX')]")
                    username = usernameElement.get_attribute("title")
                    path.append(username)

            # for article in article_path:
            #     usernameElement = article.find_element_by_xpath(".//*[contains(@class, 'FPmhX')]")
            #     username = usernameElement.get_attribute("title")
            #     path.append(username)
            lastElement = article_path[-1]
            self.driver.execute_script("arguments[0].scrollIntoView(true);", lastElement)
            
            
            #find a good way to scroll
            # body = self.driver.find_element_by_css_selector('body')
            # body.send_keys(Keys.PAGE_DOWN)

            # Calculate new scroll height and compare with last scroll height


            
        for i in path:
            print(i)
                #this for loop goes through the posts and likes posts of accounts not in the blocked list
        





#/html/body/div[1]/section/main/section/div[1]/div[1]/div/article[5]/header/div[2]/div[1]/div/h2/a
