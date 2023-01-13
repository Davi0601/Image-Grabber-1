from imports import *


driver.get("https://www.youtube.com")
time.sleep(10)

link = "https://www.youtube.com"

try:
    driver.get(link)
    time.sleep(3)
    image = driver.find_element(By.CLASS_NAME, "style-scope.yt-img-shadow")
    imageURL = image.get_attribute("src")
    print(link)
    time.sleep(3)
    # # write_to_file("\n")
    img_data = requests.get(imageURL).content
    with open(f'name.jpg', 'wb') as handler:
        handler.write(img_data)
except:
    # write_to_file("None\n")
    pass


driver.close()
driver.quit()
