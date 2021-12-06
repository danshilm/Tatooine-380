The official documentation for MonitoRSS is [here](https://docs.monitorss.xyz/).

Prerequites to use MonitoRSS:
1. Create an application on Discord's [Developer Portal](https://discord.com/developers/applications) so you can login using Discord using that application.
    
2. Click on "Bot" in the left panel, then "Add Bot". Set an icon and a username for the bot, save. Then copy the bot's token and set that as the `MONITORSS_BOT_TOKEN` variable in the [`.env` file](../.env).

3. Click on "OAuth2". Copy the Client ID and the Client Secret, set that as the `MONITORSS_BOT_CLIENTID` and `MONITORSS_BOT_CLIENTSECRET` variables respectively in the [`.env` file](../.env).

4. In the "Redirects" section, click on "Add Redirect" and enter the full URL to your MonitoRSS publicly accessible instance followed by `/authorize`. An example would be something like `https://monitorss.domain.com/authorize`.

5. Click on "URL Generator" under the "OAuth2" menu in the left panel, select the `bot` scope, then tick the `Send Messages` permission.
    
	Copy the generated URL below that and open it in a new tab to invite the bot you just created to your server.

6. Run `docker-compose up -d` in the [Monitoring](../) directory.
