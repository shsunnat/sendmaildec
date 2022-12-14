# Email sender decorator

This is decator for using sending email 

- Decorator is simple to use 
- Easy following

## Features

- Gmail setup 
- Sending simple emails
- Sending emails to multiple recipients
- Sending files
- Sending HTML formatted emails 

## Gmail setup

 You must have two-factor authentication enabled on your Gmail account. If not, you should. We’ll have to generate a password 
 that Python script will use to log into your account and send emails.
It’s a straightforward step to do. Just click on this [URL](https://myaccount.google.com/apppasswords), and you’ll be presented with a screen like this:

![image-1](https://user-images.githubusercontent.com/93898481/205278062-37ebd202-cec7-4c13-b2bc-392c4cb95b70.png)

You won’t see the “Python Email” row, however. Just click on the Select app dropdown, and then on Other (Custom name). Enter a name (arbitrary), and click on the Generate button.

That’s it! A modal window like this will pop up:


![2](https://user-images.githubusercontent.com/93898481/205279194-80171727-9217-4619-8adf-baf7d3db3540.jpg)

Just make to save the password somewhere safe.

## Sending simple emails

```sh
@sendemail('sender_email','email_password', 'email_receiver','Main Subject', 'This is test')
def plus(a,b):
  ...
```

## Sending emails to multiple recipients

```sh
@sendemail('sender_email','email_password', ['email_receiver_1', 'email_receiver_1', ...],'Main Subject', 'This is test')
def plus(a,b):
  ...
```
## Sending files

```sh
@sendemail('sender_email','email_password', ['email_receiver_1', 'email_receiver_1', ...],'Main Subject', 'This is test', file='book.pdf')
def plus(a,b):
  ...
```

![3](https://user-images.githubusercontent.com/93898481/205282692-11b8f827-224e-4de1-9df1-31bd97479251.png)

## Sending HTML formatted emails

```sh
html = """ 
<!DOCTYPE html>
<html>
    <body>
        <div style="background-color:red;padding:10px 20px; width: 410px;">
            <h2>This Is Message For You</h2>
        </div>
        <div style="padding:20px 0px">
            <div style="height: 500px;width:400px">
                <img src="https://avatars.mds.yandex.net/i?id=7acca5dc31999ab261c86d4ba53b47fa9d558c37-3922549-images-thumbs&n=13" style="height: 300px;">
                <div style="text-align:center;">
                    <h3>My first article</h3>
                    <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. A ducimus deleniti nemo quibusdam iste sint!</p>
                    <a href="#">Read more</a>
                </div>
            </div>
        </div>
    </body>
</html>
"""
@sendemail('sender_email','email_password', 'email_receiver','Main Subject', html, is_html=True)
def plus(a,b):
  ...
```

![4](https://user-images.githubusercontent.com/93898481/205287512-6e25c6b3-4170-404e-a591-f8a7cc59397a.png)

## Installation

```sh
git clone https://github.com/shsunnat/sendmaildec.git
```
