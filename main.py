from playwright.sync_api import sync_playwright
import yagmail
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)

def take_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://duckduckgo.com/", timeout=60000)
        logging.info("Navigated to DuckDuckGo homepage")
        screenshot_path = "screenshot.png"
        page.screenshot(path=screenshot_path)
        logging.info("Screenshot taken and saved to %s", screenshot_path)
        browser.close()
    return screenshot_path

def send_email(screenshot_path):
    # Replace with your actual credentials
    yag = yagmail.SMTP(user="nikkyneha210@gmail.com", password="putxrqlagicxbdxb")
    yag.send(
        to="rajeshreddychinta@gmail.com",
        subject="DuckDuckGo Screenshot",
        contents="Here is the screenshot of the website.",
        attachments=screenshot_path,
    )
    logging.info("Email sent with screenshot attached")

if __name__ == "__main__":
    path = take_screenshot()
    send_email(path)
