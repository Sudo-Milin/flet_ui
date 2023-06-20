import flet as ft
from base import FxControls
from components import typography as fxType
from components import block as fxCode


intro = """
Buttons in graphical user interfaces (GUI) serve as interactive elements that allow users to trigger actions or perform specific tasks. They enhance the usability and interactivity of GUIs, making software applications and websites more user-friendly and efficient.
"""


class ButtonOne(ft.Container):
    def __init__(
        self,
        width: int,
        height=45,
        bgcolor="cyan600",
        border_raidus=8,
    ):
        super().__init__(
            width=width,
            height=height,
            bgcolor=bgcolor,
            border_raidus=border_radius,
        )


class FxView(ft.View):
    def __init__(
        self,
        page: ft.Page,
        docs: dict,
        route="/buttons",  # set your routes here ...
        bgcolor="#23262d",
        padding=0,
    ) -> None:
        self.page = page
        self.docs = docs

        self.page.on_resize = self.fx_dynamics

        self.fx_view = FxControls(
            self.page, self.docs, self.fx_controls(), self.fx_rail()
        )

        super().__init__(route=route, bgcolor=bgcolor, padding=padding)

        self.controls = [ft.Container(expand=True, content=self.fx_view)]

    def fx_dynamics(self, event) -> None:
        if self.page.width <= 850:
            self.fx_view.set_application_to_mobile()
        else:
            self.fx_view.set_application_to_desktop()

    # Method: Create your side rails(fx_right panel) here by passing in strings...
    def fx_rail(self) -> list:
        return [
            "Installation",
            "Application Setup",
            "Configuration",
        ]

    # Method: Create your layout here. Create your UI inside this list ...
    def fx_controls(self) -> list:
        return [
            ft.Divider(height=35, color="transparent"),
            ft.Divider(height=25, color="transparent"),
            # start your layout design here ...
            fxType.heading(f"Button Intro Here"),
            fxType.paragraph(intro),
            # end your layout design here ...
            ft.Divider(height=15, color="transparent"),
        ]
