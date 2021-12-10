class ContactForm:
    def render(self, factory):
        factory.create_textbox(self).render()
        factory.create_button(self).render()