import justpy as jp
from webapp import layout

class About:

    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(
            a=wp)  # view="hHh lpR fFf" is made static in layout page
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="About This APP", classes="text-align-center text-4xl m-2")
        jp.Div(a=div, text="""
        This is a Python Based JustPy app which involves Quasar and Tailwind.
        This Application acts as an instant dictionary where the defination renders
        in real time from the data source. The data source is a .csv file which
        stores 60000+ definitions, feel free to give this App a try.""", classes="text-lg")

        return wp

