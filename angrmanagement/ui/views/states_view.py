from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtCore import QSize

from .view import BaseView
from ..widgets.qstate_table import QStateTable


class StatesView(BaseView):
    def __init__(self, instance, default_docking_position, *args, **kwargs):
        super(StatesView, self).__init__('states', instance, default_docking_position, *args, **kwargs)

        self.base_caption = 'States'
        self._state_table = None  # type: QStateTable

        self._init_widgets()

    def reload(self):
        self._state_table.state_manager = self.instance.states

    def sizeHint(self):
        return QSize(400, 800)

    def _init_widgets(self):
        self._state_table = QStateTable(self.instance, self, selection_callback=self._on_state_selected)

        hlayout = QHBoxLayout()
        hlayout.addWidget(self._state_table)
        hlayout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(hlayout)

    def _on_state_selected(self, state):
        """
        A new function is on selection right now. Update the disassembly view that is currently at front.

        :param function:
        :return:
        """

        pass
