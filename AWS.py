"""Getting Started Example for Python 2.7+/3.3+"""
from cgitb import text
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

def textToSpeech(text, fileName, voice="Matthew", ssmlMode=False):
    # Create a client using the credentials and region defined in the [adminuser]
    # section of the AWS credentials file (~/.aws/credentials).
    session = Session(profile_name="default")
    polly = session.client("polly")

    try:
        # Request speech synthesis
        if ssmlMode:
            response = polly.synthesize_speech(Text=text, OutputFormat="mp3",
                                            VoiceId=voice, TextType="ssml")
        else:
            response = polly.synthesize_speech(Text=text, OutputFormat="mp3",
                                            VoiceId=voice)
    except (BotoCoreError, ClientError) as error:
        # The service returned an error, exit gracefully
        print(error)
        sys.exit(-1)

    # Access the audio stream from the response
    if "AudioStream" in response:
        # Note: Closing the stream is important because the service throttles on the
        # number of parallel connections. Here we are using contextlib.closing to
        # ensure the close method of the stream object will be called automatically
        # at the end of the with statement's scope.
            with closing(response["AudioStream"]) as stream:
                output = os.path.join(os.getcwd(), fileName)

                try:
                # Open a file for writing the output as a binary stream
                    with open(output, "wb") as file:
                        file.write(stream.read())
                except IOError as error:
                    # Could not write to file, exit gracefully
                    print(error)
                    sys.exit(-1)

    else:
        # The response didn't contain audio data, exit gracefully
        print("Could not stream audio")
        sys.exit(-1)

# textToSpeech('<speak>Hello this is<break time="300ms"/> World talking to you</speak>', "test.mp3")