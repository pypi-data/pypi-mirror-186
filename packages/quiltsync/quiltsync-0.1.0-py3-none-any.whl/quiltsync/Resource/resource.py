import logging
from kivymd.app import MDApp
from kivymd.uix.card import MDCardSwipe
from kivy.properties import NumericProperty, StringProperty

from quiltsync.apputils import Notify, load_kv
from quiltplus import QuiltIdCache,QuiltPackage
from .confirm import ConfirmDialog


class Resource(MDCardSwipe):
    CARD_KEYS = ["resource_id", "text", "secondary_text"]
    EDIT_KEYS = ['bucket', 'package', 'top_hash', 'tag']

    _CACHE = None
    @classmethod
    def Cache(cls):
        if not cls._CACHE:
            cls._CACHE = QuiltIdCache() # TODO: use envar for path
        return cls._CACHE

    @classmethod
    def FromQuiltID(cls, qid):
        attrs = qid.with_keys(*cls.CARD_KEYS)
        return cls(**attrs)

    @classmethod
    def IdsText(cls, ids):
        return {k: ids[k].text for k in cls.EDIT_KEYS}


    resource_id = NumericProperty()
    text = StringProperty()
    secondary_text = StringProperty()

    def __init__(self, **kw):
        logging.debug(f'Resource.__init__({kw})')
        super().__init__(**kw)
        logging.debug('Resource.dialog')
        self.deletion = ConfirmDialog(title="Delete Resource",
                                    text=f"Are you sure you want to permanently delete '{self.text}'?",
                                    on_ok=self.start_delete)
        logging.debug('+Resource.dialog')

    def __repr__(self):
        args = f'resource_id={self.resource_id},text={self.text},secondary_text={self.secondary_text}'
        return f"Resource({args})"

    def __str__(self):
        return self.__repr__()

    def start_delete(self):
        self.deletion.dismiss()
        app = MDApp.get_running_app()
        app.nursery.start_soon(self.do_delete)

    async def do_delete(self):
        await Resource.Cache().delete(self.resource_id)
        Notify(text="Resource deleted").open()
        app.sm.get_screen('resources').list_resources()

    def handle_delete(self):
        if self.open_progress > 0.0:
            self.deletion.open()

    def handle_edit(self, resource_id):
        logging.debug(f'handle_edit: {resource_id}')
        if self.open_progress == 0.0:
            app = MDApp.get_running_app()
            app.sm.get_screen('edit').open(resource_id)

    def handle_package(self, resource_id):
        logging.debug(f'handle_package: {resource_id}')
        if self.open_progress == 0.0:
            app = MDApp.get_running_app()
            app.sm.get_screen('package').open(resource_id)



