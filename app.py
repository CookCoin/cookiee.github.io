import flet as ft


async def main(page: ft.Page) -> None:
    page.title = "COOKCLIKER"
    page.theme_mode = ft. ThemeMode.DARK
    page.bgcolor = "#141221"
    page.vertical_alignmrnt = ft.MainAxisAlignment.CENTER
    page.horizontal_alignmrnt = ft.CrossAxisAlignment.CENTER
    page.fonts = {"FulboArgenta": "fonts/FulboArgenta.ttf"}
    page.theme = ft.Theme(font_family="FulboArgenta")

    async def score_up(event: ft.ContainerTapEvent) -> None:
        pass

    score = ft.Text(value="0", size=100, data=0)
    score_counter = ft.Text(
        size=50, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN)
    )
    image = ft.Image(
        src="Cookiecook.png",
        fit=ft.ImageFit.CONTAIN,
        animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE)
    )
    progress_bar = ft.ProgressBar(
        value=0,
        width=page.width - 100,
        bar_height=25,
        color="#ff8b1f",
        bgcolor="#FFFFFF",
        )

    await page.add_async(
    score,
        ft.Container(
            content=ft.Stack(controls=[image, score_counter]),
            on_click=score_up,
            margin=ft.Margin(0, 0 , 0 , 30)
        ),
        ft.Container(
            content=progress_bar,
            border_radius=ft.BorderRadius(10, 10, 10, 10),
        )
    )


if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)

