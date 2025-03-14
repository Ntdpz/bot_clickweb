from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# ตั้งค่า Chrome Options
options = Options()

# ใช้ User-Agent ปลอมตัวเป็นมนุษย์
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

# ใช้โปรไฟล์ Chrome ที่ล็อกอินไว้แล้ว (แก้ path ตามเครื่องของคุณ)
options.add_argument(r"--user-data-dir=C:\Users\nnnon\AppData\Local\Google\Chrome\User Data")
options.add_argument("--profile-directory=Default")  # เปลี่ยนเป็นชื่อโปรไฟล์ที่ใช้

# ตั้งค่า WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# เปิดหน้าแรกของ Shopee
driver.get("https://shopee.co.th")

# รอให้โหลดหน้าเว็บ
time.sleep(5)

# ตรวจสอบว่ามี Popup ให้เลือกประเทศหรือไม่
try:
    thailand_button = driver.find_element(By.XPATH, '//button[contains(text(), "ไทย")]')
    thailand_button.click()
    time.sleep(3)  # รอให้หน้าโหลดใหม่
except:
    print("ไม่พบ Popup เลือกประเทศ")

# ให้ผู้ใช้ล็อกอินเองก่อนทำงานต่อ
input("กรุณาล็อกอินในเบราว์เซอร์ที่เปิดขึ้นมา แล้วกด Enter เมื่อเสร็จ...")

# ค้นหาช่องค้นหา
search_box = driver.find_element(By.NAME, "q")

# พิมพ์ชื่อสินค้าที่ต้องการค้นหา
search_box.send_keys("iPhone 14")
search_box.send_keys(Keys.RETURN)

# รอผลลัพธ์โหลด
time.sleep(5)

# ปิดเบราว์เซอร์
driver.quit()
