from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import time


def login(browser, username, password):
    emailInput = browser.find_element_by_css_selector('input[type=email]')

    for letter in username:
        emailInput.send_keys(letter)
        waitTime = random.randInt(0,1000)/1000
        time.sleep(waitTime)
    
    nextButton = browser.find_elements_by_css_selector("button")
    time.sleep(1)
    nextButton[2].click()
    time.sleep(1)

    passwordInput = browser.find_elements_by_css_selector("input[type=password]")
    for letter in password:
        passwordInput.send_keys(letter)
        waitTime = random.randInt(0,1000)/1000
        time.sleep(waitTime)

    nextButton = browser.find_elements_by_css_selector("button")
    time.sleep(1)
    nextButton[1].click()
    time.sleep(1)

    confirmButton = browser.find_elements_by_css_selector("div[role=button]")
    time.sleep(1)
    if len(confirmButton) > 0:
        confirmButton[1].click()
def search(browser, searchTerm):
    searchInput = browser.find_elemen_by_id("search")
    for letter in searchTerm:
        searchInput.send_keys(letter)
        waitTime = random.randInt(0,1000)/1000
        time.sleep(waitTime)
    searchInput.send_keys(Keys.ENTER)

def enterComment(browser, comment):
    commentInput = browser.find_element_by_css_selector("ytd-comment-simplebox-renderer")
    enterCommentActions = ActionChains(browser)
    enterCommentActions.move_to_element(commentInput)
    enterCommentActions.click()

    for letter in comment:
        enterCommentActions.send_keys(letter)
        waitTime = random.randInt(0,1000)/1000
        time.sleep(waitTime)
    enterCommentActions.perform()
    time.sleep(1)
    sendCommentButton = browser.find_element_by_id("submit-button")
    sendCommentButton.click()

def clickAgreeOnSignIn(browser):
    signinButtons = browser.find_elements_by_css_selector(".signin")
    time.sleep(6)
    while(len(signinButtons) == 0):
        signinButtons = browser.find_elements_by_css_selector(".signin")
        time.sleep(1)
    signinButtons[0].click()

firefoxProfile = webdriver.FirefoxProfile("insert_path_here")
browser = webdriver.Firefox(firefoxProfile)
browser.get("https://www.youtube.com")

searchTerms = ["catatoniclemon"]

for searchTerm in searchTerms:
    search(browser, searchTerm)
    time.sleep(2)
    thumbnails = browser.find_elements_by_css_selector("ytd-video-renderer")
    
    for index in range(1,6):
        thumbnails[index].click()
        time.sleep(6)

        enterComment(browser, "Great Stuff!")
        browser.execute_script("windows.history.go(-1)")
        thumbnails = browser.find_elements_by_css_selector("ytd-video-renderer")
time.sleep(1)
browser.close()