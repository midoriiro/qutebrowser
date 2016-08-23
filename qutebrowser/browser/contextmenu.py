"""Create and mnage a contextual menu."""

import collections

from PyQt5.QtWidgets import QMenu, QAction, QActionGroup

from qutebrowser.utils import usertypes as ut

Trigger = ut.enum('Trigger', [
    'load_status',
    'has_selection',
    'has_link',
    'has_tabs',
    'can_insert',
    'can_go_back',
    'can_go_forward',
    'can_go_to',
    'can_undo',
    'can_redo',
    'has_extra_enabled'
])


class ContextMenu:

    """

    Attributes:
        _menu: The contextual menu widget.
        _order: A list of menu order.
        _action_dict: An OrderedDict of actions definition.

    """

    def __init__(self):
        self._menu = None

        self._action_dict = collections.OrderedDict()

        self._action_dict['common'] = collections.OrderedDict()
        self._action_dict['common']['pin'] = {
            'text': 'Pin',
            'icon': None,
            'checkable': True,
            'checked': False,
        }
        self._action_dict['common']['mute'] = {
            'text': 'Mute',
            'icon': None,
            'checkable': True,
            'checked': False,
        }
        self._action_dict['common']['print'] = {
            'text': 'Print',
            'icon': None,
        }
        self._action_dict['common']['screenshot'] = {
            'text': 'Screenshot',
            'icon': None,
            'trigger': {
                'when': Trigger.load_status,
                'then': ut.LoadStatus.success or ut.LoadStatus.success_https
            }
        }

        self._action_dict['search'] = collections.OrderedDict()
        self._action_dict['search']['for'] = {
            'text': 'Search for {}',
            'icon': None,
            'trigger': Trigger.has_selection
        }

        self._action_dict['open'] = collections.OrderedDict()
        self._action_dict['open']['current'] = {
            'text': 'Open Link',
            'icon': None,
            'trigger': Trigger.has_link
        }
        self._action_dict['open']['tab'] = {
            'text': 'Open Link in New Tab',
            'icon': None,
            'trigger': Trigger.has_link
        }
        self._action_dict['open']['tab_background'] = {
            'text': 'Open Link in New Background Tab',
            'icon': None,
            'trigger': Trigger.has_link
        }
        self._action_dict['open']['window'] = {
            'text': 'Open Link in New Window',
            'icon': None,
            'trigger': Trigger.has_link
        }
        self._action_dict['open']['window_background'] = {
            'text': 'Open Link in New Background Window',
            'icon': None,
            'trigger': Trigger.has_link
        }

        self._action_dict['duplicate'] = collections.OrderedDict()
        self._action_dict['duplicate']['tab'] = {
            'text': 'Duplicate Tab',
            'icon': None,
        }
        self._action_dict['duplicate']['tab_background'] = {
            'text': 'Duplicate Tab in Background',
            'icon': None,
        }
        self._action_dict['duplicate']['window'] = {
            'text': 'Duplicate Window',
            'icon': None,
        }
        self._action_dict['duplicate']['window_background'] = {
            'text': 'Duplicate Window in Background',
            'icon': None,
        }

        self._action_dict['move'] = collections.OrderedDict()
        self._action_dict['move']['to_first'] = {
            'text': 'Move to First',
            'icon': None,
            'trigger': Trigger.has_tabs
        }
        self._action_dict['move']['to_last'] = {
            'text': 'Move to Last',
            'icon': None,
            'trigger': Trigger.has_tabs
        }
        self._action_dict['move']['to_left'] = {
            'text': 'Move to Left',
            'icon': None,
            'trigger': Trigger.has_tabs
        }
        self._action_dict['move']['to_right'] = {
            'text': 'Move to Right',
            'icon': None,
            'trigger': Trigger.has_tabs
        }
        self._action_dict['move']['to'] = {
            'text': 'Move to',
            'icon': None  # TODO menu
        }

        self._action_dict['close'] = collections.OrderedDict()
        self._action_dict['close']['current'] = {
            'text': 'Close',
            'icon': None,
        }
        self._action_dict['close']['similar'] = {
            'text': 'Close Similar Tabs',
            'icon': None,
            'trigger': Trigger.has_tabs
        }
        self._action_dict['close']['other'] = {
            'text': 'Close Other Tabs',
            'icon': None,
            'trigger': Trigger.has_tabs
        }
        self._action_dict['close']['left'] = {
            'text': 'Close Left Tabs',
            'icon': None,
            'trigger': Trigger.has_tabs
        }
        self._action_dict['close']['right'] = {
            'text': 'Close Right Tabs',
            'icon': None,
            'trigger': Trigger.has_tabs
        }

        self._action_dict['link'] = collections.OrderedDict()
        self._action_dict['link']['copy_link'] = {
            'text': 'Copy Link',
            'icon': None,
            'trigger': Trigger.has_link
        }
        self._action_dict['link']['copy_image'] = {
            'text': 'Copy Image',
            'icon': None,
            'trigger': Trigger.has_link
        }
        self._action_dict['link']['copy_image_link'] = {
            'text': 'Copy Image Link',
            'icon': None,
            'trigger': Trigger.has_link
        }
        self._action_dict['link']['save_link'] = {
            'text': 'Save Link...',
            'icon': None,
            'trigger': Trigger.has_link
        }
        self._action_dict['link']['save_image'] = {
            'text': 'Save Image...',
            'icon': None,
            'trigger': Trigger.has_link
        }

        self._action_dict['clipboard'] = collections.OrderedDict()
        self._action_dict['clipboard']['cut'] = {
            'text': 'Cut',
            'icon': None,
            'trigger': Trigger.has_selection
        }
        self._action_dict['clipboard']['copy'] = {
            'text': 'Copy',
            'icon': None,
            'trigger': Trigger.has_selection
        }
        self._action_dict['clipboard']['paste'] = {
            'text': 'Paste',
            'icon': None,
            'trigger': Trigger.can_insert
        }

        self._action_dict['history'] = collections.OrderedDict()
        self._action_dict['history']['back'] = {
            'text': 'Go Back',
            'icon': None,
            'trigger': Trigger.can_go_back
        }
        self._action_dict['history']['forward'] = {
            'text': 'Go Forward',
            'icon': None,
            'trigger': Trigger.can_go_forward
        }
        self._action_dict['history']['to'] = {
            'text': 'Go to',
            'icon': None,
            'trigger': Trigger.can_go_to
        }

        self._action_dict['stack'] = collections.OrderedDict()
        self._action_dict['stack']['undo'] = {
            'text': 'Undo',
            'icon': None,
            'trigger': Trigger.can_undo
        }
        self._action_dict['stack']['redo'] = {
            'text': 'Redo',
            'icon': None,
            'trigger': Trigger.can_redo
        }

        self._action_dict['loading'] = collections.OrderedDict()
        self._action_dict['loading']['reload'] = {
            'text': 'Reload',
            'icon': None,
            'trigger': {
                'when': Trigger.load_status,
                'then': ut.LoadStatus.success or ut.LoadStatus.success_https
            }
        }
        self._action_dict['loading']['force_reload'] = {
            'text': 'Force Reload',
            'icon': None,
            'trigger': {
                'when': Trigger.load_status,
                'then': ut.LoadStatus.success or ut.LoadStatus.success_https
            }
        }
        self._action_dict['loading']['stop'] = {
            'text': 'Stop',
            'icon': None,
            'trigger': {
                'when': Trigger.load_status,
                'then': ut.LoadStatus.loading
            }
        }
        self._action_dict['loading']['stop_all'] = {
            'text': 'Stop All',
            'icon': None,
            'trigger': {
                'when': Trigger.load_status,
                'then': ut.LoadStatus.loading
            }
        }

        self._action_dict['page'] = collections.OrderedDict()
        self._action_dict['page']['save'] = {
            'text': 'Save Page',
            'icon': None,
            'trigger': {
                'when': Trigger.load_status,
                'then': ut.LoadStatus.success or ut.LoadStatus.success_https
            }
        }
        self._action_dict['page']['save_as'] = {
            'text': 'Save Page as...',
            'icon': None,
            'trigger': {
                'when': Trigger.load_status,
                'then': ut.LoadStatus.success or ut.LoadStatus.success_https
            }
        }

        self._action_dict['bookmark'] = collections.OrderedDict()
        self._action_dict['bookmark']['link'] = {
            'text': 'Bookmark Link',
            'icon': None,
            'trigger': Trigger.has_link
        }
        self._action_dict['bookmark']['page'] = {
            'text': 'Bookmark Page',
            'icon': None,
            'trigger': {
                'when': Trigger.load_status,
                'then': ut.LoadStatus.success or ut.LoadStatus.success_https
            }
        }

        self._action_dict['extra'] = collections.OrderedDict()
        self._action_dict['extra']['inspect'] = {
            'text': 'Inspect Element',
            'icon': None,
            'trigger': Trigger.has_extra_enabled
        }

        self._order = [k for k in self._action_dict.keys()]

    def _init_menu(self, widget):
        self._menu = QMenu(widget)

        for section in self._order:
            for k in self._action_dict[section].keys():
                action = QAction(self._menu)

                try:
                    action.setCheckable(
                        self._action_dict[section][k]['checkable']
                    )
                    action.setChecked(self._action_dict[section][k]['checked'])
                except:
                    pass
                finally:
                    action.setText(self._action_dict[section][k]['text'])
                    #action.setIcon(self._action_dict[section][k]['icon']) TODO

                self._action_dict[section][k]['object'] = action

                self._menu.addAction(action)

            self._menu.addSeparator()
