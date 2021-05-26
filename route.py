from flask import Flask, render_template
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

app = Flask(__name__)


@app.route("/")
@app.route("/harsh")
def check():
    PATH = r"C:\Users\Jay\chromedriver.exe"

    driver = webdriver.Chrome(PATH)

    driver.get("https://www.instagram.com/jay.malave/")

    live = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span')

    data = live.text

    driver.close()

    return render_template(live.html, data=data)

if __name__ == "__main__":
    app.run()
