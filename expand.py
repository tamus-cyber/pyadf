from pyadf.group_node import GroupNode
from pyadf.group_node_children_mixin import GroupNodeChildrenMixin

class Expand(GroupNode, GroupNodeChildrenMixin):
    type = 'expand'
    def __init__(self, title='Click here to expand...', parent=None):
        self.title = title
        super(Expand, self).__init__(parent=parent)

    def attrs(self):
        if self.title:
            return {
                'title': self.title
            }
        return None
