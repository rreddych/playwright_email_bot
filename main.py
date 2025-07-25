from playwright.sync_api import sync_playwright
import yagmail
import logging

def take_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://duckduckgo.com/", timeout=60000)
        logging
        screenshot_path = "screenshot.png"
        page.screenshot(path=screenshot_path)
        logging
        browser.close()
    return screenshot_path

def send_email(screenshot_path):
    # Replace with your actual credentials
    yag = yagmail.SMTP(user="nikkyneha210@gmail.com", password="masked_enter_actual_password_here")
    yag.send(
        to="rajeshreddychinta@gmail.com",
        subject="DuckDuckGo Screenshot",
        contents="Here is the screenshot of the website.",
        attachments=screenshot_path,
    )
    logging

if __name__ == "__main__":
    path = take_screenshot()
    send_email(path)
