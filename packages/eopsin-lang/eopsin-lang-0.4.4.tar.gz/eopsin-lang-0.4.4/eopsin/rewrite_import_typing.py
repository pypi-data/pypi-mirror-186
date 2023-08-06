from ast import *
from copy import copy
from typing import Optional

"""
Checks that there was an import of dataclass if there are any class definitions
"""


class RewriteImportTyping(NodeTransformer):

    imports_typing = False

    def visit_ImportFrom(self, node: ImportFrom) -> Optional[ImportFrom]:
        if node.module != "typing":
            return node
        assert (
            len(node.names) == 4
        ), "The program must contain one 'from typing import List, Dict, Optional, Union'"
        for i, n in enumerate(["List", "Dict", "Optional", "Union"]):
            assert (
                node.names[i].name == n
            ), "The program must contain one 'from typing import List, Dict, Optional, Union'"
            assert (
                node.names[i].asname == None
            ), "The program must contain one 'from typing import List, Dict, Optional, Union'"
        self.imports_typing = True
        return None

    def visit_ClassDef(self, node: ClassDef) -> ClassDef:
        assert (
            self.imports_typing
        ), "typing must be imported in order to use datum classes"
        return node
