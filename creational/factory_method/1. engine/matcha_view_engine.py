from view_engine import ViewEngine


class MatchaViewEngine(ViewEngine):
    def render(self, viewname, context):
        return "View rendered by Matcha"