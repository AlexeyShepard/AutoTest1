import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_click_wordfile():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/")

    driver.find_element(By.XPATH, "//div[@class='card mt-4 top-card']").click()
    driver.find_element(By.ID, "item-1").click()
    driver.find_element(By.XPATH, "//button[@class='rct-collapse rct-collapse-btn']").click()
    driver.find_element(By.XPATH,"//label[contains(., 'Downloads')]/preceding-sibling::button").click()
    driver.find_element(By.XPATH,"//span[contains(., 'Excel File.doc')]").click()

    word = driver.find_element(By.XPATH,'//label[@for="tree-node-wordFile"]').text

    selected_text = driver.find_element(By.XPATH, "//span[text()='You have selected :']").text

    result = selected_text + " " + word

    assert result == "You have selected : Word File.doc"
