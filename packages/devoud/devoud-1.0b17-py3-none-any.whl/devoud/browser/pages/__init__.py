from devoud.browser.pages.control_page import ControlPage
from devoud.browser.pages.not_found_page import NotFoundPage
from devoud.browser.pages.void_page import VoidPage

embedded_pages = {'devoud://control': ControlPage,
                  'devoud://notfound': NotFoundPage,
                  'devoud://void': VoidPage}

redirects = {'about:blank': NotFoundPage.url,
             'web://desktop': 'https://dustinbrett.com/',
             'web://macos': 'https://macos9.app/'}
