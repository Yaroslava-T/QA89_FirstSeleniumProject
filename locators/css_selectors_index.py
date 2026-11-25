from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                          # запускает браузер Chrome

try:
    # open site
    # driver.get("https://telranedu.pages.dev/login") # открывает страницу
    driver.get("https://icarro-v1.netlify.app/login")

    # by tag name
    # поиск первого элемента по имени HTML-тега
    # CSS_SELECTOR — это способ найти HTML - элемент по CSS - селектору.
    # Через CSS - селектор можно искать элемент по разным признакам(тегу, классу, id и тд).
    # Пример: driver.find_element(By.CSS_SELECTOR, "input.login")
    # Можно комбинировать: Это значит: найти тег input с классом login.
    div = driver.find_element(By.TAG_NAME, "div")
    div_1 = driver.find_element(By.CSS_SELECTOR, "div")  # тот же поиск через CSS
    div_2 = driver.find_element(By.XPATH, "//div")  # ищет первый элемент <div> на странице с помощью XPath
    div_3 = driver.find_elements(By.XPATH, "//div")  # ищет все элементы <div> и возвращает список

    h1 = driver.find_element(By.TAG_NAME, "h1")          # первый заголовок h1
    h1_1 = driver.find_element(By.CSS_SELECTOR, "h1")    # h1 через CSS
    h1_2 = driver.find_element(By.XPATH, "//h1")        # ищет первый заголовок <h1> через XPath

    input_box = driver.find_element(By.TAG_NAME, "input")     # первое поле input
    input_1 = driver.find_element(By.CSS_SELECTOR, "input")   # input через CSS
    input_2 = driver.find_element(By.XPATH, "//input")  # ищет первое поле <input> через XPath

    a_list = driver.find_elements(By.TAG_NAME, "a")           # все ссылки на странице
    a_1 = driver.find_elements(By.CSS_SELECTOR, "a")          # все ссылки через CSS
    a_2 = driver.find_elements(By.XPATH, "//a")  # ищет все теги <a> на странице через XPath и возвращает список
    # // a — XPath - выражение, которое означает: найти все элементы < a > в любом месте страницы.

    print(len(a_list))         # количество найденных ссылок

    # поиск по class
    # element = driver.find_element(By.CLASS_NAME, "class_name")
    # by class
    container = driver.find_element(By.CLASS_NAME, "container")  # ищет элемент по class
    container_1 = driver.find_element(By.CSS_SELECTOR, ".container")  # тот же class через CSS selector
    container_2 = driver.find_element(By.XPATH,"//div[@class='container']")  # ищет первый тег <div> с атрибутом class="container" через XPath

    navbar = driver.find_element(By.CLASS_NAME, "navbar-component_nav__1X_4m")  # ищет navbar по class
    navbar_1 = driver.find_element(By.CSS_SELECTOR, ".navbar-component_nav__1X_4m")  # тот же class через CSS
    navbar_2 = driver.find_element(By.XPATH, "//*[@class='navbar-component_nav__1X_4m']")   # ищет любой элемент с class="navbar-component_nav__1X_4m"

    form = driver.find_element(By.CLASS_NAME, "login_login__3EHKB")  # ищет форму login по class
    form_1 = driver.find_element(By.CSS_SELECTOR, ".login_login__3EHKB")  # тот же class через CSS
    form_2 = driver.find_element(By.XPATH, "//*[@class='login_login__3EHKB']")  # ищет любой элемент с class="login_login__3EHKB"

    # поиск по id
    # element = driver.find_element(By.ID, "element_id")
    # by id
    root = driver.find_element(By.ID, "root")  # ищет один элемент по id="root"
    root_1 = driver.find_element(By.CSS_SELECTOR, "#root")  # ищет тот же элемент по id через CSS selector
    root_2 = driver.find_element(By.XPATH, "//*[@id='root']")     # ищет любой элемент с id="root"

    # by id list
    root_2 = driver.find_elements(By.ID, "root")  # ищет все элементы с id="root" и возвращает список
    root_3 = driver.find_elements(By.CSS_SELECTOR, "#root")  # тот же поиск через CSS selector, возвращает список

    # by attribute []
    name_input = driver.find_element(By.CSS_SELECTOR,"[placeholder='Email']")  # ищет элемент по атрибуту placeholder="Email"
    name_input4 = driver.find_element(By.XPATH,"//*[@placeholder='Email']")  # ищет любой элемент с атрибутом placeholder="Email"

    home = driver.find_element(By.CSS_SELECTOR, "[href='/home']")  # ищет элемент по атрибуту href="/home"
    home_1 = driver.find_element(By.XPATH, "//*[@href='/home']")  # ищет любой элемент с атрибутом href="/home"

    name_input2 = driver.find_element(By.CSS_SELECTOR, "input[name='email']")  # ищет тег input с атрибутом name="email"
    name_input3 = driver.find_element(By.XPATH, "//input[@name='email']")  # ищет тег <input> с атрибутом name="email"

    # by Name
    name_input_1 = driver.find_element(By.NAME, "email")  # ищет элемент по атрибуту name="name"

    # by text, only XPath
    login_button = driver.find_element(By.XPATH,"//*[text()='Login']")  # ищет любой элемент (HTML-тег), текст которого полностью равен "Login"



    #icarro
    # start -> ^
    starts = driver.find_element(By.CSS_SELECTOR,"[class^='login']")  # ищет элемент, у которого class начинается с "login"
    # end -> $
    end = driver.find_element(By.CSS_SELECTOR,"[class$='auth-page']")  # ищет элемент, у которого class заканчивается на "auth-page"
    # contains -> *=
    contains = driver.find_element(By.CSS_SELECTOR, "[class*='container']")   # ищет элемент, у которого class содержит "container"

    # ^= — начинается с
    # $= — заканчивается на
    # *= — содержит



finally:
    driver.quit()                                             # полностью закрывает браузер

# driver.close()                                              # закрывает только текущую вкладку
# TAG_NAME      → ищем по HTML-тегу
# CSS_SELECTOR  → ищем через CSS-селектор
# find_element  → один элемент
# find_elements → список элементов
# CLASS_NAME    → по class
# ID            → по id
