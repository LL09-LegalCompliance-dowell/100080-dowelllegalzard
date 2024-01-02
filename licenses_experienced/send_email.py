import requests

"""Dowell Mail API services"""
def send_email(toname,toemail,subject,email_content):
    url = "https://100085.pythonanywhere.com/api/email/"
    print(toemail)
    payload = {
        "toname": toname,
        "toemail": toemail,
        "subject": subject,
        "email_content":email_content
    }
    response = requests.post(url, json=payload)
    print(response.text)
    return response.text

EMAIL_FROM_WEBSITE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dowell Open Source License Compatibility Test Information</title>
</head>
<body>
    <div style="font-family: Helvetica,Arial,sans-serif;min-width:100px;overflow:auto;line-height:2">
        <div style="margin:50px auto;width:70%;padding:20px 0">
          <div style="border-bottom:1px solid #eee">
            <a href="#" style="font-size:1.2em;color: #00466a;text-decoration:none;font-weight:600">Dowell UX Living Lab</a>
          </div>
          <p style="font-size:1.1em">Email : {},</p>
          <p style="font-size:1.1em">Title : {}</p>
          <p style="font-size:1.1em">License One : <strong>{}</strong>&nbsp;&nbsp; VS License Two : <strong>{}</strong></p>
          <p style="font-size:1.1em">Recommend using on the same Project/Repository : {}</p>
          <p style="font-size:1.1em"> Percentage of compatibility: {}%</p>
          <p style="font-size:1.1em">Consult your legal team for license amendments, If not fully compatible, follow conditions and add required liabilities & copyright notices for compliance</p>
        </div>
      </div>
</body>
</html>
"""
# dowell@dowellresearch.uk

import re

def is_valid_email(email):
    # Regular expression pattern for a basic email address validation
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # Use re.match to check if the email matches the pattern
    if re.match(email_pattern, email):
        return True
    else:
        return False



