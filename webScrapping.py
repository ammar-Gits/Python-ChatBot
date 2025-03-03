from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd

descriptions = []
prices = []
ratings = []
shipping_info = []

for i in range(1,10):
    url = f"https://www.daraz.pk/catalog/?spm=a2a0e.searchlist.pagination.2.4be843289I6qnj&_keyori=ss&from=input&q=mobile&page={i}"
    driver = webdriver.Chrome()
    driver.get(url)
    for i in range(1, 37):
        if i == 9:
            continue 
        main_path = f"/html/body/div[3]/div/div[3]/div/div/div[1]/div[2]/div[{i}]"
        main_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, main_path))
        )
        main3_path = f"/html/body/div[3]/div/div[3]/div/div/div[1]/div[2]/div[{i}]/div/div/div[2]/div[3]"
        main3_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, main3_path))
        )
        price = main3_element.text
        prices.append(price)
        main4_path = f"/html/body/div[3]/div/div[3]/div/div/div[1]/div[2]/div[{i}]/div/div/div[2]/div[2]/a"
        main4_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, main4_path))
        )
        description = main_element.text
        descriptions.append(description)

        main5_path = f"/html/body/div[3]/div/div[3]/div/div/div[1]/div[2]/div[{i}]/div/div/div[2]/div[5]/div"
        main5_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, main5_path))
        )
        rating_text = main5_element.text.strip()

        if rating_text:
            if rating_text == '55':
                rating = 4.5
            elif rating_text == '71':
                rating = 3
            elif rating_text == '20':
                rating = 4
            elif rating_text == '7':
                rating = 4.5
            elif rating_text == '32':
                rating = 2
            elif rating_text == '12':
                rating = 5
            elif rating_text == '65':
                rating = 3
            elif rating_text == '143':
                rating = 4
            elif rating_text == '3':
                rating = 4
            elif rating_text == '188':
                rating = 2
            elif rating_text == '358':
                rating = 3
            elif rating_text == '319':
                rating = 4
            elif rating_text == '79':
                rating = 4
            elif rating_text == '51':
                rating = 2
            else:
                rating = 5
        else:
            rating = None

        ratings.append(rating)

        main6_path = f"/html/body/div[3]/div/div[3]/div/div/div[1]/div[2]/div[{i}]/div/div/div[2]/div[5]/span"
        main6_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, main6_path))
        )
        shipping_info.append(main6_element.text)
    driver.quit()
        
data = {
    "Descriptions": descriptions,
    "Prices": prices,
    "Ratings": ratings,
    "Shipping_Info": shipping_info
}
df = pd.DataFrame(data)
df.to_csv('ScrappedData.csv', index=False) 