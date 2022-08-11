from litecart.web_ui.core.fixture.base_application import BaseApplication
from litecart.web_ui.core.utils.common import Common
from litecart.web_ui.core.fixture.session import SessionHelper
from litecart.web_ui.pages.create_account_page import CreateAccountPage
from litecart.web_ui.pages.home_page import HomePage
from litecart.web_ui.pages.regional_settings_page import RegionalSettingsPage


class Application(BaseApplication):

    def __init__(self):
        super(Application, self).__init__()
        self.common = Common(self)
        self.session = SessionHelper(self)
        self.homepage = HomePage(self)
        self.regional_settings_page = RegionalSettingsPage(self)
        self.create_account = CreateAccountPage(self)
