import flet as ft

class MainContainer(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return ft.Container(
            width=275,
            height=60,
            content=ft.Column(
                spacing=5,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Modern Dropdown Control in flet",
                            size=10,
                            weight="w400",
                            color="white54",
                            ),
                    ft.Text("Line Indent",
                            size=30,
                            color="white",
                            weight="bold",
                            ),
                ]
            )
        )


class DropdownContainer(ft.UserControl):
    def __init__(self, initials: str, name: str, gen: str, title: str, description: str, salary: str):
        self.initial = initials
        self.name = name
        self.gen = gen
        self.title = title
        self.description = description
        self.salary = salary

        super().__init__()

    def expand_container(self, event: ft.ControlEvent):
        if self.controls[0].height != 180:
            self.controls[0].height = 180
            event.control.icon = ft.icons.KEYBOARD_DOUBLE_ARROW_DOWN
            self.controls[0].update()

        else:
            event.control.icon = ft.icons.KEYBOARD_DOUBLE_ARROW_LEFT
            self.controls[0].height = 90
            self.controls[0].update()

    def top_container(self):
        return ft.Container(
            width=265,
            height=70,
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(
                                width=40,
                                height=40,
                                bgcolor="white24",
                                border_radius=40,
                                alignment=ft.alignment.center,
                                content=ft.Text(self.initial,
                                                size=11,
                                                color="white",
                                                weight="bold")
                            ),
                            ft.VerticalDivider(width=2),
                            ft.Container(
                                content=ft.Column(
                                    spacing=1,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(self.name, size=11,
                                                color="white"),
                                        ft.Text(self.gen, size=9,
                                                color="white54"),

                                    ]
                                )
                            )
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.Container(
                                content=ft.IconButton(
                                    icon=ft.icons.KEYBOARD_DOUBLE_ARROW_LEFT,
                                    icon_size=20,
                                    on_click=self.expand_container
                                )
                            )
                        ]
                    )
                ]
            )
        )

    def all_employee_data(self):
        items = [
            ["Job Title", self.title],
            ["Description", self.description],
            ["Salary", self.salary],
        ]

        widgets = []
        for item in items:
            widgets.append(
                ft.Row(
                    controls=[
                        ft.Column(
                            expand=1,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            controls=[
                                ft.Text(item[0], size=10,
                                        color="white", weight="bold"),
                            ]
                        ),
                        ft.Column(
                            expand=2,
                            horizontal_alignment=ft.CrossAxisAlignment.END,
                            controls=[
                                ft.Text(item[1], size=9,
                                        color="white54", weight="bold"),
                            ]
                        )
                    ]
                )
            )

        return widgets

    def bottom_container(self):
        title, description, salary = self.all_employee_data()
        return ft.Container(
            width=265,
            height=100,
            # bgcolor="white24",
            content=ft.Column(
                spacing=12,
                controls=[
                    title, description, salary
                ]
            )
        )

    def build(self):
        return ft.Container(
            width=275,
            height=90,
            bgcolor="white10",
            border_radius=11,
            padding=ft.padding.only(left=10, right=10, top=10),
            animate=ft.animation.Animation(400, "decelerate"),
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            content=ft.Column(
                # spacing=5,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    self.top_container(),
                    self.bottom_container()
                ]
            )
        )


def main(page: ft.Page):
    page.title = "Flet Deopdown"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    def on_column_scroll(e: ft.OnScrollEvent):
        print(
            f"Type: {e.event_type}, pixels: {e.pixels}, min_scroll_extent: {e.min_scroll_extent}, max_scroll_extent: {e.max_scroll_extent}"
        )

    main_container = ft.Container(
        width=300,
        height=600,
        bgcolor="black",
        border_radius=40,
        padding=20,
        content=ft.Column(
            controls=[
                ft.Divider(height=20, color="transparent"),
                MainContainer(),
                ft.Divider(height=30, color="white24"),
                ft.Text("Employees", size=12, color="white"),
                ft.Container(
                    padding=10,
                    bgcolor="transparent",
                    border=ft.border.all(1),
                    content=ft.Column(
                        height=380,
                        scroll=ft.ScrollMode.HIDDEN,
                        on_scroll=on_column_scroll,
                        controls=[
                            DropdownContainer('J.T', "Juan F. Torres", "Enginer",
                                              "Senior Software Enginer II", "Full Stack", "$100,000"),
                            DropdownContainer('P.Y', "Phineas F. Yehf", "Lawyer",
                                              "Senior Lawyer", "Civil, Criminal, Family", "$150,000"),
                            DropdownContainer('M.T', "Miguel A. Torres", "Enginer",
                                              "Senior Software Enginer III", "Full Stack", "$300,000"),
                        ]
                    )
                ),

            ]
        )

    )

    page.add(main_container)
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
