# Text to Email

A barely useful project but hey ho.

I have this running on a cronjob so I can have alerts about emails regardless of my current mobile internet connectivity.

In the email-helper.py file you will see that in this example I am just filtering for emails that have ebay in the subject as the person who I made this for was using it for eBay.


#### Instructions

You will need to have created a Twilio account for this.

.sample_env

Use the below .sample_env template and save it as .env

```

EMAIL=
PASSWORD=

DB_PASS=

ACCOUNT_SID=
AUTH_TOKEN=

MY_TWILIO_NUMBER=
MY_NUMBER=

```

You will need to have a mysql instance running.

The table you will need to create is very simple. See the db.sql file to create.

Once all that is done, simply run python text.py
