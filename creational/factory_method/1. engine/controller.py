from matcha_view_engine import MatchaViewEngine


class Controller:
    def create_view_engine(self):
        return MatchaViewEngine()

    def render(self, viewname, context):
        engine = self.create_view_engine()
        html = engine.render(viewname, context)
        print(html)