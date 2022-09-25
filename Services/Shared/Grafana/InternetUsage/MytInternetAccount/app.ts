import { InfluxDB } from 'influx';
import { Axios } from 'axios';
import { DateTime } from 'luxon';
import { writeFileSync } from 'fs';

interface LoginResponse {
  token: string;
}

interface BankDetails {
  response: {
    convertedBalance: string;
    balance: string;
    validitydate: string;
    creditLimit: string;
    rawaccumulatedusage: string;
    bankName: string;
    category: string;
    categoryName: string;
    isUnlimitedBank: string;
    accumulatedusage: string;
  }[];
  errorMessage: string;
  errorCode: string;
}

const now = DateTime.now().setLocale('en-GB');

// Fill those up
const mytLoginDetails = { username: 'username', password: 'password' };
const influxdbDetails = {
  database: 'database name',
  host: 'hostname or ip address',
  port: 8086,
  username: 'username if applicable, or set this as undefined, just like the password on the next line',
  password: undefined,
};

const app = async () => {
  const axiosInstance = new Axios({
    withCredentials: true,
    headers: { 'Content-Type': 'application/json' },
    transformResponse: (data) => {
      try {
        return JSON.parse(data);
      } catch (e) {
        return undefined;
      }
    },
    transformRequest: (data) => {
      try {
        return JSON.stringify(data);
      } catch (e) {
        return undefined;
      }
    },
  });

  const { data: response } = await axiosInstance.post<LoginResponse>(
    'https://internetaccount.myt.mu/portal-api/auth/login',
    { email: mytLoginDetails.username, password: mytLoginDetails.password }
  );

  if (!response) {
    return console.log(`${now.toISO}: Error logging in`);
  }

  const { data: bankDetails } = await axiosInstance.post<BankDetails>(
    `https://internetaccount.myt.mu/rest-services/selfcare/subscriber/${mytLoginDetails.username}/bankInstanceList`,
    {
      identifierName: 'USERNAI',
      identifierValue: mytLoginDetails.username,
    },
    {
      headers: {
        Authorization: `Bearer ${response.token}`,
      },
    }
  );

  if (!bankDetails || bankDetails.errorCode !== '0') {
    return console.log(`${now.toISO}: Error getting usage history`);
  }

  const dataRemaining = bankDetails.response.find(
    (res) => res.bankName === 'LimitedData'
  )?.balance;

  if (!dataRemaining) {
    return console.log(`${now.toISO}: Error getting data balance left`);
  }

  const influx = new InfluxDB({
    database: influxdbDetails.database,
    host: influxdbDetails.host,
    port: influxdbDetails.port,
    username: influxdbDetails.username,
    password: influxdbDetails.password,
  });

  await influx.writePoints([
    {
      measurement: 'internet_usage_myt',
      tags: {
        monthyear: `${now.month.toLocaleString(undefined, {
          minimumIntegerDigits: 2,
        })}/${now.year}`,
      },
      fields: {
        // in bytes
        data_left: Number(dataRemaining),
      },
    },
  ]);

  const remaining = (Number(dataRemaining) / 1024 / 1024);

  const output = `${now.toISO()}: bandwidth remaining ${remaining.toFixed(0)} MB / ${(remaining / 1024).toFixed(2)} GB, ${((remaining / 4194304) * 100).toFixed(2)}% left`;

  writeFileSync('last_run.log', `${output}\n`, {
    flag: 'as+',
    encoding: 'utf-8'
  })

  console.log(output);
};

app().catch((e) =>
  console.log(`${now.toISO}: Oops, something went wrong: ${e}`)
);
