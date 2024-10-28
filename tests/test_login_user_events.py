from pages.home_page import HomePage
from pages.header_page import HeaderElements
from pages.personal_page import PersonalPage
from pages.order_history_page import OrderHistoryPage
from pages.login_page import LoginPage
import allure

@allure.suite('Test Login User Events')
class TestLogiUserEvents:
    @allure.title('test open personal page from link klick on home page')
    def test_open_personal_page_from_link_klick_on_home_page(self, login_user):
        homme_page = HomePage(login_user)
        # action_page.ac_click_element(HeaderElements.button_personal_account)
        homme_page.click_button_personal_account()
        pers_page = PersonalPage(login_user)
        # action_page.wait_element(PersonalPage.button_order_history)
        pers_page.wait_button_order_history()
        # assert login_user.current_url == PersonalPage.URL
        pers_page.check_self_current_url()

    @allure.title('test open history page from button on personal page')
    def test_open_history_page_from_button_on_personal_page(self, login_user):
        home_page = HomePage(login_user)
        # action_page.ac_click_element(HeaderElements.button_personal_account)
        home_page.click_button_personal_account()
        # action_page.wait_element(PersonalPage.button_order_history)
        pers_page = PersonalPage(login_user)
        pers_page.wait_button_order_history()
        # action_page.ac_click_element(PersonalPage.button_order_history)
        pers_page.click_button_order_history()
        # action_page.wait_element_off(OrderHistoryPage.load_message)
        order_hist = OrderHistoryPage(login_user)
        order_hist.wait_load_message_off()
        order_hist.check_self_current_url()
        # assert login_user.current_url == OrderHistoryPage.URL

    @allure.title('test open login page from logout button on personal page')
    def test_open_login_page_from_logout_button_on_personal_page(self, login_user):
        home_page = HomePage(login_user)
        # action_page.ac_click_element(HeaderElements.button_personal_account)
        home_page.click_button_personal_account()
        # action_page.wait_element(PersonalPage.button_order_history)
        pers_page = PersonalPage(login_user)
        pers_page.wait_button_order_history()
        # action_page.ac_click_element(PersonalPage.button_logout)
        pers_page.click_button_logout()
        # action_page.wait_element(LoginPage.button_login)
        login_page = LoginPage(login_user)
        login_page.wait_button_login()
        # assert login_user.current_url == LoginPage.URL
        login_page.check_self_current_url()
