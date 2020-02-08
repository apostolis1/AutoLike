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

class InstaBot:
    
    def getLikeButtonByArticleElement(self, articleElement):
        return articleElement.find_element_by_xpath(".//span[contains(@class, 'fr66n')]//button")
    
    def getUsernameByArticleElement(self, articleElement):
        usernameElement = articleElement.find_element_by_xpath(".//*[contains(@class, 'FPmhX')]")
        return usernameElement.get_attribute("title")
    
    def toLike(self, userName, usersToLike):
        if userName in usersToLike:
            return True
        return False

    def addUser(self, user):
        self.usersToLike.append(user)    

    def getLikeCondition(self, likebutton):
        return likebutton.find_element_by_xpath(".//*[name()='svg']").get_attribute("aria-label")

    def signIn(self):
        self.driver .get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        width, height = pyautogui.size()
        self.driver.set_window_size(width, height)#Fullsize window
        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
        sleep(1)
        sleep(2)
        sleep(2)
        #logged in and on the main page

    def like(self):
        SCROLL_PAUSE_TIME = 0.5
        likedPosts = 0
        article_path = []
        uniqueElementsFound = []
        while len(uniqueElementsFound) < self.NO_POSTS_TO_LIKE:
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            article_path = self.driver.find_elements_by_xpath("//*[contains(@class, 'L_LMM SgTZ1')]")
            for article in article_path:
                if article not in uniqueElementsFound and len(uniqueElementsFound) < self.NO_POSTS_TO_LIKE: #The article is not already checked and the limit hasnt been exceeded
                    uniqueElementsFound.append(article)
                    usernameElement = article.find_element_by_xpath(".//*[contains(@class, 'FPmhX')]")
                    likeBtn = self.getLikeButtonByArticleElement(article)
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", likeBtn)
                    self.driver.execute_script("window.scrollBy(0,-200);")
                    username = usernameElement.get_attribute("title")
                    if not self.CheckTheList or self.toLike(username, self.usersToLike):
                        if self.getLikeCondition(likeBtn) == "Like":
                            likeBtn.click()
                            likedPosts += 1
                            print("Liked one photo from", username)
        print("Proccess terminated succesfully. Liked" , likedPosts, "posts")
    
    def __init__(self, us, pw, posts, extUsers, tocheck):#takes the username and password of the user as parameters
        self.NO_POSTS_TO_LIKE = posts #the number of top posts of the feed that we will look through
        self.CheckTheList = tocheck #determines if we look at specific usernames or all the posts
        self.password = pw
        self.username = us
        self.driver = webdriver.Chrome()
        self.usersToLike = []
        for user in extUsers:
            self.addUser(user)
        for i in ["euroleague", "nba", "bleacherreport", "overtime"]:
            self.addUser(i)
            
if __name__ == "__main__":    
    mybot = InstaBot("", "", 1, [], True)
    mybot.signIn()
    mybot.like()
    print("test")