import smtplib as smt
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import dotenv

dotenv.load_dotenv()

smtp_server = "smtp.gmail.com"
smtp_port = 587
provider = os.getenv("moon_analyzer_provider")  # Ensure valid sender email
emps = os.getenv("moon_analyzer_emps")


def send_verification_email(username, usermail, otp):
    msg = MIMEMultipart("alternative")  # Dual format (HTML and Plain Text)
    msg["From"] = provider
    msg["To"] = usermail
    msg["Subject"] = "Verify Your Email Address"
    msg["Reply-To"] = provider  # Valid reply address
    msg["X-Mailer"] = "Python-Mailer"  # Custom header to avoid spam triggers
    msg["X-Priority"] = "3"  # Priority should not be set to 1 unless necessary

    # Plain text version (important for spam avoidance)
    plain_content = f"""
    Hello {username},
    
    Welcome to MoonAnalyzer!

    Please verify your email address by using the verification code below:
    Verification Code: {otp}

    If you did not sign up for this account, please disregard this email.

    Thanks,
    MoonAnalyzer Team

    Need help? Ask at help.moonAnalyzer@gmail.com or visit our website: {os.getenv('CLIENT_URI')}

    Follow us on:
    Facebook: [Facebook Link]
    Instagram: [Instagram Link]
    Twitter: [Twitter Link]
    YouTube: [YouTube Link]

    Thanks,
    MoonAnalyzer Team
    """

    # HTML version (with minimal, clean design)
    html_content = f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Static Template</title>

    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap"
      rel="stylesheet"
    />
  </head>
  <body
    style="
      margin: 0;
      font-family: 'Poppins', sans-serif;
      background: #ffffff;
      font-size: 14px;
    "
  >
    <div
      style="
        max-width: 680px;
        margin: 0 auto;
        padding: 45px 30px 60px;
        background: #f4f7ff;
        background-image: url('https://res.cloudinary.com/dcspbmii5/image/upload/v1727442674/banner_wo5not.png');
        background-repeat: no-repeat;
        background-size: 800px 452px;
        background-position: top center;
        font-size: 14px;
        color: #434343;
      "
    >
      <div>
        <table style="width: 100%;">
          <tbody>
            <tr style="height: 0;">
              <td>
                <h2 style="font-family: 'Poppins', sans-serif; color: aliceblue;">MoonAnalyzer</h2>
              </td>
              <td style="text-align: right;">
                <span style="font-size: 16px; line-height: 30px; color: #ffffff;">
                  {datetime.now().strftime("%d/%m/%Y")}
                </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div>
        <div
          style="
            margin: 0;
            margin-top: 70px;
            padding: 92px 30px 115px;
            background: #ffffff;
            border-radius: 30px;
            text-align: center;
          "
        >
          <div style="width: 100%; max-width: 489px; margin: 0 auto;">
            <h1
              style="
                margin: 0;
                font-size: 24px;
                font-weight: 500;
                color: #1f1f1f;
              "
            >
              Your OTP
            </h1>
            <p
              style="
                margin: 0;
                margin-top: 17px;
                font-size: 16px;
                font-weight: 500;
              "
            >
              Hey {username},
            </p>
            <p
              style="
                margin: 0;
                margin-top: 17px;
                font-weight: 500;
                letter-spacing: 0.56px;
              "
            >
              Thank you for choosing MoonAnalyzer. Use the following OTP
              to complete the procedure to change your email address. OTP is
              valid for
              <span style="font-weight: 600; color: #1f1f1f;">5 minutes</span>.
              Do not share this code with others, including Archisketch
              employees.
            </p>
            <p
              style="
                margin: 0;
                margin-top: 60px;
                font-size: 40px;
                font-weight: 600;
                letter-spacing: 25px;
                color: #ba3d4f;
              "
            >
              {otp}
            </p>
          </div>
        </div>

        <p
          style="
            max-width: 400px;
            margin: 0 auto;
            margin-top: 90px;
            text-align: center;
            font-weight: 500;
            color: #8c8c8c;
          "
        >
          Need help? Ask at
          <a
            href="mailto:archisketch@gmail.com"
            style="color: #499fb6; text-decoration: none;"
            >help.moonAnalyzer@gmail.com</a
          >
          or visit our
          <a
            href="{os.getenv('CLIENT_URI')}"
            target="_blank"
            style="color: #499fb6; text-decoration: none;"
            >Website</a
          >
        </p>
     

      <div
        style="
          width: 100%;
          max-width: 490px;
          margin: 20px auto 0;
          text-align: center;
          border-top: 1px solid #e6ebf1;
        "
      >
        <p
          style="
            margin: 0;
            margin-top: 40px;
            font-size: 16px;
            font-weight: 600;
            color: #434343;
          "
        >
          MoonAnalyzer
        </p>
        <p style="margin: 0; margin-top: 8px; color: #434343;">
          67/8, 4th Cross Road, Lavella Road, near The Glass House, Bengaluru, Karnataka 560001, India
        </p>
        <div style="margin: 0; margin-top: 16px;">
          <a href="" target="_blank" style="display: inline-block;">
            <img
              width="36px"
              alt="Facebook"
              src="https://res.cloudinary.com/dcspbmii5/image/upload/v1727439141/facebook_rfhy35.png"
            />
          </a>
          <a
            href=""
            target="_blank"
            style="display: inline-block; margin-left: 8px;"
          >
            <img
              width="36px"
              alt="Instagram"
              src="https://res.cloudinary.com/dcspbmii5/image/upload/v1727439257/insta_lpxrpy.png"
            />
          </a>
          <a
            href=""
            target="_blank"
            style="display: inline-block; margin-left: 8px;"
          >
            <img
              width="36px"
              alt="Twitter"
              src="https://res.cloudinary.com/dcspbmii5/image/upload/v1727439257/twitter_ettvvb.png"
            />
          </a>
          <a
            href=""
            target="_blank"
            style="display: inline-block; margin-left: 8px;"
          >
            <img
              width="36px"
              alt="YouTube"
              src="https://res.cloudinary.com/dcspbmii5/image/upload/v1727439258/yt_mcwkqw.png"
            />
          </a>
        </div>
        <p style="margin: 0; margin-top: 16px; color: #434343;">
          Copyright © 2022 Company. All rights reserved.
        </p>
      </div>
    </div>
    </div>
  </body>
</html>

    """

    # Attach both plain and HTML content
    msg.attach(MIMEText(plain_content, "plain"))
    msg.attach(MIMEText(html_content, "html"))

    # SMTP connection
    try:
        s = smt.SMTP(smtp_server, smtp_port)
        s.starttls()
        s.login(provider, emps)
        s.sendmail(provider, usermail, msg.as_string())
    finally:
        s.quit()
