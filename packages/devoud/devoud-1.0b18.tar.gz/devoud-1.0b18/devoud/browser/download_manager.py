from devoud.browser import *


class DownloadItem(QObject):
    def __init__(self, request: QWebEngineDownloadRequest):
        super().__init__()
        self.request = request
        self.name = request.downloadFileName()
        self.size = request.totalBytes()
        self.request.totalBytesChanged.connect(self.update_size)

        self.date = datetime.now().strftime("%d/%m/%Y(%H-%M)")
        self.source = request.url().toString()
        self.location = str(Path(request.downloadDirectory(), request.downloadFileName()))

    def update_size(self):
        self.size = self.request.totalBytes()


class ListProxy(QObject):
    add = Signal(DownloadItem)
    delete = Signal(DownloadItem)


class DownloadList(list):
    def __init__(self, manager, *args):
        super().__init__(*args)
        self.manager = manager
        self._proxy = ListProxy()
        self.add = self._proxy.add
        self.delete = self._proxy.delete

    def append(self, item):
        item.request.isFinishedChanged.connect(lambda: self.manager.download_finished(item))
        item.request.accept()
        super().append(item)
        self.add.emit(item)
        print(
            f'[Загрузки]: Файл ({item.request.downloadFileName()})[{item.request.downloadDirectory()}] добавлен в очередь для загрузки')

    def remove(self, item):
        try:
            super().remove(item)
        except ValueError:
            pass
        if not item.request.isFinished():
            item.request.cancel()
            self.delete.emit(item)


class DownloadHistoryProxy(QObject):
    delete = Signal(str)


class DownloadManager(QObject):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self._download_list = DownloadList(self)
        self._history = self.get_download_history()
        self._proxy = DownloadHistoryProxy()
        self.history_item_delete = self._proxy.delete

    def list(self):
        return self._download_list

    def history(self):
        return self._history

    def save_download_history(self):
        with Path(self.browser.FS.config_dir(), 'downloads.json').open('w') as file:
            json.dump(self.history(), file, indent=4, ensure_ascii=False)

    def get_download_history(self):
        with Path(self.browser.FS.config_dir(), 'downloads.json').open('r') as file:
            try:
                return json.load(file)
            except json.decoder.JSONDecodeError:
                return {}

    def download_requested(self, request: QWebEngineDownloadRequest):
        DownloadMethod.Method(self.parent(), request)
        DownloadMethod.Method = DownloadMethod.Default

    def download_finished(self, item):
        self._history[item.name] = {'size': item.size,
                                    'date': item.date,
                                    'source': item.source,
                                    'location': item.location}
        print(
            f'[Загрузки]: Файл ({item.request.downloadFileName()})[{item.request.downloadDirectory()}] был загружен')
        notification.notify(
            title='Файл загружен',
            message=item.location,
            app_name='Devoud',
        )
        self.save_download_history()
        self.list().remove(item)


class DownloadMessageBox(QMessageBox):
    def __init__(self, parent, request: QWebEngineDownloadRequest):
        super().__init__(parent)
        self.setWindowTitle('Сохранить в загрузках?')
        self.request = request
        self.setIcon(QMessageBox.Icon.Question)
        self.setText(request.downloadFileName())

        self.save_button = self.addButton('Сохранить', QMessageBox.ButtonRole.YesRole)
        self.save_button.clicked.connect(self.save)

        self.select_button = self.addButton('Выбрать место', QMessageBox.ButtonRole.YesRole)
        self.select_button.clicked.connect(self.select)

        self.cancel_button = self.addButton('Отменить', QMessageBox.ButtonRole.NoRole)
        self.cancel_button.clicked.connect(self.cancel)

        self.exec()

    def save(self):
        download_item = DownloadItem(self.request)
        self.parent().download_manager.list().append(download_item)

    def select(self):
        DownloadMethod.SaveAs(self.parent(), self.request)

    def cancel(self):
        self.request.cancel()
        print('[Загрузки]: Загрузка файла отменена')


class DownloadMethod(QObject):
    @classmethod
    def Default(cls, parent, request: QWebEngineDownloadRequest):
        DownloadMessageBox(parent, request)

    @classmethod
    def SaveAs(cls, parent, request: QWebEngineDownloadRequest):
        path = Path(QFileDialog.getSaveFileName(parent, 'Сохранить файл как', request.downloadFileName())[0])

        if str(path) != '.':
            request.setDownloadFileName(path.name)
            request.setDownloadDirectory(str(path.parent))
            download_item = DownloadItem(request)
            parent.download_manager.list().append(download_item)
        else:
            request.cancel()
            print('[Загрузки]: Загрузка файла отменена')

    Method = Default
