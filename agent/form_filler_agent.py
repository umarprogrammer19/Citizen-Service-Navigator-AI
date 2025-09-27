import pdfkit
from fastapi.responses import StreamingResponse
from io import BytesIO
from agents import Agent


class FormFillerAgent(Agent):
    def __init__(self):
        # Set the path to wkhtmltopdf if not found automatically
        self.configuration = pdfkit.configuration(
            wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
        )  # Update this path if needed

    def fill_form(self, citizen_data):
        # Safely extract fields with a default value if missing
        form_data = {
            "name": citizen_data.get("name", "N/A"),
            "address": citizen_data.get("address", "Address not provided"),
            "income": citizen_data.get("monthly_income", "Not specified"),
            "household_size": citizen_data.get("household_size", 0),
            "disability_status": citizen_data.get("disability_status", "Not specified"),
            # Add any other fields needed from citizen_data
        }

        # Generate or fill the form based on the citizen data
        filled_pdf = self.generate_pdf(form_data)
        return filled_pdf

    def generate_pdf(self, form_data):
        # Generate a PDF from the form data (simplified)
        html_content = f"""
        <html>
        <body>
            <h1>Application Form</h1>
            <p>Name: {form_data['name']}</p>
            <p>Address: {form_data['address']}</p>
            <p>Income: {form_data['income']}</p>
            <p>Household Size: {form_data['household_size']}</p>
            <p>Disability Status: {form_data['disability_status']}</p>
        </body>
        </html>
        """

        # Generate the PDF from the HTML content
        pdf_content = pdfkit.from_string(
            html_content, False, configuration=self.configuration
        )

        # Return the PDF content as a binary stream using StreamingResponse
        pdf_stream = BytesIO(pdf_content)
        return StreamingResponse(pdf_stream, media_type="application/pdf")
