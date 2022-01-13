import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"


def test_find_button(browser):
    browser.get(link)
    button = browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert button.text == "Add to basket"