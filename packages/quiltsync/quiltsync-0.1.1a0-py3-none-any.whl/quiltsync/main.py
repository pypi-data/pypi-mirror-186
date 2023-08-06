#!/usr/bin/env python

import os
import trio
import logging
LOGLEVEL = os.environ.get('LOGLEVEL', 'WARNING').upper()
logging.basicConfig(level=LOGLEVEL)

from kivy.uix.screenmanager import RiseInTransition, FallOutTransition, SlideTransition, ScreenManager
# from kivymd.app import MDApp
from kivymd.tools.hotreload.app import MDApp
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.menu import MDDropdownMenu
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.metrics import dp
from kivy.utils import platform
from quiltplus import QuiltID

from json import dumps
from pkg_resources import get_distribution
__version__ = get_distribution('quiltsync').version

if platform == 'android':
    from android import mActivity

class AppConfig():
    TITLE = 'Quilt Desktop Demo'
    SECTION = 'app'
    QUILT_CATALOG = 'https://open.quiltdata.com'
    QUILT_CACHE = 'Documents/QuiltData'
    QUILT_URI = 'quilt+s3://quilt-example#package=examples/echarts@a0ec78f0fadba41b8a6261ad7834a3fae6798a1dc3cc66eb2ff151f372bf3a5a'
    KEY_DESC = {
        'QUILT_CATALOG': 'Default Quilt Catalog for pushing revisions',
        'QUILT_CACHE': 'Relative path to cache Quilt Packages',
        'QUILT_URI': 'Default URI to add if no recents',
    }

    def __init__(self, config):
        self.config = config
        conf_opts = {key: getattr(self, key) for key in AppConfig.KEY_DESC.keys()}
        self.config.setdefaults(AppConfig.SECTION, conf_opts)

    def panel_data(self):
        klist = [{
            "type": "title",
            "title": f"{AppConfig.TITLE} Settings"
        }]
        for key, desc in AppConfig.KEY_DESC.items():
            key_data = {
                "type": "string",
                "title": key.replace('_',' ').title(),
                "desc": desc,
                "section": AppConfig.SECTION,
                "key": key
            }
            klist.append(key_data)
        return klist

    def panel_json(self):
        return dumps(self.panel_data())

    def add_settings_panel(self, settings):
        settings.add_json_panel(AppConfig.TITLE, self.config, data=self.panel_json())

    def update_env(self):
        for key in AppConfig.KEY_DESC.keys():
            os.environ[key] = self.config.get(AppConfig.SECTION, key)
        catalog = os.environ['QUILT_CATALOG']
        QuiltID.DEFAULT_CATALOG = catalog.replace('https://','')

    def update_config(key, value):
        os.environ[key] = value

    def matches_config(config, section):
        return config is self.config and section == AppConfig.SECTION


class AppMenu(MDDropdownMenu):
    def __init__(self):
        self.items = []
        super().__init__(items=self.items, width_mult=3)

    def add_item(self, **kwargs):
        base_item = {"viewclass": "MenuItem",
                     "text": "",
                     "icon": "",
                     "height": dp(48),
                     "on_release": None,
                     }
        base_item.update(kwargs)
        self.items.append(base_item)

    def remove_item(self, item_id):
        self.items = [item for item in self.items if item['id'] != item_id]

    def click(self, ref):
        self.caller = ref
        self.open()


class MenuItem(OneLineIconListItem):
    icon = StringProperty()


class SM(ScreenManager):
    def get_classes(self):
        return {screen.__class__.__name__: screen.__class__.__module__
                for screen in self.screens}


class MainApp(MDApp):
    use_kivy_settings = False

    sm = None
    menu = None
    session_cookie = None
    state = {}
    version = __version__

    # TODO: refactor AppConfig

    def build_config(self, config):
        self.config = AppConfig(config)

    def build_settings(self, settings):
        self.config.add_settings_panel(settings)

    def open_settings(self, *largs):
        self.menu.dismiss()
        MDApp.open_settings(self, *largs)

    def on_config_change(self, config, section, key, value):
        if self.config.matches_config(config, section):
            self.update_config(key, value)

    def on_start(self): 
        logging.debug("on_start")
        self.open_resources()

    def on_stop(self):
         Window.close()

    def open_resources(self):
        logging.debug("open_resources")
        resource_screen = self.sm.get_screen('resources')
        resource_screen.open()
        resource_screen.list_resources()

    # Create state (cache for hot reload)
    def build_app(self, first=False):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_palette = "Pink"

        self.title = "Resources"
        self.icon = 'images/icon.png'

        Window.bind(on_keyboard=self.keyboard_hook)
        if platform in ['win', 'linux', 'macosx']:
            Window.size = (800, 600)

        self.config.update_env()
        self.cache_state()
        KV_FILES = []
        self.sm = SM()
        CLASSES = self.sm.get_classes()

        self.menu = AppMenu()
        self.menu.add_item(id="about", text="About", icon="information", on_release=self.sm.get_screen('about').open)
        self.menu.add_item(id="settings", text="Settings", icon="cog", on_release=self.open_settings)
        self.menu.add_item(id="refresh", text="Refresh", icon="reload", on_release=self.sm.get_screen('resources').open)

        if self.session_cookie is None:
            self.menu.add_item(id="login", text="Login", icon="login", on_release=self.sm.get_screen('login').open)
        else:
            self.menu.add_item(id="logout", text="Logout", icon="logout", on_release=self.sm.get_screen('login').logout)


        return self.sm

    # TODO: cache/restore pending edits
    # Save state for hot reloading
    def cache_state(self):
        if self.sm is None:
            self.state = {'session': None,
                          'current': None,
                          'edit_id': None,
                          }
        else:
            self.state = {'session': self.session_cookie,
                          'current': self.sm.current,
                          'edit_id': self.sm.get_screen('edit').resource_id,
                          }


    # Restore state on hot reload
    def apply_state(self, state):
        self.session_cookie = state['session']
        self.sm.current = state['current']
        if self.sm.current == 'edit':
            self.sm.get_screen('edit').open(state['edit_id'])
        elif self.sm.current == 'resources':
            self.open_resources()



    def keyboard_hook(self, key, scancode, codepoint, modifier, *args):
        if scancode == 27:  # ESC
            if self.sm.current == 'resources':
                if platform == 'android':
                    mActivity.finishAndRemoveTask()
                    return True
                else:
                    return False
            elif self.sm.current == 'edit':
                self.sm.get_screen('edit').close()
                return True
            else:
                self.open_resources()
                return True

    def switch_screen(self, screen_name='resources'):
        logging.debug(f'app.switch_screen: {screen_name}')
        self.menu.dismiss()
        if screen_name == 'login':
            self.sm.transition = RiseInTransition()
        elif self.sm.current == 'login':
            self.sm.transition = FallOutTransition()
        elif self.sm.current == 'resources':
            self.sm.transition = SlideTransition(direction='left')
            self.sm.get_screen('resources').list_resources()
        else:
             self.sm.transition = SlideTransition(direction='right')
        self.sm.current = screen_name
        logging.debug(f'app.switch_screen.current: {self.sm.current}')

    def is_auth(self):
        return self.session_cookie is not None

    async def async_trio(self):
        logging.debug(f'app.async_trio {self.KV_FILES}')
        async with trio.open_nursery() as nursery:
            self.nursery = nursery
            logging.debug(f'app.async_trio.nursery {nursery}')
            async def run_app():
                logging.debug('app.async_trio.async_run')
                await self.async_run(async_lib='trio')
                logging.debug('app.async_trio.done')
                nursery.cancel_scope.cancel()
            logging.debug(f'app.async_trio.start_soon {run_app}')
            nursery.start_soon(run_app)
            #await run_app()

def run():
    app = MainApp()
    trio.run(app.async_trio)

if __name__ == '__main__':
    run()
