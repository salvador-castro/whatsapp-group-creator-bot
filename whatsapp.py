from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# ChromeDriver Configuration
service = Service("/usr/local/bin/chromedriver")
options = webdriver.ChromeOptions()
options.binary_location = "/Users/salvacastro/Downloads/chrome-mac-arm64/GoogleChromeForTesting.app/Contents/MacOS/Google Chrome for Testing"
options.add_argument("--user-data-dir=/Users/salvacastro/Library/Application Support/Google/Chrome")
options.add_argument("--profile-directory=Default")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--remote-debugging-port=9222")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://web.whatsapp.com")

input("\n📷 Escaneá el código QR y presioná ENTER cuando esté listo...\n")

# Wait for the chat interface to load
try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@aria-label, 'Chat')]"))
    )
except:
    print("❌ No se detectó la interfaz de WhatsApp. Revisá si se cargó bien o si el QR se escaneó.")
    driver.quit()
    exit()

# Read CSV and create groups
with open("grupos_a_crear.csv", newline='') as archivo_csv:
    lector = csv.reader(archivo_csv)
    next(lector)  # encabezado

    for fila in lector:
        group_name = fila[0].strip()
        if not group_name:
            continue

        print(f"🔧 Creando grupo: {group_name}")

        try:
            # Floating "new chat" button
            chat_name = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='new-chat-outline']"))
            )
            chat_name.click()

            # "New group" button
            group_name = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'New group')]"))
            )
            group_name.click()

            # Search for contact
            input_search = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search name or number']"))
            )
            input_search.send_keys("Mio Uruguay")

            contact = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@title='Mio Uruguay']"))
            )
            contact.click()

            # "Next" button
            next = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='arrow-forward']"))
            )
            next.click()

            # Enter group name
            input_group_name = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@title='Group subject (optional)']//p[@class='selectable-text copyable-text x15bjb6t x1n2onr6']"))
            )
            input_group_name.send_keys(group_name)

            # "Create group" button
            create_grupo = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='checkmark-medium']"))
            )
            create_grupo.click()

            print(f"✅ Grupo '{group_name}' creado.")
            time.sleep(3)

        except Exception as e:
            print(f"⚠️ Error al crear el grupo '{group_name}': {e}")
            continue

print("✅ Todos los grupos fueron procesados.")