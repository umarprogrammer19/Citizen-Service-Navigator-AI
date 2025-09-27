from agents import Agent
import pdfkit  # For PDF form generation


class FormFillerAgent(Agent):
    def fill_form(self, citizen_data):
        # Use citizen data to fill out a PDF form
        filled_pdf = pdfkit.from_file("form_template.html", False, options=citizen_data)
        return filled_pdf
