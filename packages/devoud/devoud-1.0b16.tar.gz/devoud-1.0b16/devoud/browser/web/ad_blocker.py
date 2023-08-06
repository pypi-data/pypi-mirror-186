from adblockparser import AdblockRules
from devoud.browser import *


class AdBlocker(QObject):
    def __init__(self, parent):
        super().__init__(parent)
        self.rules = None
        self.interceptor = None

    def load_file(self):
        if self.parent().FS.get_option('easyprivacy'):
            print('Внимание!!! Включен блокировщик трекеров, он может замедлить время запуска браузера')
            start_time = time.time()
            with open("./browser/web/easyprivacy.txt") as file:
                self.rules = AdblockRules(file.readlines())
            print("[ %s секунд ]" % (time.time() - start_time))
            return True
        else:
            return False


class WebEngineUrlRequestInterceptor(QWebEngineUrlRequestInterceptor):
    def __init__(self, rules):
        super().__init__()
        self.rules = rules

    def interceptRequest(self, info):
        url = info.requestUrl().toString()
        if self.rules.should_block(url):
            print("[Блокировка]:", url)
            info.block(True)
