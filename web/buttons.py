import inspect
import time
import flet as ft
from base import FxControls
from components import typography as fxType
from components import block as fxCode


intro = """
Buttons in graphical user interfaces (GUI) serve as interactive elements that allow users to trigger actions or perform specific tasks. They enhance the usability and interactivity of GUIs, making software applications and websites more user-friendly and efficient.
"""


def add_container_shadow():
    return ft.BoxShadow(
        spread_radius=4,
        blur_radius=8,
        color=ft.colors.with_opacity(0.25, "black"),
        offset=ft.Offset(4, 4),
    )


class ButtonOne(ft.Container):
    def __init__(
        self,
        padding=ft.padding.only(left=35, right=35),
        height=45,
        bgcolor="teal",
        border_radius=6,
        alignment=ft.alignment.center,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        ink=True,
    ):
        super().__init__(
            padding=padding,
            height=height,
            bgcolor=bgcolor,
            border_radius=border_radius,
            alignment=alignment,
            clip_behavior=clip_behavior,
            ink=ink,
        )

        self.isPlaying = False

        self.text = ft.Text(
            "Send",
            size=15,
            weight="w800",
            opacity=1,
            animate_opacity=ft.Animation(400, "ease"),
            offset=ft.transform.Offset(0, 0),
            animate_offset=ft.Animation(900, "ease"),
        )

        self.button = ft.Icon(
            name=ft.icons.SEND_SHARP,
            size=15,
            color="white",
            offset=ft.transform.Offset(0, 0),
            animate_offset=ft.Animation(900, "ease"),
        )

        self.content = ft.Row(
            alignment="center",
            vertical_alignment="center",
            controls=[self.button, self.text],
        )

        self.on_click = lambda e: self.__str__(e)
        self.on_hover = lambda e: self.animate_button(e)

    def __str__(self, e) -> None:
        e.page.set_clipboard(inspect.getsource(type(self)))

    def hover_up(self):
        self.button.offset = ft.transform.Offset(2, 0.1)
        self.button.update()
        time.sleep(0.9)

    def hover_down(self):
        self.button.offset = ft.transform.Offset(2, -0.1)
        self.button.update()
        time.sleep(0.9)

    def hover_none(self):
        self.button.offset = ft.transform.Offset(0, 0)
        self.button.update()

    def animate_button(self, e):
        if e.data == "true":
            self.text.opacity = 0
            self.text.offset = ft.transform.Offset(1, 0)

            self.button.offset = ft.transform.Offset(2, 0)
            self.isPlaying = True

            self.button.update()
            self.text.update()

        else:
            self.button.offset = ft.transform.Offset(0, 0)
            self.isPlaying = False

            self.text.opacity = 1
            self.text.offset = ft.transform.Offset(0, 0)

            self.button.update()

        self.text.update()

        while self.isPlaying == True:
            self.hover_up()
            if self.isPlaying == False:
                self.hover_none()
                break
            self.hover_down()
            if self.isPlaying == False:
                self.hover_none()
                break


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
            "Button One",
            "Button Two",
            "Button Three",
        ]

    # Method: Create your layout here. Create your UI inside this list ...
    def fx_controls(self) -> list:
        return [
            ft.Divider(height=35, color="transparent"),
            ft.Divider(height=25, color="transparent"),
            # start your layout design here ...
            fxType.heading(f"Flet Button UI"),
            fxType.paragraph(intro),
            ft.Divider(height=5, color="transparent"),
            ft.Container(
                border=ft.border.all(1, "white10"),
                border_radius=6,
                padding=ft.padding.all(20),
                shadow=add_container_shadow(),
                content=ft.Row(alignment="center", controls=[ButtonOne()]),
            ),
            # end your layout design here ...
            ft.Divider(height=15, color="transparent"),
        ]
