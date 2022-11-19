import flet
from flet import (
    Page,
    Container,
    Column,
    border,
    Row,
    padding,
    Text,
    ResponsiveRow,
    LinearGradient,
    alignment,
    PopupMenuButton,
    PopupMenuItem,
    GridView,
)
import random
import importlib, os
from math import ceil

# directory where button modules exist
dir = "./fletton/"
_moduleList = []
# iterate through the sorted files in the directory
for filename in sorted(os.listdir(dir)):
    # get the file path
    _file = os.path.join(dir, filename)
    # check if the file is indeed a file
    if os.path.isfile(_file):
        # strip the .py extension from the file
        filename = filename.strip(".py")
        # create a module and store it in _module
        _module = importlib.import_module(f"fletton." + filename)
        # append the _module to the module list
        _moduleList.append(_module)


def main(page: Page):
    page.title = "Flet UI"

    def _copy_control_data(e):
        page.set_clipboard(e.control.data)

    def _select_tab_(e):
        if isinstance(e.control, flet.popup_menu_button.PopupMenuItem):
            if e.control.text == "Gradients":
                _main_bar_.visible = False
                _main_bar_.update()
                _main_bar_gradient.visible = True
                _main_bar_gradient.update()
            if e.control.text == "Colors":
                _main_bar_.visible = True
                _main_bar_.update()
                _main_bar_gradient.visible = False
                _main_bar_gradient.update()
            if e.control.text == "Animations":
                _main_bar_.visible = False
                _main_bar_.update()
                _main_bar_gradient.visible = False
                _main_bar_gradient.update()
                _main_bar_animation.visible = True
                _main_bar_animation.update()

        else:
            for row in _side_panel_.controls[1:4]:
                (
                    row.controls[0].border,
                    row.controls[0].content.color,
                    row.controls[0].content.data,
                ) = (
                    border.only(left=border.BorderSide(1, "#64748b")),
                    "#64748b",
                    False,
                )
                row.controls[0].update()
                row.controls[0].content.update()

                if e.control.content.data != True:
                    e.control.content.color, e.control.content.data = "white", True
                    e.control.border = border.only(left=border.BorderSide(1, "white"))
                    e.control.update()
                    e.control.content.update()

                if e.control.content.value == "Gradients":
                    _main_bar_.visible = False
                    _main_bar_.update()
                    _main_bar_gradient.visible = True
                    _main_bar_gradient.update()

                elif e.control.content.value == "Colors":
                    _main_bar_.visible = True
                    _main_bar_.update()
                    _main_bar_gradient.visible = False
                    _main_bar_gradient.update()

                elif e.control.content.value == "Animations":
                    _main_bar_.visible = False
                    _main_bar_.update()
                    _main_bar_gradient.visible = False
                    _main_bar_gradient.update()
                    _main_bar_animation.visible = True
                    _main_bar_animation.update()

                else:
                    pass

    def _side_panel_menu(e):
        if e.data == "true":
            if e.control.content.data == True:
                pass
            else:
                e.control.border = border.only(left=border.BorderSide(1, "#f8fafc"))
                e.control.update()
                e.control.content.color = "#f8fafc"
                e.control.content.update()
        else:
            if e.control.content.data == True:
                pass
            else:
                e.control.border = border.only(left=border.BorderSide(1, "#64748b"))
                e.control.update()
                e.control.content.color = "#64748b"
                e.control.content.update()

    def page_resize(e):
        if page.width <= 730:
            _main_row_.controls[1].visible = False
            _main_row_.update()

            _ref_row_.visible = True
            _ref_row_.update()

            _exoand_container.visible = False
            _exoand_container.update()

        else:
            _main_row_.controls[1].visible = True
            _main_row_.update()

            _ref_row_.visible = False
            _ref_row_.update()

            _exoand_container.visible = True
            _exoand_container.update()

        if page.width <= 730:
            _main_bar_.height = page.height - 550
            _main_bar_.update()

            _main_bar_gradient.height = page.height - 550
            _main_bar_gradient.update()
        else:
            _main_bar_.height = page.height - 250
            _main_bar_.update()

            _main_bar_gradient.height = page.height - 250
            _main_bar_gradient.update()

    _color_name_ = [
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

    _color_number = [
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

    _color_white_ = [
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

    # Main Column
    _main_column_ = Column(scroll="auto")
    #
    _title_row_ = ResponsiveRow(
        alignment="center",
        controls=[
            Container(
                alignment=alignment.top_center,
                col={"xs": 12, "sm": 12, "md": 10, "lg": 10, "xl": 12},
                padding=30,
                content=Text(
                    "Open Source UI Designs Programmed In Flet",
                    size=44,
                    weight="w700",
                    text_align="center",
                ),
            )
        ],
    )
    #
    _subtitle_row_ = ResponsiveRow(
        alignment="center",
        controls=[
            Container(
                col={"xs": 10, "sm": 10, "md": 10, "lg": 8, "xl": 6},
                alignment=alignment.center,
                padding=padding.only(bottom=30),
                content=Text(
                    "A collection of Flet's color palette, animations, and linear gradients that you can use as content in any part of your website. Simply click a single color item or gradient and paste the Python code inside your application or project!.",
                    size=16,
                    weight="w300",
                    text_align="center",
                    color="#64748b",
                ),
            )
        ],
    )
    #
    # REF ROW
    _ref_row_ = Row(
        visible=False,
        alignment="start",
        controls=[
            PopupMenuButton(
                items=[
                    PopupMenuItem(
                        text="Colors",
                        on_click=lambda e: _select_tab_(e),
                    ),
                    PopupMenuItem(
                        text="Animations",
                        on_click=lambda e: _select_tab_(e),
                    ),
                    PopupMenuItem(
                        text="Gradients",
                        on_click=lambda e: _select_tab_(e),
                    ),
                ]
            )
        ],
    )

    # COLOR TAB
    _main_bar_column_ = Column(scroll="adaptive")
    _main_bar_ = Container(
        visible=True,
        height=page.height + 300,
        content=_main_bar_column_,
    )
    # Gradient TAB
    _main_bar_gradient_tab_ = Column(scroll="adaptive")
    _main_bar_gradient = Container(
        visible=False,
        height=page.height + 300,
        content=_main_bar_gradient_tab_,
    )
    # ANIMATION TAB
    _main_bar_animation_tab_ = Column(scroll="adaptive")
    _main_bar_animation = Container(
        visible=False,
        height=page.height + 300,
        content=_main_bar_animation_tab_,
    )
    # SIDE PANEL COLUMN
    _side_panel_ = Column(
        spacing=1,
        controls=[
            Row(
                controls=[
                    Container(
                        padding=padding.only(bottom=10),
                        content=Text("Customization"),
                    )
                ]
            ),
            Row(
                controls=[
                    Container(
                        height=30,
                        alignment=alignment.center,
                        padding=padding.only(left=20),
                        on_click=lambda e: _select_tab_(e),
                        on_hover=lambda e: _side_panel_menu(e),
                        border=border.only(left=border.BorderSide(1, "white")),
                        content=Text(
                            "Colors",
                            color="white",
                            data=True,
                        ),
                    )
                ]
            ),
            Row(
                controls=[
                    Container(
                        height=30,
                        alignment=alignment.center,
                        padding=padding.only(left=20),
                        on_hover=lambda e: _side_panel_menu(e),
                        on_click=lambda e: _select_tab_(e),
                        content=Text(
                            "Animations",
                            color="#64748b",
                            data=False,
                        ),
                        border=border.only(left=border.BorderSide(1, "#64748b")),
                    )
                ]
            ),
            Row(
                controls=[
                    Container(
                        height=30,
                        alignment=alignment.center,
                        padding=padding.only(left=20),
                        on_hover=lambda e: _side_panel_menu(e),
                        on_click=lambda e: _select_tab_(e),
                        content=Text(
                            "Gradients",
                            color="#64748b",
                            data=False,
                        ),
                        border=border.only(left=border.BorderSide(1, "#64748b")),
                    )
                ]
            ),
        ],
    )

    # EXPANDED RIGHT CONTIANERS
    _exoand_container = Container(expand=1)

    # MAIN ROW
    _main_row_ = Row(
        alignment="center",
        vertical_alignment="start",
        controls=[
            Container(padding=padding.only(left=20)),
            Container(
                height=200,
                expand=1,
                content=Column(
                    scroll="auto",
                    horizontal_alignment="center",
                    controls=[
                        Container(
                            content=_side_panel_,
                        ),
                    ],
                ),
            ),
            Container(
                expand=6,
                content=Column(
                    controls=[
                        _main_bar_,
                        _main_bar_gradient,
                        _main_bar_animation,
                    ],
                ),
            ),
            # _exoand_container,
            Container(padding=padding.only(left=20)),
        ],
    )

    #
    __main = Container(
        margin=-10,
        height=page.height,
        gradient=LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=["#1f2937", "#111827"],
        ),
        expand=True,
        content=_main_column_,
    )
    page.add(__main)

    _main_column_.controls.append(_ref_row_)
    _main_column_.controls.append(Container(padding=padding.only(top=100)))
    _main_column_.controls.append(_title_row_)
    _main_column_.controls.append(_subtitle_row_)
    _main_column_.controls.append(Container(padding=padding.only(bottom=100)))
    _main_column_.controls.append(_main_row_)

    #
    _white_row = ResponsiveRow(
        run_spacing=10,
        alignment="center",
        vertical_alignment="center",
        controls=[
            Text("BLACK/WHITE", text_align="center"),
        ],
    )
    #
    _white_container = Container(
        alignment=alignment.center,
        content=_white_row,
    )

    _main_bar_column_.controls.append(_white_container)
    page.update()

    #
    for _color in _color_white_:
        _c = Container(
            border_radius=10,
            aspect_ratio=1.25,
            bgcolor=_color,
            col={"xs": 3.175, "sm": 2.25, "md": 2.25, "lg": 1, "xl": 1},
            tooltip=f"{_color}",
            data=_color,
            on_click=lambda e: _copy_control_data(e),
        )
        _white_row.controls.append(_c)
        _white_row.update()

    for _color in _color_name_:
        _ = ResponsiveRow(
            run_spacing=10,
            controls=[Text(f"{_color.upper()}", text_align="center")],
            alignment="center",
            vertical_alignment="center",
        )
        __ = Container(content=_)
        _main_bar_column_.controls.append(__)
        page.update()
        for _number in _color_number:
            __color = f"{_color}{_number}"
            _c = Container(
                border_radius=10,
                aspect_ratio=1.25,
                col={"xs": 3.175, "sm": 2.25, "md": 2.25, "lg": 1, "xl": 1},
                bgcolor=__color,
                tooltip=f"{__color}",
                data=__color,
                on_click=lambda e: _copy_control_data(e),
            )

            _.controls.append(_c)
            _.update()

    _color_state = True
    for row in range(60):
        _ = ResponsiveRow(run_spacing=10, alignment="center")
        __ = Container(content=_)
        _main_bar_gradient_tab_.controls.append(__)
        page.update()

        for nothing in range(4):
            _start = random.choice(_color_name_) + random.choice(_color_number)
            _end = random.choice(_color_name_) + random.choice(_color_number)

            while _color_state == True:
                if _start != _end:
                    _color_state = False
                else:
                    _start = random.choice(_color_name_) + random.choice(_color_number)
                    _end = random.choice(_color_name_) + random.choice(_color_number)
            else:
                _gradient = Container(
                    bgcolor="white",
                    padding=40,
                    border_radius=12,
                    aspect_ratio=1,
                    col={"xs": 12, "sm": 6, "md": 6, "lg": 6, "xl": 3},
                    content=Container(
                        aspect_ratio=1,
                        border_radius=500,
                        gradient=LinearGradient(
                            begin=alignment.bottom_left,
                            end=alignment.top_right,
                            colors=[_start, _end],
                        ),
                        data=f"gradient=LinearGradient(begin=alignment.bottom_left, end=alignment.top_right, colors=['{_start}', '{_end}']),",
                        on_click=lambda e: _copy_control_data(e),
                    ),
                )
                _.controls.append(_gradient)

    _row_ani = ResponsiveRow(
        run_spacing=10,
        alignment="center",
    )
    _main_bar_animation_tab_.controls.append(_row_ani)
    page.update()
    for i in _moduleList:
        _gradient = Container(
            bgcolor="white",
            padding=30,
            border_radius=12,
            aspect_ratio=1,
            col={"xs": 12, "sm": 6, "md": 6, "lg": 4, "xl": 3},
            content=i.Button(),
        )

        _row_ani.controls.append(_gradient)

    page.on_resize = page_resize
    page.update()


if __name__ == "__main__":
    flet.app(target=main)
