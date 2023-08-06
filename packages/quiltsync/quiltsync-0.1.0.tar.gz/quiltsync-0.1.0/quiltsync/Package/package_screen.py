import os
import json
import logging

from pathlib import Path
from kivymd.app import MDApp
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.screen import MDScreen
from kivy.properties import NumericProperty, StringProperty

from quiltsync.apputils import Notify, load_kv
from quiltsync.Resource.resource import Resource
from quiltplus import QuiltID, QuiltPackage

load_kv(__name__)

class PackageContent(MDCardSwipe):
    name = StringProperty()
    path = StringProperty()

    @staticmethod
    def FromFile(file, dest):
        root = Path(dest)
        path = root / file
        widget = PackageContent(name=file, path=str(path))
        return widget

class PackageView(MDScreen):
    resource_id = NumericProperty(None, allownone=True)
    title = StringProperty()
    uri = StringProperty()
    local_dir = StringProperty()

    @staticmethod
    def AppRun(async_method, arg=None):
        app = MDApp.get_running_app()
        if arg:
            app.nursery.start_soon(async_method, arg)
        else:
            app.nursery.start_soon(async_method)
        return app       

    @staticmethod
    async def FromResourceID(resource_id):
        logging.debug(f'FromResourceID.resource_id {resource_id}')
        qid = await Resource.Cache().get(resource_id)
        logging.debug(f'FromResourceID.qid {qid}')
        pkg = QuiltPackage(qid)
        logging.debug(f'FromResourceID.pkg {pkg}')
        return pkg


    def open(self, resource_id):
        logging.debug(f'PackageView.open: {resource_id}')
        self.resource_id = resource_id
        self.ids.pkg_loading.active = True
        app = self.AppRun(self._setup)
        logging.debug(f'PackageView.switch_screen: package')
        app.switch_screen('package')

    async def _setup(self):
        logging.debug(f'PackageView._setup: {self}')
        self.pkg = await PackageView.FromResourceID(self.resource_id)
        logging.debug(f'PackageView._setup.pkg: {self.pkg}')
        self.title = f'{self.resource_id}: {self.pkg.name}'
        self.uri = self.pkg.id.quilt_uri()
        self.local_dir = self.pkg.dest()

        files = await self.pkg.list()
        logging.debug(f'PackageView._setup.files: {files}')
        for file in files:
            logging.debug(f'PackageView._setup.file: {file}')
            widget = PackageContent.FromFile(file, self.local_dir)
            logging.debug(f'_setup[{file}]: {widget}')
            self.ids.pkg_content.add_widget(widget)

        self.ids.pkg_loading.active = False

    def do_edit(self, ref=None):
        app = MDApp.get_running_app()
        app.sm.get_screen('edit').open(self.resource_id)

    def close(self, ref=None):
        self.clear()
        app = MDApp.get_running_app()
        app.sm.get_screen('resources').open()

    def clear(self):
        self.resource_id = None
        self.title = ''
        self.uri = ''
        self.local_dir = ''
        self.pkg = None
        self.ids.pkg_loading.active = True
        self.ids.pkg_content.clear_widgets()

    def do_download(self, file=None):
        logging.debug(f'do_download: {file}')
        self.AppRun(self._do_download, file)

    async def _do_download(self, file=None):
        logging.debug(f'_do_download: {file}')
        result = await self.pkg.getAll()
        logging.debug(f'_do_download.result: {result}')
