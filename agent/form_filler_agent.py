import pdfkit
from agents import Agent


class FormFillerAgent(Agent):
    def fill_form(self, citizen_data):
        filled_pdf = pdfkit.from_file("form_template.html", False, options=citizen_data)
        return filled_pdf
