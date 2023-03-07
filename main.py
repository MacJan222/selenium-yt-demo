import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class YtMainPage:
    """
    Representation of first page visited during test. Contains tuples made of type name and XPATH/CSS/NAME/ID used to access important page contents.
    """
    
    def __init__(self):
        self.by_cookie_reject = (By.XPATH, '/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[1]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')
        self.by_search_bar = (By.NAME, 'search_query')
        self.by_search_icon = (By.ID, 'search-icon-legacy')
        self.by_first_video = (By.CSS_SELECTOR, '#video-title > yt-formatted-string')


class YtVideoPage:
    """
    Representation of a video page accesed during the test. Contains tuples made of type name and XPATH/CSS values used to access important page contents.
    """

    def __init__(self) -> None:
        self.by_skip_button = (By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[17]/div/div[3]/div/div[2]/span/button/span')
        self.by_video_slider = (By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[31]/div[1]/div[2]/div[3]')
        self.by_play_button = (By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[31]/div[2]/div[1]/button')
        self.by_video_window = (By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[1]/video')
        self.by_video_title = (By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[1]/h1/yt-formatted-string')
        self.by_video_duration = (By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[31]/div[2]/div[1]/div[1]/span[2]/span[3]')
        self.by_channel_name = (By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-video-owner-renderer/div[1]/ytd-channel-name/div/div/yt-formatted-string/a')
        self.by_views_count = (By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[3]/div[1]/div/div/yt-formatted-string/span[1]')
        self.by_upload_date = (By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[3]/div[1]/div/div/yt-formatted-string/span[3]')
        # self.by_likes_count = (By.XPATH, '')
        # self.by_dislikes_count = (By.XPATH, '')
        self.by_second_video = (By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[3]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-compact-video-renderer[1]/div[1]/div/div[1]/a/h3/span')
        self.by_foo = (By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]")
        self.by_current_time = (By.CSS_SELECTOR, '#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > div.ytp-time-display.notranslate > span:nth-child(2) > span.ytp-time-current')


def ad_skip(driver, ad_delay: int):
    """This function is used to skip an advertisement in a youtube video. It was not a required feature, however it significantly speeds up the process of testing.

    :param driver: driver instance used in a test.
    :param ad_delay: explicit wait time for ad to be skippable. 
    :type ad_delay: int

    """
    try:
        skip_button = WebDriverWait(driver, ad_delay).until(EC.element_to_be_clickable(yt_first_video_page.by_skip_button))
        skip_button.click()
        print("An ad was skipped!")
    except TimeoutException:
        print("No ad was skipped")

def find_from_by(by):
    """Helper function responsible for unpacking 'by' type tuple used to store values needed to reach important data during testing.

    :param by: an incoming tuple with data to be unpacked and used by find_element function
    :return: located element from unpacked tuple data.
    """
    return driver.find_element(by[0], by[1])

def check_if_video_is_played():
    """Function that makes sure the video is being played. If a video is paused, both timestamps will be the same.
    Not necessary in my work, introduced in case default browser on other devices works differently.

    :return: logical value of comparison between two timestamps. 
    :rtype: boolean
    """
    timestamp1 = find_from_by(yt_second_video_page.by_current_time.text)
    time.sleep(2)
    timestamp2 = find_from_by(yt_second_video_page.by_current_time.text)
    print(timestamp1, timestamp2)
    return timestamp1 != timestamp2

if __name__ == "__main__":
    # prepare time variables
    normal_delay = 8
    ad_delay = 12

    # prepare page instances
    yt_main_page = YtMainPage()
    yt_first_video_page = YtVideoPage()
    yt_second_video_page = YtVideoPage()

    # chromium driver is added to path
    driver = webdriver.Chrome()
    driver.maximize_window()

    #navigate to YouTube main page
    driver.get('http://youtube.com')

    # handle cookie message
    try:
        cookie_reject = WebDriverWait(driver, normal_delay).until(EC.presence_of_element_located(yt_main_page.by_cookie_reject))
        cookie_reject.click()
        print("Cookies rejected successfully!")
    except TimeoutException:
        print("Cookies rejection failed")

    # search "Python"
    search_bar = WebDriverWait(driver, normal_delay).until(EC.element_to_be_clickable(yt_main_page.by_search_bar))
    search_icon = WebDriverWait(driver, normal_delay).until(EC.element_to_be_clickable(yt_main_page.by_search_icon))
    driver.implicitly_wait(2)
    search_bar.click()
    search_bar.send_keys("Python")
    search_icon.click()

    # go to 1st video
    first_video = WebDriverWait(driver, normal_delay).until(EC.element_to_be_clickable(yt_main_page.by_first_video))
    first_video.click()

    ad_skip(driver, ad_delay)

    # drag video slider and mute video
    video_slider = find_from_by(yt_first_video_page.by_video_slider)
    video_window = find_from_by(yt_first_video_page.by_video_window)
    ActionChains(driver).send_keys('m').move_to_element(video_slider).click().perform()

    ad_skip(driver, ad_delay)

    # run video if paused
    if check_if_video_is_played:
        pass
    else:
        video_window.click()

    # wait for site to load
    driver.implicitly_wait(6)

    # get requested information and print it
    video_duration = find_from_by(yt_first_video_page.by_video_duration).text
    video_title = find_from_by(yt_first_video_page.by_video_title).text
    channel_name = find_from_by(yt_first_video_page.by_channel_name).text
    views_count = find_from_by(yt_first_video_page.by_views_count).text
    upload_date = find_from_by(yt_first_video_page.by_upload_date).text
    print("Video title:", video_title)
    print("Video duration:", video_duration)
    print("Channel name:", channel_name)
    print("Views count:", views_count)
    print("Upload date:", upload_date)
    print("Likes and dislikes count: scraping disabled by site owner")

    # find and go to next video
    second_video = find_from_by(yt_first_video_page.by_second_video)
    second_video.click()

    ad_skip(driver, ad_delay)

    # wait for site to load
    driver.implicitly_wait(6)

    # move mouse over player to show current time and check it periodically 
    loop_counter = 0
    while loop_counter < 12:
        ActionChains(driver).move_to_element(video_window).move_to_element(video_slider).perform()
        tmp = find_from_by(yt_second_video_page.by_current_time).text
        if tmp == '0:10':
            break
        time.sleep(0.8)
        loop_counter += 1

    # pause the video
    video_window.click()

    # see the result
    time.sleep(4)
