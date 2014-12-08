# flask-not-robot-recaptcha

Google new recaptcha , I am not robot. Flask example.

![](https://raw.githubusercontent.com/eternnoir/flask-not-robot-recaptcha/master/index.png)

## Install requirement package.

```bash
pip install -r requirements.txt
```

## Change keys.

Edit app.py line 7,8 to your api key.

```python
# Change to your site key and secret key.
# Check https://www.google.com/recaptcha/intro/index.html
SITE_KEY = '6LfX2v4SAAAAAE22aaDg*********************'
SECRET_KEY = '6LfX2v4SAAAAAHSlw9*********************'
```

## Run

```python
python app.py
```

