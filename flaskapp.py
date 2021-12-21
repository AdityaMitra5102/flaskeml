import smtplib
from flask import *

senderacc="adityamitra5102devacc@gmail.com"
senderpass="DevPassword1"

app=Flask(__name__)

def sendEmail(eml,name,loc):
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login(senderacc, senderpass)
	subject=str(name)+' is in a danger.'
	html_content=str(name)+' is in a danger. Location https://google.com/maps?q='+str(loc)
	message = "Subject:"+str(subject)+"\n\n"+str(html_content)
	s.sendmail(senderacc, eml, message)
	s.quit()

@app.route("/",methods=['POST','GET'])
def home():
	eml=request.args.get('eml')
	nm=request.args.get('nm')
	loc=request.args.get('loc')
	print(eml,nm,loc)
	sendEmail(eml,nm,loc)
	return ""
	
app.run()