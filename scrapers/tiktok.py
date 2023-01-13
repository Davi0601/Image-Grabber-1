from imports import *


driver.get("https://www.tiktok.com")
time.sleep(10)

link = "https://www.tiktok.com"

try:
    driver.get(link)
    start = driver.find_element(By.CLASS_NAME, "tiktok-1zpj2q-ImgAvatar.e1e9er4e1")
    imgUrl = start.get_attribute("src")
    print(link)
    img_data = requests.get(imgUrl).content
    with open(f'name.jpg', 'wb') as handler:
        handler.write(img_data)
except:
    pass

driver.close()
driver.quit()
