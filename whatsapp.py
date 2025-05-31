from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Configuración de ChromeDriver
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

# Esperar a que cargue la interfaz de chats
try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@aria-label, 'Chat')]"))
    )
except:
    print("❌ No se detectó la interfaz de WhatsApp. Revisá si se cargó bien o si el QR se escaneó.")
    driver.quit()
    exit()

# Leer CSV y crear grupos
with open("grupos_a_crear.csv", newline='') as archivo_csv:
    lector = csv.reader(archivo_csv)
    next(lector)  # encabezado

    for fila in lector:
        nombre_grupo = fila[0].strip()
        if not nombre_grupo:
            continue

        print(f"🔧 Creando grupo: {nombre_grupo}")

        try:
            # Botón flotante de "nuevo chat"
            nuevo_chat = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='new-chat-outline']"))
            )
            nuevo_chat.click()

            # Botón "Nuevo grupo"
            nuevo_grupo = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'New group')]"))
            )
            nuevo_grupo.click()

            # Buscar contacto
            input_busqueda = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search name or number']"))
            )
            input_busqueda.send_keys("Mio Uruguay")

            contacto = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@title='Mio Uruguay']"))
            )
            contacto.click()

            # Botón "Siguiente"
            siguiente = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='arrow-forward']"))
            )
            siguiente.click()

            # Escribir nombre del grupo
            input_nombre_grupo = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@title='Group subject (optional)']//p[@class='selectable-text copyable-text x15bjb6t x1n2onr6']"))
            )
            input_nombre_grupo.send_keys(nombre_grupo)

            # Botón "Crear grupo"
            crear_grupo = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='checkmark-medium']"))
            )
            crear_grupo.click()

            print(f"✅ Grupo '{nombre_grupo}' creado.")
            time.sleep(3)

        except Exception as e:
            print(f"⚠️ Error al crear el grupo '{nombre_grupo}': {e}")
            continue

print("✅ Todos los grupos fueron procesados.")