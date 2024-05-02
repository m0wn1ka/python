# pip install pywhatkit
import pywhatkit 

# Specify the phone number (with country code) and the message
# phone_number = "+919110565212"
message = "Hello from Python! This is an instant WhatsApp message."
# kit.sendwhatmsg_to_group_instantly("Groip", "Hey All!")
pywhatkit.sendwhatmsg("+919110565212",message, 14, 24)
# Send the message instantly
# kit.sendwhatmsg_instantly(phone_number, message)