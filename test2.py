


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



#TODO Implement wait instead of sleep()
#TODO Devide into methods for more readeable codee
#TODO check how we found click in other file and implemet that on the toLike method

class InstaBot:
    
    def getLikeButtonByArticleElement(self, articleElement):
        return articleElement.find_element_by_xpath(".//span[contains(@class, 'fr66n')]//button")
    
    def getUsernameByArticleElement(self, articleElement):
        usernameElement = articleElement.find_element_by_xpath(".//*[contains(@class, 'FPmhX')]")
        return usernameElement.get_attribute("title")
    
    def toLike(self, articleElement, usersToLike):
        if self.getUsernameByArticleElement(articleElement) in usersToLike:
            return True
        return False

    def __init__(self, us, pw):#takes the username and password of the user as parameters
        NO_POSTS_TO_LIKE = 20 #the number of top posts of the feed that we will look through
        CheckTheList = False #determines if we look at specific usernames or all the posts
        self.password = pw
        self.username = us
        width, height = pyautogui.size()
        self.driver = webdriver.Chrome()
        liked = 0
        users = ["euroleague", "nba", "bleacherreport", "overtime"]

        
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

        article_path = []
        path = []
        uniqueElementsFound = []
        while len(uniqueElementsFound) < NO_POSTS_TO_LIKE:
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            article_path = self.driver.find_elements_by_xpath("//*[contains(@class, 'L_LMM SgTZ1')]")
            for article in article_path:
                sleep(1)
                if article not in uniqueElementsFound and len(uniqueElementsFound) < NO_POSTS_TO_LIKE:
                    uniqueElementsFound.append(article)
                    usernameElement = article.find_element_by_xpath(".//*[contains(@class, 'FPmhX')]")
                    username = usernameElement.get_attribute("title")
                    if True or self.toLike(article, users):
                        likeBtn = self.getLikeButtonByArticleElement(article)
                        likeBtnCondition = likeBtn.find_element_by_xpath("./*[name()='svg']").get_attribute("aria-label")
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", likeBtn)
                        self.driver.execute_script("window.scrollBy(0,-200);")
                        if likeBtnCondition == "Like":
                            likeBtn.click()
                        print(username, likeBtnCondition)
                    path.append(username)

mybot = InstaBot("apostolis.stamatis1@gmail.com", "1532000!@#")