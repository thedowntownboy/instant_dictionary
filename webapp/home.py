import justpy as jp


class Home:

    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)



        drawer = jp.QDrawer(a=layout, show_if_above=True, v_model="left", bordered="true")
        scroller = jp.QScrollArea(a=drawer, classes="fit")
        qlist = jp.QList(a=scroller)
        a_classes = "p-2 m-2 text-lg text-red-400 hover:text-red-700"
        jp.A(a=qlist, text="Home",href="/home", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictionary",href="/dictionary", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About",href="/about", classes=a_classes)
        jp.Br(a=qlist)

        btn = jp.QBtn(a=toolbar, dense=True, flat=True, round=True,
                      icon="menu",
                      click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")
        container = jp.QPageContainer(a=layout)
        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-3")
        jp.Div(a=div, text="This is a home Page", classes="text-4xl m2")
        return wp

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True