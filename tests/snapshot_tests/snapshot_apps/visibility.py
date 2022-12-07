from textual.app import App
from textual.containers import Vertical
from textual.widgets import Static


class Visibility(App):
    """Check that visibility: hidden also makes children invisible;"""

    CSS = """
    Screen {
        layout: horizontal;        
    }
    Vertical {
        width: 1fr;
        border: solid red;
    }

    #container1 {
        visibility: hidden;
    }

    .float {
        border: solid blue;        
    }
    
    /* Make a child of a hidden widget visible again */
    #container1 .float {
        visibility: visible;
    }
    """

    def compose(self):

        yield Vertical(
            Static("foo"),
            Static("float", classes="float"),
            id="container1",
        )
        yield Vertical(
            Static("bar"),
            Static("float", classes="float"),
            id="container2",
        )


if __name__ == "__main__":
    app = Visibility()
    app.run()
