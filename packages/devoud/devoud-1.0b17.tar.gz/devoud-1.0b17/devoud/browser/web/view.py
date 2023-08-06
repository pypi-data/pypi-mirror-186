from devoud.browser import *
from devoud.browser.context_menu import BrowserContextMenu
from devoud.browser.download_manager import DownloadMethod
from devoud.browser.web.search_engines import search_engines


class BrowserWebView(QWebEngineView):
    def __init__(self, parent):
        super().__init__()
        self.window = parent.window
        self.FS = parent.window.FS
        self.parent = parent
        self.profile = parent.window.profile
        self.embedded = False
        self.menu = None
        self.title = 'Нет названия'
        self.setPage(QWebEnginePage(self.window.profile, self))

        QShortcut(QKeySequence("F11"), self).activated.connect(self.toggle_fullscreen)

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.parent.layout().addWidget(self)
            self.showNormal()
            self.window.show()
        else:
            self.setParent(None)
            self.showFullScreen()
            self.window.hide()

    def save_image_as(self):
        DownloadMethod.Method = DownloadMethod.SaveAs
        self.page().triggerAction(QWebEnginePage.DownloadImageToDisk)

    def createWindow(self, type_):
        if type_ == QWebEnginePage.WebBrowserTab:
            # запрос на новую вкладку
            return self.window.tab_widget.create_tab()

    def contextMenuEvent(self, event):
        self.menu = BrowserContextMenu(self.window)
        self.menu.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        page = self.page()

        if self.lastContextMenuRequest().selectedText():
            self.menu.addAction('Копировать', lambda: page.triggerAction(QWebEnginePage.Copy))
            self.menu.addSeparator()
            self.menu.addAction(f'Поиск в {self.FS.get_option("searchEngine")}', lambda: self.window.tab_widget.create_tab(
                f'{search_engines[self.FS.get_option("searchEngine")][0]}{page.selectedText()}'))
        elif self.lastContextMenuRequest().mediaType() == QWebEngineContextMenuRequest.MediaTypeImage:
            media_url = self.lastContextMenuRequest().mediaUrl().toString()
            self.menu.addAction('Копировать изображение',
                                lambda: page.triggerAction(QWebEnginePage.CopyImageToClipboard))
            self.menu.addAction('Копировать ссылку на изображение',
                                lambda: page.triggerAction(QWebEnginePage.CopyImageUrlToClipboard))
            self.menu.addAction('Сохранить изображение как', self.save_image_as)
            self.menu.addAction('Открыть в новой вкладке',
                                lambda: self.window.tab_widget.create_tab(media_url, switch=False))
        elif self.lastContextMenuRequest().linkUrl().isValid():
            link = self.lastContextMenuRequest().linkUrl().toString()
            self.menu.addAction('Копировать ссылку', lambda: page.triggerAction(QWebEnginePage.CopyLinkToClipboard))
            self.menu.addAction('Открыть ссылку',
                                lambda: self.window.tab_widget.current().load(link))
            self.menu.addAction('Открыть в новой вкладке',
                                lambda: self.window.tab_widget.create_tab(link, switch=False))
        self.menu.addSeparator()
        self.menu.addAction('Выделить всё', lambda: page.triggerAction(QWebEnginePage.SelectAll))
        self.menu.addAction('Назад', self.back)
        self.menu.addAction('Вперед', self.forward)
        self.menu.addAction('Перезагрузить', lambda: page.triggerAction(QWebEnginePage.Reload))
        self.menu.addSeparator()
        self.menu.addAction('Посмотреть исходники', lambda: page.triggerAction(QWebEnginePage.ViewSource))
        self.menu.popup(event.globalPos())
