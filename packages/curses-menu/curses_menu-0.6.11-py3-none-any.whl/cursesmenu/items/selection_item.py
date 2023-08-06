"""A class for a menu item with an integer return value."""

from typing import Optional

from cursesmenu import CursesMenu
from cursesmenu.items import MenuItem


class SelectionItem(MenuItem):
    """A class for a menu item with an integer return value."""

    def __init__(
        self,
        text: str,
        index: int,
        menu: Optional[CursesMenu] = None,
        *,
        should_exit: bool = False,
        override_index: Optional[str] = None,
    ) -> None:
        """Initialize the item."""
        super().__init__(
            text=text,
            should_exit=should_exit,
            menu=menu,
            override_index=override_index,
        )
        self.index = index

    def get_return(self) -> int:
        """Get the return value."""
        return self.index
