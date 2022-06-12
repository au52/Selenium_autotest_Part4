from .pages.main_page import MainPage
from .pages.login_page import LoginPage


# Строка для запуска: pytest -v --tb=line --language=en test_main_page.py

#def test_guest_can_go_to_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
#    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#    page.open()                      # открываем страницу
#    page.go_to_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

# Самодельный тест для проверки текущей страницы
# и наличия на ней форм регистрации и логина
# из шага 8 https://stepik.org/lesson/238819/step/9?unit=211271

# def test_login_url_and_login_and_register_form_presented(browser):
#    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
#    page = LoginPage(browser, link)
#    page.open()
#    page.should_be_login_page()

# Это тест из шага 9 https://stepik.org/lesson/238819/step/9?unit=211271,
# который заменяет собой тесты 1 и 3.

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

