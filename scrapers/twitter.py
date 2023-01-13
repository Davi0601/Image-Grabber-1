from imports import *


driver.get("https://www.twitter.com")
time.sleep(10)

link = "https://www.twitter.com"

try:
    driver.get(f"{link}/photo")
    time.sleep(3)
    print(link)
    img = driver.find_element(By.TAG_NAME, "img")
    imgURL = img.get_attribute("src")
    # # write_to_file("\n")
    img_data = requests.get(imgURL).content
    with open(f'name.jpg', 'wb') as handler:
        handler.write(img_data)
except:
    # write_to_file("None\n")
    pass

driver.close()
driver.quit()
