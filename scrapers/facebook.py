from imports import *


driver.get("https://www.facebook.com/")
time.sleep(10)

# def write_to_file(link):
    # with open('insta_mails.txt', 'a', encoding = "utf-8") as f:
        # f.writelines(link)

link = "https://www.facebook.com/"

try:
    driver.get(link)
    time.sleep(3)
    start = driver.find_element(By.CLASS_NAME, "x1rg5ohu.x1n2onr6.x3ajldb.x1ja2u2z")
    image = start.find_element(By.TAG_NAME, "image")
    imageURL = start.get_attribute("href")
    print(link)
    image.click()
    time.sleep(3)
    img = driver.find_element(By.CLASS_NAME, "x1bwycvy.x193iq5w.x4fas0m.x19kjcj4")
    imgURL = img.get_attribute("src")
    time.sleep(3)
    # # write_to_file("\n")
    img_data = requests.get(imgURL).content
    with open(f'name.jpg', 'wb') as handler:
        handler.write(img_data)
except:
    # write_to_file("None\n")
    pass



driver.close()
driver.quit()