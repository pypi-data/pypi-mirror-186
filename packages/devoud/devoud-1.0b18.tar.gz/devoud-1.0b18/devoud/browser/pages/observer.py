import devoud.browser.pages as pages


class PagesObserver:
    _pages = []

    @classmethod
    def pages(cls):
        return cls._pages

    @classmethod
    def urls(cls):
        return list(map(lambda page: page.url, cls._pages))

    @classmethod
    def add_page(cls, page):
        cls._pages.append(page)

    @classmethod
    def remove_page(cls, page):
        cls._pages.remove(page)

    @classmethod
    def control_update_lists(cls):
        for page in cls._pages:
            if isinstance(page.view, pages.ControlPage):
                page.view.update_lists()

    @classmethod
    def update_control_pages(cls):
        for page in cls._pages:
            if isinstance(page.view, pages.ControlPage):
                page.reload()
