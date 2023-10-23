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
          <p style="font-size:1.1em">License One : {} VS License Two : {}</p>
          <p style="font-size:1.1em">Are the Two Licenses Compatible? : {}</p>
          <p style="font-size:1.1em">Recommend using on the same project : {}</p>
          <p style="font-size:1.1em"> Percentage of compatibility: {}</p>
          <p style="font-size:1.1em">Unique Comparison Identifier: {}</p>
          <p style="font-size:1.1em">Message/Disclaimer: {}</p>
        </div>
      </div>
</body>
</html>
"""
# dowell@dowellresearch.uk



