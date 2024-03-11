from fpdf import FPDF
import requests
import os
from datetime import datetime

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'APP Privacy Policy', 0, 1, 'C')
    def add_bulleted_list(self, items, bullet='*'):
        self.set_font('Arial', '', 12)
        for item in items:
            self.cell(0, 10, '    '+ bullet + ' ' + item, 0, 1)

def create_and_upload_app_privacy_policy():
    pdf = PDF()
    pdf.add_page()

    # Subtopic with bold text
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'What Type of Information We Gather', 0, 1)

    # Paragraph with some bold text
    pdf.set_font('Arial', '', 12)
    pdf.write(10, "Because Sample Ltd allows you to add its outputs AppTest legalzard / http://app.com/app on your promotional material (Print advertisements, Websites, Online Ads, Packaging etc.), you must register for an account for the desired services. The registration process asks for your personal information such as but not limited to: ")   
    # Adding a bulleted list
    pdf.ln(10)  # Add a line break
    list_items = ["First Name", "Last Name", "Email Address", "Password"]
    pdf.add_bulleted_list(list_items)
    
    pdf.ln(10)  # Add a line break
    pdf.set_font('Arial', '', 12)
    pdf.write(10, "By the nature of our Service, Sample Ltd will gather non-personally identifiable statistics about the usage of our outputs in your promotions and store that information.")
    
    pdf.ln(20)  # Add a line break
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'How do we use this Information', 0, 1)
    pdf.set_font('Arial', '', 12)
    pdf.write(10, "When you log into the Service, our servers automatically record information that you enter in the app. These server logs may include information such as your web request, Internet Protocol address, browser type, browser language, the date and time of your request, browser user agent, and one or more cookies that may uniquely identify your browser. ")
    
    pdf.ln(10)  # Add a line break
    pdf.set_font('Arial', '', 12)
    pdf.write(10, "When you send email or other communication to Sample Ltd, we may retain those communications in order to process your inquiries, respond to your requests and improve our services. Sample Ltd will not share your personal information without your consent or unless required by law. Sample Ltd will not share your website/app statistics without your consent. ")
    
    pdf.ln(10)  # Add a line break
    pdf.set_font('Arial', '', 12)
    pdf.write(10, "Sample Ltd will not share your personal information without your consent or unless required by law. ")
    pdf.ln(10)  # Add a line break
    pdf.set_font('Arial', '', 12)
    pdf.write(10, "Sample Ltd will not share your website/app statistics without your consent.")
    pdf.ln(10)  # Add a line break
    pdf.set_font('Arial', '', 12)
    pdf.write(10, "Sample Ltd only processes your personal information for the purpose of providing, improving, ensuring the delivery of, and developing new services to users. ")
    pdf.ln(10) 
    pdf.set_font('Arial', '', 12)
    pdf.write(10, "If Sample Ltd becomes involved in a merger, acquisition, or any form of sale of some or all of its assets, we will provide notice before your personal information is transferred and becomes subject to a different privacy policy.")
    
    pdf.ln(20)  # Add a line break
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'How do we protect your Information', 0, 1)
    pdf.set_font('Arial', '', 12)
    pdf.write(10, "Sample Ltd has implemented reasonable security mechanisms to protect Sample Ltd Customer Information and Customer User Data that is maintained on Sample Ltd servers from loss, misuse and unauthorized access, disclosure, alteration and destruction. Examples of these security mechanisms include limited and password-protected access, high security public/private keys, encryption on processed data, and SSL encryption to protect transmission of data.")
    pdf.ln(10)
    pdf.set_font('Arial', '', 12)
    pdf.write(10, "However, please keep in mind that no security system is impenetrable. It may be possible for third parties to intercept or access Sample Ltd Customer Information and Customer User Data in spite of these measures. Sample Ltd cannot guarantee the security of your information and cannot be held responsible for unauthorized access to Sample Ltd Customer accounts.")
    
    pdf.ln(10)  # Add a line break
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Changes to this privacy policy', 0, 1)
    pdf.set_font('Arial', '', 12)
    pdf.write(10, "Sample Ltd retains the discretion to amend or modify this Privacy Policy from time to time. If we make material changes to the way we collect, use or disclose Personally Identifiable Information, we will notify you by posting a clear and prominent announcement on Sample Ltd or through a direct communication to your Sample Ltd account.")
    pdf.ln(10)
    pdf.set_font('Arial', '', 12)
    pdf.write(10, "Sample Ltd uses remarketing to advertise across the internet. Along with the Google Analytics cookie, the DoubleClick cookie is collected by Google based on your browsing history. This helps us gain an understanding of our visitors' Demographics and Interests. The reports are anonymous and cannot be associated with any individual personally identifiable information that you may have shared with us.")
    pdf.ln(10)
    pdf.set_font('Arial', '', 12)
    pdf.write(10, "If you want to opt-out of this, please change your settings by going to Google's Ad Settings page.")
    pdf.ln(10)
    pdf.set_font('Arial', '', 12)
    pdf.write(10, "The terms and conditions along with privacy policies with all references, constitutes the sole and entire agreement of the parties to this agreement with respect to the subject matter contained herein, and supersedes all prior terms and conditions which were agreed by the Customer.")
    
    pdf.ln(20)
    pdf.set_font('Arial', '', 12)
    pdf.write(10, "Contact Details")
    pdf.ln(10)
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, "Email ID: apptestlegalzard@website.com")

    
    
    
    # Generate a timestamp for the filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    temp_pdf_filename = f'{timestamp}_temp_pdf.pdf'
    pdf.output(temp_pdf_filename)

    # Assuming 'pdf' is the correct field based on the error message
    try:
        with open(temp_pdf_filename, 'rb') as pdf_file:
            files = {'pdf': pdf_file}  # Adjust the field name if necessary
            upload_url = 'https://dowellfileuploader.uxlivinglab.online/uploadfiles/upload-pdf-file/'
            response = requests.post(upload_url, files=files)
            print("Response from upload: ", response.text)
            if response.status_code == 201:
                # Parse the response to get the uploaded document URI
                response_data = response.json()
                uploaded_document_uri = response_data.get('file_url')
                print("Uploaded document URL:", uploaded_document_uri)
            else:
                print("Failed to upload the document. Status Code:", response.status_code)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Remove the temporary file
        if os.path.exists(temp_pdf_filename):
            os.remove(temp_pdf_filename)

# Example usage
create_and_upload_app_privacy_policy()
