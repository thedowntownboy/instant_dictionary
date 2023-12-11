import justpy as jp
import uvicorn

from webapp.about import About
from webapp.dictionary import Dictionary
from webapp.home import Home

app = jp.app 
jp.Route(About.path, About.serve)
jp.Route(Home.path, Home.serve)
jp.Route(Dictionary.path, Dictionary.serve)
jp.justpy(start_server=False)
uvicorn.run(app)
