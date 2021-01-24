from selenium import webdriver
import os
import time

class InstagramBot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.driver=webdriver.Chrome(r'####Path/to/chromedriver####')
        self.login(username,password)

    def login(self,username,password):
        self.driver.get('https://www.instagram.com/accounts/login/#')
        time.sleep(2)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath("//div[contains(text(), 'Log In')]").click()
        self.likePosts()

    def likePosts(self):
        self.baseURL='https://www.instagram.com/explore/tags/'
        self.tags=['**List of Tags to like**']
        for tag in self.tags:
            tagURL='https://www.instagram.com/explore/tags/{}'.format(str(tag))
            time.sleep(5)
            self.driver.get(tagURL)
            self.posts=self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]')
            self.posts[0].click()
            for i in range (500):
                try:
                    time.sleep(2)
                    self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button").click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click()
                except:
                    print("error in liking post {}".format(i+1))
                    self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click()
if __name__ == '__main__': 
    igBot=InstagramBot('###username###','###Password###')
