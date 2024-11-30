from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

from kangeki.settings import Settings


class KangekiApp(App):
    """
    A simple mood-tracker and micro-journal application
    for the terminal.
    """

    TITLE = "kangeki"
    ENABLE_COMMAND_PALETTE = False

    BINDINGS = [("ctrl+q", "quit", "Quit")]

    def __init__(self, settings: Settings):
        super().__init__()

        self.settings = settings
        self.theme = self.settings.theme

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()


def main():
    settings = Settings()

    app = KangekiApp(settings)
    app.run()


if __name__ == "__main__":
    main()
