import justpy as jp
import definition

class Dictionary:

    path = "/dictionary"

    @classmethod  # is used as self becomes a ticking bomb later as jp changes it to request
    def serve(cls, req):
        wp  = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-300 h-screen")
        jp.Div(a=div, text="Instant Dictionry", classes="text-4xl m2")
        jp.Div(a=div, text="Get the definition of any English word you type.", classes="text-1xl m-3")
        input_div= jp.Div(a=div, classes="grid grid-cols-2")

        output_div = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40")
        input_word = jp.Input(a=input_div, placeholder = "Type in a word...", outputbox=output_div, classes ="m-3 bg-gray-100 border-2 border-gray-200 rounded w-64 focus:bg-white focus:outline-none "
                                                     "focus:border-purple-500 py-2 px-4 ")
        input_word.on('input', cls.get_definition)

        #jp.Button(a=input_div, text="Get Defination", classes="border-2 text-gray-500", click=cls.get_definition, inputbox=input_word, outputbox=output_div)
        return wp


    @staticmethod # acts as a independent function in a class
    def get_definition(widget, msg):
        defined = definition.Defination(widget.value).get()

        widget.outputbox.text = " ".join(defined)


