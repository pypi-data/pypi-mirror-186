import os
import logging

from kivy.factory import Factory
from kivymd.uix.screen import MDScreen
from kivy.properties import NumericProperty
from kivymd.app import MDApp

from quiltsync.apputils import Notify, load_kv
from quiltsync.Resource.resource import Resource

load_kv(__name__)


class ResourceEdit(MDScreen):
    resource_id = NumericProperty(None, allownone=True)

    def open(self, resource_id=None):
        self.resource_id = resource_id
        app = MDApp.get_running_app()
        self.ids.bucket.focus = True
        app.switch_screen('edit')

        if resource_id is not None:
            app.nursery.start_soon(self._get_resource)

    def close(self, ref=None):
        self.clear()
        app = MDApp.get_running_app()
        app.sm.get_screen('resources').open()

    async def _get_resource(resource_id):
        logging.debug(f'_get_resource{resource_id}')
        data = await Resource.Cache().get(resource_id)
        await self._load_data(data)

    async def _load_data(self, data):
        logging.debug(f'_load_data: {data}')
        if data:
            self.resource_id = data.id()
            for key in Resource.EDIT_KEYS:
                self.ids[key].text = data.get(key)

    def handle_save(self):
        logging.debug('handle_save')
        self.body = Resource.IdsText(self.ids)
        logging.debug(f'handle_save.body {self.body}')
        app = MDApp.get_running_app()
        app.nursery.start_soon(self._handle_save)

    async def _handle_save(self):
        logging.debug(f'_handle_save: {self.body}')
        if self.resource_id:
            logging.debug(f'_handle_save.put({self.resource_id})')
            result = await Resource.Cache().put(self.body, self.resource_id)
        else:
            logging.debug(f'_handle_save.post')
            result = await Resource.Cache().post(self.body)
        logging.debug(f'_handle_save.DONE: {result}')
        self.save_success()

    def save_success(self):
        Notify(text=f"Resource {'added' if self.resource_id is None else 'updated'}").open()
        self.clear()
        app = MDApp.get_running_app()
        app.sm.get_screen('resources').list_resources()
        app.sm.get_screen('resources').open()

    def clear(self):
        self.resource_id = None
        for key in Resource.EDIT_KEYS:
            self.ids[key].text = ''
