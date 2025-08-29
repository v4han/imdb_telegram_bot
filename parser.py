from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def get_driver():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver


def movies_most_popular():
    driver = get_driver()
    popmovies = []
    try:
        driver.get("https://www.imdb.com/chart/moviemeter/?ref_=chttvtp_nv_menu")
        time.sleep(2)

        for i in range(1, 11):
            try:
                popmovies.append(
                    f"{i}. " + driver.find_element(
                        By.CSS_SELECTOR,
                        f'#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center '
                        f'> section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li:nth-child({i}) a h3'
                    ).text
                )
            except:
                popmovies.append(f"{i}. [Title not found]")
        return popmovies
    finally:
        driver.quit()


def most_popular_movies_of_all_time():
    driver = get_driver()
    movies = []
    try:
        driver.get("https://www.imdb.com/chart/top/?ref_=chttp_nv_menu")
        time.sleep(2)

        for i in range(1, 11):
            try:
                movies.append(
                    f"{i}. " + driver.find_element(
                        By.CSS_SELECTOR,
                        f'#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center '
                        f'> section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li:nth-child({i}) a h3'
                    ).text
                )
            except:
                movies.append(f"{i}. [Title not found]")
        return movies
    finally:
        driver.quit()


def get_movie_description(index, url):
    driver = get_driver()
    try:
        driver.get(url)
        time.sleep(2)

        element = driver.find_element(
            By.CSS_SELECTOR,
            f'#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center '
            f'> section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li:nth-child({index+1}) a'
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)
        element.click()
        time.sleep(2)

        title = driver.find_element(By.CSS_SELECTOR, "h1").text

        try:
            description = driver.find_element(By.CSS_SELECTOR, "span.sc-bf30a0e-2.bRimta").text
        except:
            description = "No description found."

        try:
            rating = driver.find_element(By.CSS_SELECTOR, "span.sc-4dc495c1-1.lbQcRY").text
        except:
            rating = "No rating"

        try:
            runtime = driver.find_element(
                By.CSS_SELECTOR,
                "#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-358297d7-0.CHcbB "
                "> section > div:nth-child(5) > section > section > div.sc-b234497d-3.ffckSa "
                "> div.sc-13687a64-0.iOkLEK > ul > li:nth-child(3)"
            ).text
        except:
            runtime = "Can't find runtime"

        return f"🎬 {title}\n⭐ Rating: {rating}/10\n⏳ Runtime: {runtime} \n\n{description}"
    finally:
        driver.quit()


def tv_shows_most_popular():
    driver = get_driver()
    shows = []
    try:
        driver.get("https://www.imdb.com/chart/tvmeter/?ref_=chttvtp_nv_menu")
        time.sleep(2)

        for i in range(1, 11):
            try:
                shows.append(
                    f"{i}. " + driver.find_element(
                        By.CSS_SELECTOR,
                        f'#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center '
                        f'> section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li:nth-child({i}) a h3'
                    ).text
                )
            except:
                shows.append(f"{i}. [Title not found]")
        return shows
    finally:
        driver.quit()


def tv_shows_most_popular_all_time():
    driver = get_driver()
    shows = []
    try:
        driver.get("https://www.imdb.com/chart/toptv/?ref_=chtmvm_nv_menu")
        time.sleep(2)

        for i in range(1, 11):
            try:
                shows.append(
                    f"{i}. " + driver.find_element(
                        By.CSS_SELECTOR,
                        f'#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center '
                        f'> section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li:nth-child({i}) a h3'
                    ).text
                )
            except:
                shows.append(f"{i}. [Title not found]")
        return shows
    finally:
        driver.quit()


def get_tv_description(index, url):
    driver = get_driver()
    try:
        driver.get(url)
        time.sleep(2)

        element = driver.find_element(
            By.CSS_SELECTOR,
            f'#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center '
            f'> section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li:nth-child({index+1}) a'
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)
        element.click()
        time.sleep(2)

        title = driver.find_element(By.CSS_SELECTOR, "h1").text

        try:
            description = driver.find_element(By.CSS_SELECTOR, "span.sc-bf30a0e-2.bRimta").text
        except:
            description = "No description found."

        try:
            rating = driver.find_element(By.CSS_SELECTOR, "span.sc-4dc495c1-1.lbQcRY").text
        except:
            rating = "No rating"

        try:
            runtime = driver.find_element(
                By.CSS_SELECTOR,
                "#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-358297d7-0.CHcbB "
                "> section > div:nth-child(5) > section > section > div.sc-b234497d-3.ffckSa "
                "> div.sc-13687a64-0.iOkLEK > ul > li:nth-child(4)"
            ).text
        except:
            runtime = "Can't find runtime"

        return f"🎬 {title}\n⭐ Rating: {rating}/10\n⏳ Episode runtime: {runtime} \n\n{description}"
    finally:
        driver.quit()
