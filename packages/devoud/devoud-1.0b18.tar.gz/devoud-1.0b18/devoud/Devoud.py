#!/usr/bin/python3
from pyshortcuts import make_shortcut
from devoud.browser import *
from devoud.browser.filesystem import FileSystem
from devoud.browser.main_window import BrowserWindow
from devoud.browser.pages.abstract_page import AbstractPage
from devoud.browser.web.ad_blocker import AdBlocker, WebEngineUrlRequestInterceptor
from devoud.browser.update import update


def main():
    from devoud import __version__
    if len(sys.argv) > 1:
        if sys.argv[1] == 'help':
            return print('Использование:       devoud [ссылка/опция]\n\n'
                         'Доступные опции:\n'
                         ' devoud              запуск браузера\n'
                         ' devoud \'ссылка\'     запустить браузер и открыть ссылку в новой вкладке\n'
                         ' devoud help         помощь по командам\n'
                         ' devoud update       проверить и установить обновления\n'
                         ' devoud version      показать текущую версию браузера\n'
                         ' devoud shortcut     создать ярлык запуска')
        elif sys.argv[1] == 'version':
            return print(f'Devoud ({__version__}) by OneEyedDancer')
        elif sys.argv[1] == 'update':
            update()
        elif sys.argv[1] == 'shortcut':
            FileSystem().create_launch_shortcut()
            return

    print(fr'''---------------------------------------------
  Добро пожаловать в
  _____  ________      ______  _    _ _____  
 |  __ \|  ____\ \    / / __ \| |  | |  __ \ 
 | |  | | |__   \ \  / / |  | | |  | | |  | |
 | |  | |  __|   \ \/ /| |  | | |  | | |  | |
 | |__| | |____   \  / | |__| | |__| | |__| |
 |_____/|______|   \/   \____/ \____/|_____/ 
    ({__version__}) by OneEyedDancer            
---------------------------------------------''')
    os.environ["QT_FONT_DPI"] = "96"
    app = QApplication(sys.argv)

    window = BrowserWindow()

    if len(sys.argv) > 1:
        if AbstractPage.is_url(sys.argv[1]):
            # открытие ссылки в новой вкладке
            window.tab_widget.create_tab(sys.argv[1])

    size = window.screen().availableGeometry()
    window.resize(size.width() * 2 / 3, size.height() * 2 / 3)
    window.show()

    window.change_style()

    ad = AdBlocker(window)
    if ad.load_file():
        interceptor = WebEngineUrlRequestInterceptor(ad.rules)
        window.profile.setUrlRequestInterceptor(interceptor)

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
