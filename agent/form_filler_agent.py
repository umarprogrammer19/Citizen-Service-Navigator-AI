import pdfkit  # PDF generation library
from agents import Agent


class FormFillerAgent(Agent):
    def fill_form(self, citizen_data):
        # Example: Create a form based on citizen data
        form_data = {
            "name": citizen_data["name"],
            "address": citizen_data["address"],
            "income": citizen_data["income"],
            # Add other fields as necessary
        }

        # Create or fill an existing PDF form (simplified)
        filled_pdf = self.generate_pdf(form_data)
        return filled_pdf

    def generate_pdf(self, form_data):
        # Generate a PDF form using citizen data (for simplicity)
        html_content = f"""
        <html>
        <body>
            <h1>Application Form</h1>
            <p>Name: {form_data['name']}</p>
            <p>Address: {form_data['address']}</p>
            <p>Income: {form_data['income']}</p>
        </body>
        </html>
        """
        return pdfkit.from_string(
            html_content, False
        )  
