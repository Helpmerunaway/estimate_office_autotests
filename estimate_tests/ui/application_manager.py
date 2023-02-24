from selene.support.shared import browser

from estimate_tests.ui.pages.account_page import AccountPage
from estimate_tests.ui.pages.estimates_page import EstimatesPage
from estimate_tests.ui.pages.login_page import LoginPage
from estimate_tests.ui.pages.normatives_page import NormativesPage

# APPLICATION MANAGER
from estimate_tests.ui.pages.objects_page import ObjectsPage
from estimate_tests.ui.pages.search_page import SearchPage


class ApplicationManager():
	def __init__(self):
		self.login_page = LoginPage()
		self.account_page = AccountPage()
		self.objects_page = ObjectsPage()
		self.estimates_page = EstimatesPage()
		self.normatives_page = NormativesPage()
		self.search_page = SearchPage()

app = ApplicationManager()
