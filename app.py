import time
from keys import keys as k 
from selenium import webdriver
import requests

global latency

class Match: #self = java .this
  def __init__(self, team1,team2,choice):
    self.t1 = team1
    self.t2 = team2
    self.choice = choice

  def stampa(self):
    print(self.t1 + " vs " + self.t2 + " \n" + "Your Choice:" + self.choice + "\n")


def login(driver):
    driver.get('https://betonbit.com/login')
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/form[1]/div[1]/input').send_keys(k['email'])
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/form[1]/div[2]/input').send_keys(k['password'])
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/form[1]/div[3]/button').click()
    time.sleep(time)
    if (driver.current_url == 'https://betonbit.com/login'):
        print('Login Failed ,wrong credentials')
        return 0
    driver.get('https://betonbit.com/betting')
    return 1

def vp_fetch_games(driver):
    driver.get('https://www.vpgame.com/prediction')
    n=10
    g_list=[]
    for i in range(1,5):
        driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div[1]/div/a[2]').click()
        time.sleep(latency)
        div = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/div[{}]'.format(i))
        m_link = div.find_element_by_css_selector('a').get_attribute('href')
        g_list.append(study(m_link))
        time.sleep(latency)
        driver.back()
    return g_list

def study(match_link):
    driver.get(match_link)
    time.sleep(3)

    team1 = str(driver.find_element_by_xpath('//*[@id="match-main-info"]/div[3]/div[1]/div[1]/div[1]').text)
    odd1 = float(driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div[2]/div[3]/div[1]/div[1]/div[2]/span').text)
    perc1 = float(driver.find_element_by_xpath('//*[@id="match-main-info"]/div[3]/div[2]').text.split('%')[0])

    team2 = str(driver.find_element_by_xpath(' //*[@id="match-main-info"]/div[5]/div[1]/div[2]/div[1]').text)
    odd2 = float(driver.find_element_by_xpath('//*[@id="match-main-info"]/div[5]/div[1]/div[2]/div[2]/span').text)
    perc2 = float(driver.find_element_by_xpath('//*[@id="match-main-info"]/div[5]/div[2]').text.split('%')[0])

    #Calculate a result with last data
    

    match=Match(team1,team2,team1)
    return match






    


    

if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')
    latency=5
    #if login(driver,latency):
        #time.sleep(10)
    games = vp_fetch_games(driver) #Fetches and studies the next n games
    for x in games:
        x.stampa()
