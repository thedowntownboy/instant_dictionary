import justpy as jp

class About:

    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is About page", classes="text-align-center text-4xl m-2")
        jp.Div(a=div, text="""
        dc jkdwcj ckjsd ckj sdkjckjs dckjer hcjjegdxcjhebhbhdhjedh,
        c eewhj h ceh wjhjhe hc wh djejejjeje chishe he eg xfg,
        jdbhedgwgg ge dgbnehhcehheoieb dgg bebbbbs,
         xeh xhwexhbwehcbawjhbchjawebchwbechjwebcjhbwejhcb,
         new cjhwe cjhw ehjcw ejc wehc whj cjhw chjew chjw chw""", classes="text-lg")

        return wp

