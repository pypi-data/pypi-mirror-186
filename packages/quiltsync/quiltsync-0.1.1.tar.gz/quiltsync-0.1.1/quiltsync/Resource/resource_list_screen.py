import os
import json
import logging

from kivymd.app import MDApp
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.screen import MDScreen

from quiltsync.apputils import Notify, load_kv
from quiltplus import QuiltID

load_kv(__name__)

from quiltsync.Resource.resource import Resource

class ResourceList(MDScreen):
    @staticmethod
    def handle_addnew():
        app = MDApp.get_running_app()
        app.sm.get_screen('edit').open()

    def open(self):
        app = MDApp.get_running_app()
        app.switch_screen('resources')
        self.empty = True

    def list_resources(self):
        app = MDApp.get_running_app()
        app.menu.dismiss()
        logging.debug('list_resources: {app.nursery}')

        async def _list_resources(self):
            logging.debug('_list_resources')
            await self._clear_data()
            logging.debug('_list_resources._clear_data')
            results = await Resource.Cache().get()
            logging.debug(f'_list_resources.results {results}')
            if not results or len(results) < 1:
                results = await self._add_default()
            await self._load_data(results)
            logging.debug('_list_resources._load_data')

        app.nursery.start_soon(_list_resources, self)
        logging.debug('+list_resources')

    async def _clear_data(self):
        logging.debug('_clear_data')
        self.ids.loading.active = True
        self.ids.resourcelist.clear_widgets()

    async def _on_error(self, *args): # UNUSED
        self.ids.loading.active = False

    async def _add_qid(self, qid):
        logging.debug(f'_add_qid.qid: {qid}')
        resource = Resource.FromQuiltID(qid)
        logging.debug(f'_add_qid.resource: {resource}')
        self.ids.resourcelist.add_widget(resource)

    async def _load_data(self, results):
        if results:
            for qid in results:
                await self._add_qid(qid)
        self.ids.loading.active = False

    async def _add_default(self):
        uri = os.environ['QUILT_URI']
        qid = QuiltID(uri)
        await Resource.Cache().post(qid.attrs)
        results = await Resource.Cache().get()
        return results

# TODO: ERROR HANDLING

