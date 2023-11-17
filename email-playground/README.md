# Email Sender
### simple program that sends email to specified Email Address from specified Email Address with specific content, this can be used to build mailing list
---
### Initial setup
- create a `.env` file refer to `.env.example` file
- to get app password 
    - enable 2FA on your Google Account (which will act like sender)
    - open [this link](https://myaccount.google.com/apppasswords) and create an app password 

---

#### how to run

```sh
python email_sender.py
```
```sh
python email_sender2.py
```

---
make sure the virtual environment on the root of the repo is activated and `python-dotenv` is installed