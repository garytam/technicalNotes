from flask import Flask, send_from_directory, request
import os
from twilio.twiml.voice_response import  VoiceResponse, Gather

app = Flask(__name__)

XML_DIR_PATH = "/Users/garytam/git_gary/twilio_xml/test_case_1"


# ******************************** #
#   answering incoming call        #
# ******************************** #
@app.route('/answer', methods=['POST', 'GET'])
def answer():
    print("answering....")
    return send_from_directory(
        os.path.abspath(XML_DIR_PATH), "answer.xml")


# ******************************** #
#   making outbound call           #
# ******************************** #
@app.route('/make_call', methods=['POST', 'GET'])
def make_call():
    print("*" * 80)
    print("making call ....")
    return send_from_directory(
        os.path.abspath(XML_DIR_PATH), "calling_level_1.xml")


# ******************************** #
#   response to Gather             #
# ******************************** #
@app.route('/process_gather', methods=['POST', 'GET'])
def process_gather():
    print("into process_gather")

    # Start our TwiML response
    resp = VoiceResponse()

    # If Twilio's request to our app included already gathered digits,
    # process them
    if 'Digits' in request.values:
        # Get which digit the caller chose
        choice = request.values['Digits']

        print("first level choice -->", choice)

        # <Say> a different message depending on the caller's choice
        if choice == '1':
            return send_from_directory(
                os.path.abspath(XML_DIR_PATH), "calling_level_2_1.xml")
        elif choice == '2':
            return send_from_directory(
                os.path.abspath(XML_DIR_PATH), "calling_level_2_2.xml")
        elif choice == '3':
            resp.say('Will transfer to you the next available nurse, please wait')
            print('transfer call to next nurse')
            return str(resp)
        else:
            # If the caller didn't choose 1 or 2, apologize and ask them again
            resp.say("Sorry, I don't understand that choice.")

    # If the user didn't choose 1 or 2 (or anything), send them back to /voice
    # resp.redirect('/voice')
    print("You goofed")
    resp.say("you goof")
    return str(resp)


@app.route('/process_gather_level_2', methods=['POST', 'GET'])
def process_gather_level_2():
    print("into process_gather_level_2")

    # Start our TwiML response
    resp = VoiceResponse()

    # If Twilio's request to our app included already gathered digits,
    # process them
    if 'Digits' in request.values:
        # Get which digit the caller chose
        choice = request.values['Digits']

        print("support choice -->", choice)

        # <Say> a different message depending on the caller's choice
        if choice == '1':
            resp.say('Tomorrow will be a better day')
            return str(resp)
        elif choice == '2':
            resp.say('time wait for no one')
            return str(resp)
        elif choice =='3':
            resp.say('Sorry to hear that, rest in peace')
            return str(resp)
        else:
            # If the caller didn't choose 1 or 2, apologize and ask them again
            resp.say("Sorry, I don't understand that choice.")

    # If the user didn't choose 1 or 2 (or anything), send them back to /voice
    # resp.redirect('/voice')
    resp.say("you goof")
    return str(resp)

if __name__ == '__main__':
    app.run(port=5000)
