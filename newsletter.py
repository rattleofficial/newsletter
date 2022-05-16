import streamlit as sl
from pyrebase import *
config={
    "apiKey": "AIzaSyCilEt1u-MY3Yz56_fPoGbsysgLoweReYI",
    "authDomain": "newsletter-f9a5f.firebaseapp.com",
    "projectId": "newsletter-f9a5f",
    "databaseURL":"https://newsletter-f9a5f-default-rtdb.firebaseio.com/",
    "storageBucket": "newsletter-f9a5f.appspot.com",
    "messagingSenderId": "793080417319",
    "appId": "1:793080417319:web:4bcc987850a3fd934c5202",
    "measurementId": "G-NNWFG7Z232"
}
firebase=pyrebase.initialize_app(config)
db=firebase.database()
sl.title('Join our newsletter now!')
sl.markdown("Hello join our Rattlefoundation's newsletter to get our updates upto date through your email.Rattlefoundation is a tech provider trusted by 1000+ people around the world.")
inp=sl.text_input('Your name:')
inp2=sl.text_input('Your email:')
if sl.button('Join!'):
    data={inp:""}
    s=inp2.replace('.','')
    data2={s:""}
    db.child("Name").update(data)
    db.child("Email id").update(data2)
    m=sl.header('Thank you for joining our newsletter!')
