import time

import allure
from selene.support import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from estimate_tests.data.users import AdminDev, NoLicenceDev, AdminUserPrev, NoLicenseUserPrev
from selene import have, be, command
from selene.support.shared import browser
import pytest
import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from selene.support.shared import browser
import logging
from estimate_tests.utils import attach
from estimate_tests.utils.date_and_time import current_time_with_sec, today_date

logging.getLogger('WDM').setLevel(logging.ERROR)

"""

Конфигурационный файл для настроек

"""






# import logging
# import time
# logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
# logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
#
#
# def main():
#     while True:
#         logging.Formatter('Date and time')
#         logging.info('Тут что-то происходит')
#         time.sleep(3)
#
#
#
# if __name__ == '__main__':
#     main()

# позволяет переиспользовать пользователя по умолчанию на любого


admin_user_preview = AdminUserPrev()

no_licence_preview = NoLicenseUserPrev()

admin_dev = AdminDev()

no_licence_dev = NoLicenceDev()

preview_link = f"{preview_link}"

stage_link = f'{stage_link}'

dev_link = f'{dev_link}'

def pytest_addoption(parser):
    """
    Parser option
    """
    parser.addoption(
        '--web_remote_driver',
        default='selenoid.autotests.cloud',
        help='web: remote driver'
    )

    parser.addoption(
        '--web_browser',
        default='chrome',
        help='web: browser (chrome or firefox)'
    )

    parser.addoption(
        '--type',
        default='web',
        help='type of tests: web, api, mobile'
    )


# def pytest_addoption(parser):
#     """Declaring the command-line options for test run"""
#     parser.addoption('--browser_name', action='store', default="chrome",
#                      help="Choose browser: chrome, edge or firefox")
#     parser.addoption('--language', action='store', default="ru",
#                      help="Choose language: en, ru, es etc.")
#     parser.addoption('--headless',
#                      default='true',
#                      help='headless options: "true" or "false"')

# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("browser_name")
#     headless = request.config.getoption('--headless')
#     chrome_option = webdriver.ChromeOptions()
#     firefox_option = webdriver.FirefoxOptions()
#     edge_option = webdriver.EdgeOptions()
#     if browser_name == "chrome":
#         if headless == 'true':
#             chrome_option.add_argument('--headless')
#             chrome_option.add_argument('--ignore-certificate-errors')
#         browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
#     elif browser_name == "firefox":
#         if headless == 'true':
#             firefox_option.add_argument('--headless')
#             firefox_option.add_argument('--ignore-certificate-errors')
#         browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_option)
#     elif browser_name == 'edge':
#         if headless == 'true':
#             edge_option.add_argument('--headless')
#             edge_option.add_argument('--ignore-certificate-errors')
#         browser = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_option)
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
#     yield browser
#     browser.quit()

"""
Made for testing from localhost
"""
@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    print('Starting browser')

    browser.config.wait_for_no_overlap_found_by_js = True
    browser.config.browser_name = 'chrome'
    browser.config.hold_browser_open = False
    browser.config.timeout = 6
    browser.config.window_width = 1600
    browser.config.window_height = 900
    yield browser
    # даже если тест упадет закрепы будут в отсчете

    browser.quit()

"""
Version for selenoid tests
"""
@pytest.fixture(scope='function', autouse=False)
def setup_browser(request):
    options = Options()
    browser.config.timeout = 6
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "105.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False,
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="http://selenoid.smeta.ru:4444/wd/hub",
        options=options
    )

    browser.config.driver = driver
    driver.set_window_size(1900, 1000)

    yield browser
    # даже если тест упадет закрепы будут в отсчете
    attach.add_html(browser)
    attach.add_screenshoot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()


@pytest.mark.login
@allure.link(f"{preview_link}")
@pytest.fixture()
def open_login_page():
    browser.open(preview_link)
    browser.should(have.title('Сметный офис'))
    browser.element('[class="form-caption"]')\
        .should(have.text('Вход в офисный пакет для работы со сметными нормативами и документами'))


@pytest.mark.account
@allure.link(f"{preview_link}")
@pytest.fixture()
def auth_user(open_login_page):
    browser.element('#login-input').click().type(admin_user_preview.login)
    browser.element('#password-input').click().type(admin_user_preview.password)
    browser.element('#login-button').click()
    yield
    browser.element("#heared-user-block").click()
    browser.element("#header-dropdown-logout").click()
    browser.element("#login-button").should(be.present)
    print('End Authorization')


@pytest.mark.objects
@allure.link(f"{preview_link}")
@pytest.fixture()
def switch_to_objects_page(auth_user):
    print('Go to estimates')
    browser.element('#go-to-estimates-button').should(be.enabled).click()
    browser.element('#ribbon-title').should(be.present)
    yield
    if browser.element('[aria-label="Auto"] [aria-node-type="Folder"]').matching(be.visible):
        browser.element('[aria-label="Auto"] [aria-node-type="Folder"]').click()
        browser.element('#ribbon-delete').click()
        print('Delete data by fixture')
    else:
        browser.element('[aria-node-type="virtual.root"]').click()
        print('No data to delete')
    browser.element('#ribbon-back-button').should(be.enabled).click()
    print('Back to account')


@pytest.mark.estimates
@allure.link(f"{preview_link}")
@pytest.fixture()
def create_estimate_tsn(switch_to_objects_page):
    browser.element('[role="alert"]').should(be.absent)
    my_estimates = browser.element('[aria-node-type="virtual.root"]')
    my_estimates.wait_until(be.clickable)
    my_estimates.double_click()
    if browser.element('[aria-label="Auto"] [aria-node-type="Folder"]').is_displayed():
        browser.element('[aria-label="Auto"] [aria-node-type="Folder"]').context_click()
        browser.element('#context-menu-Delete').click()
        print('Delete data before test')
        browser.element('[aria-node-type="virtual.root"]').click()
    else:
        print('No data to delete')
        browser.element('[aria-node-type="virtual.root"]').click()
    browser.element("#ribbon-addFolder").click()
    new_folder = browser.element('[aria-label="Новая папка"] [aria-node-type="Folder"]')
    new_folder.wait_until(be.visible)
    time.sleep(2)
    ActionChains(browser.driver).send_keys('Auto').perform()
    auto = browser.element('[aria-label="Auto"] [aria-node-type="Folder"]')
    auto.wait_until(be.visible)
    browser.element('#ribbon-addEstimate').click()
    browser.element('#ec-estimate-name').click().clear().send_keys('TSN_65_' + today_date)
    browser.element('#ec-object-name').click().send_keys('111')
    browser.element('#ec-estimate-code').click().send_keys('1234')
    browser.element('#ec-base-selector').click()
    browser.element('#ec-base-selector-TSN_MGE').click()
    browser.element('#ec-addition-selector').click()
    browser.element('#ec-addition-selector-addition-65').click()
    time.sleep(3)
    browser.element('#edit-estimate-button').should(be.clickable).click()
    browser.element(f'//div[contains(text(), "{"TSN_65_" + today_date}")]').should(be.present)
    browser.all('[col-id="viewNumber"]').element_by(have.text('Раздел 1.')).should(be.visible)
    yield
    attach.add_html(browser)
    attach.add_screenshoot(browser)
    attach.add_logs(browser)
    browser.element('#ribbon-tab-MainTab').click()
    browser.element('#fast-panel-object').click()


@pytest.mark.normatives
@allure.link(f"{preview_link}")
@pytest.fixture()
def switch_to_database_page(switch_to_objects_page):
    browser.element('#ribbon-normatives').should(be.present).click()
    browser.element('[mat-focus-indicator ribbon-button mat-raised-button '
                    'mat-button-base toggle-button-checked]').wait_until(be.visible)
    yield
    attach.add_html(browser)
    attach.add_screenshoot(browser)
    attach.add_logs(browser)
    browser.element('#ribbon-object').click()
    browser.element('#ribbon-tab-MainTab').click()
    browser.element('#fast-panel-object').click()


@pytest.mark.search
@allure.link({preview_link})
@pytest.fixture()
def switch_to_search_page(switch_to_objects_page):
    browser.element('#ribbon-search').should(be.clickable).click()
    browser.element('[class="window-smr"] [class="content-wrapper"]').wait_until(be.visible)
    yield
    browser.element('[class="window-close-button"]').should(be.visible).click()
    browser.element('#ribbon-object').should(be.clickable).click()
    browser.element('#ribbon-tab-MainTab').should(be.clickable).click()
    browser.element('#fast-panel-object').should(be.clickable).click()

