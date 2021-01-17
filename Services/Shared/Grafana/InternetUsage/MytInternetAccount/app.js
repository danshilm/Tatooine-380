const puppeteerr = require('puppeteer');
const Influx = require('influx');

const url = 'https://internetaccount.myt.mu/alepowsrc/L7ExSNbPC4sb6TPJDblCAkN0baRJxw3qqt9ErkZgoetbexguZOJ1K13kJjowRDi9zus9pCmpMedELy99QFKjgA/L7E59/JDb97/goebc';
const internetAccountUsername = 'myt-internet-account-username';
const internetAccountPassword = 'myt-internet-account-password';
const usernameInput = '#id2';
const passwordInput = '.loginarea > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > input:nth-child(1)';
const signinButton = '#id5';
const volumeLeftLabel = '#id22 > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(6) > td:nth-child(2) > div > font > span > label';
const signoutButton = '#ida';
const now = new Date();
const influx = new Influx.InfluxDB({
	database: 'database',
	host: 'localhost',
	port: 8086,
	username: 'username',
	password: 'password'
});

(async () => {
	// Open browser and navigate to website
	// Set headless to false to see it in action
	const browser = await puppeteerr.launch({ headless: true });
	const page = await browser.newPage();
	await page.goto(url);

	// Login
	await page.type(usernameInput, internetAccountUsername);
	await page.type(passwordInput, internetAccountPassword);
	await page.click(signinButton);

	// Wait for content to be dynamically loaded, then grab the value
	await page.waitForSelector('#ContentBody');
	const label = await page.$(volumeLeftLabel);
	const labelText = await (await label.getProperty('textContent')).jsonValue();
	// in MB
	const amountLeft = Math.round(parseInt(labelText.split(/ /)[0]));

	// Sign out after doing the deed and close the browser
	await page.click(signoutButton);
	await browser.close();

	// Send to InfluxDB
	influx.writePoints([
		{
			measurement: 'internet_usage_myt',
			tags: {
				month: now.getMonth() + 1
			},
			fields: {
				data_left: amountLeft * 1024 // Convert MB into KB
			}
		}
	]).catch(error => {
		console.log('Error saving data to InfluxDB database');
	});

	console.log(`${now.toISOString()} : volume left: ${amountLeft} MB`);
})();
