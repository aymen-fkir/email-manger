import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pandas as pd
import pandasai
import os
from pandasai.llm import OpenAI
import emojis


class Manager:
    def connect(self)-> dict:
        SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
                creds = flow.run_local_server(port=3000)
            with open("token.json", "w") as token:
                token.write(creds.to_json())
        return creds
    
    def getEmails(self)->[int,str or pd.DataFrame]: 
        creds = self.connect()
        try:
            service = build("gmail", "v1", credentials=creds)
            messagesId = service.users().messages().list(userId="me",q="in:inbox is:unread category:primary").execute()
            Message = {"From": [] ,"Subject": [], "snippet": []}

            for msg_id in messagesId["messages"]:
                
                message = service.users().messages().get(userId="me", id=msg_id["id"]).execute()
                Message["snippet"].append(emojis.decode(message["snippet"]))
                for name in message["payload"]["headers"]:
                    if name["name"]=="From":
                        Message["From"].append(emojis.decode(name["value"]))
                    elif name["name"] == "Subject":
                        Message["Subject"].append(emojis.decode(name["value"]))
                        

            emails_df = pd.DataFrame(Message)
            emails_df.to_csv("Emails.csv")
            return [200,emails_df]
        
        except HttpError:
            return [400,f"error {HttpError}"]
        
    def filterEmail(self)-> [KeyError,pd.DataFrame]:
        code,df = self.getEmails()
        if code == 200:
            api_key = os.environ.get("openai")
            llm = OpenAI(api_token=api_key)
            agent = pandasai.Agent([df],config={"llm":llm})
            responce = agent.chat(query="""filter these email rows and keep only the important email that speaks about [work,Linkden opportunities,deeplearnig ai,family,education],
                                  PS : the words between ': : ' are emojies""",output_type=pd.DataFrame)
            return [None,responce]
        else:
            return [df,None]







