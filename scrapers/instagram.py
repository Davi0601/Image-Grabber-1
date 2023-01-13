from imports import *


# def write_to_file(link):
#     with open('insta_mails.txt', 'a', encoding = "utf-8") as f:
#         f.writelines(link)
        

driver.get("https://www.instagram.com")
time.sleep(10)

link = "https://www.instagram.com/_missbo/"

try:
    driver.get(link)
    # # start = driver.find_element(By.CLASS_NAME, "tiktok-1g04lal-DivShareLayoutHeader-StyledDivShareLayoutHeaderV2.elmjn4l2")
    start = driver.find_element(By.CLASS_NAME, "x6umtig.x1b1mbwd.xaqea5y.xav7gou.xk390pu.x5yr21d.xpdipgo.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x11njtxf.xh8yej3")
    imageURL = start.get_attribute("src")
    print(link)
    # write_to_file("\n")
    img_data = requests.get(imageURL).contsent
    with open(f'name.jpg', 'wb') as handler:
        handler.write(img_data)
except:
    time.sleep(10)
    # write_to_file("None\n")
    pass

driver.close()
driver.quit()
