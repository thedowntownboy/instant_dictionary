import justpy as jp
from webapp import layout


class Home:

    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp) # view="hHh lpR fFf" is made static in layout page
        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-3")
        jp.Img(a=div, src="/static/webapp/instant_dictionary.png", classes="")
        return wp

