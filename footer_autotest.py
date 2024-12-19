import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Настройки для браузера
chrome_options = Options()
chrome_options.add_argument("--headless")  # Запуск без графического интерфейса
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Инициализация драйвера
service = Service(r'C:\Program Files\JetBrains\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

# Список страниц для проверки
pages = [
    "https://only.digital/",
    "https://only.digital/services/",
    "https://only.digital/portfolio/",
    "https://only.digital/blog/",
    "https://only.digital/about/"
]

# Элементы футера, которые нужно проверить
footer_elements = {
    "Логотип в футере": "//footer//img[contains(@src, 'logo')]",
    "Контактная информация": "//footer//a[contains(@href, 'tel:')]",
    "Email в футере": "//footer//a[contains(@href, 'mailto:')]",
    "Ссылки на соцсети": "//footer//a[contains(@href, 'facebook') or contains(@href, 'twitter') or contains(@href, 'instagram')]",
    "Политика конфиденциальности": "//footer//a[contains(text(), 'Политика конфиденциальности')]"
}

# Функция для проверки футера на одной странице
def check_footer_elements(page_url):
    """Проверяет наличие футера и его элементов на странице."""
    results = []
    driver.get(page_url)
    time.sleep(2)  # Ожидание загрузки страницы

    try:
        # Проверяем наличие самого футера
        footer = driver.find_element(By.TAG_NAME, 'footer')
        if footer:
            results.append(f"✅ Футер найден на странице {page_url}")
    except Exception as e:
        results.append(f"❌ Футер НЕ найден на странице {page_url}")

    # Проверяем наличие элементов внутри футера
    for element_name, xpath in footer_elements.items():
        try:
            element = driver.find_element(By.XPATH, xpath)
            if element:
                results.append(f"✅ {element_name} найден на странице {page_url}")
        except Exception as e:
            results.append(f"❌ {element_name} НЕ найден на странице {page_url}")

    return results


# Основной цикл по всем страницам
all_results = []
for page in pages:
    results = check_footer_elements(page)
    all_results.extend(results)

# Завершение работы драйвера
driver.quit()

# Вывод результатов
for result in all_results:
    print(result)
