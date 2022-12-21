# mastodon_timeline_to_rss

Service to transform your personal mastodon timeline into an RSS source that you can feed to an RSS reader.

The project is suited to be run from a pythonanywhere instance, so it uses the django version offered there and doesn't use the latest available one.

To run the project, it needs a `.env` file in the root folder (There's a sample `.env.sample` that you can copy to `.env` and fill the values). This `.env` file needs to define some environmental variables for the program to run:

    SECRET_KEY=xxx # Django secret key. feel free to google about this. I've used https://djecrety.ir/ to generate mine
    MASTODON_HOST=https://xxx.yy # URL of your mastodon host
    MASTODON_BEARER=zzz # Bearer token to access the API for your account. Use this guide to generate one: https://dev.to/bitsrfr/getting-started-with-the-mastodon-api-41jj#find-your-access-token 
    DEBUG=True # or False. Optative variable. If present and True, you'll get additional log lines about what the app is doing
    ALLOWED_HOSTS=127.0.0.1 your_account.eu.pythonanywhere.com # space-separate list of django allowed hosts, feel free to google about this.

In dev mode, start the server with `python manage.py runserver`, the feed should be available in `HOST/mastodon_timeline.rss`

### Important notice re pythonanywhere

By default, pythonanywhere restricts the allowed APIs that can be accessed: https://help.pythonanywhere.com/pages/RequestingWhitelistAdditions/

if you get a `403 Forbidden` with a `Tunnel connection failed` description, follow the procedure in the link to request they add your `MASTODON_HOST` to the whitelist
