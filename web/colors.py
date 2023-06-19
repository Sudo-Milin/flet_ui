import flet as ft
from base import FxControls
from components import typography as fxType
from components import block as fxCode

pallet_container = ft.Container()

# black & white pallete
bw_pallet = [
    "black",
    "white10",
    "white12",
    "white24",
    "white30",
    "white38",
    "white54",
    "white60",
    "white70",
    "white",
]
bw_row = ft.ResponsiveRow(
    run_spacing=10,
    alignment="center",
    vertical_alignment="center",
)

for color in bw_pallet:
    container = ft.Container(
        border_radius=10,
        aspect_ratio=1.25,
        bgcolor=color,
        col={"xs": 3.175, "sm": 2.25, "md": 2.25, "lg": 1, "xl": 1},
        tooltip=f"{color}",
        data=color,
        on_click=lambda e: e.page.set_clipboard(e.control.data),
    )
    bw_row.controls.append(container)

# rest of the colors
color_list: list = []
color_names: list = [
    "red",
    "pink",
    "purple",
    "deeppurple",
    "indigo",
    "lightblue",
    "cyan",
    "teal",
    "blue",
    "green",
    "lightgreen",
    "lime",
    "yellow",
    "amber",
    "orange",
    "deeporange",
    "brown",
    "bluegrey",
]

color_numbers: list = [
    "50",
    "100",
    "200",
    "300",
    "400",
    "500",
    "600",
    "700",
    "800",
    "900",
]

for color_name in color_names:
    temp_list: list = []
    for color_number in color_numbers:
        temp_list.append(f"{color_name}{color_number}")
    color_list.append(temp_list)


class FxView(ft.View):
    def __init__(
        self,
        page: ft.Page,
        docs: dict,
        route="",  # set your routes here ...
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
            fxType.subtitle(f"Black & White", key=1),
            ft.Divider(height=5, color="transparent"),
            ft.Container(content=bw_row, alignment=ft.alignment.center),
            # end your layout design here ...
            ft.Divider(height=15, color="transparent"),
        ]
