from view_engine import ViewEngine


class SharpViewEngine(ViewEngine):
    def render(self, viewname, context):
        return "View rendered by Sharp"