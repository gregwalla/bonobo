from unittest.mock import MagicMock

from bonobo.execution import NodeExecutionContext


class CapturingNodeExecutionContext(NodeExecutionContext):
    def __init__(self, wrapped, parent):
        super().__init__(wrapped, parent)
        self.send = MagicMock()
