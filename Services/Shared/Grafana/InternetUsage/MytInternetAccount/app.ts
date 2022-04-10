import { InfluxDB } from 'influx';
import { Axios } from 'axios';
import { DateTime } from 'luxon';

interface LoginResponse {
  token: string;
}

interface UsageHistory {
  response: {
    SubscriptionIdentifier: string;
    ALEPOEDRID: string;
    EndTime: string;
    TotalUsage: string;
    EventType: string;
    UnitCharges: string;
    subscriberId: string;
    CallDuration: string;
    CustomField1: string;
    SubscriptionType: string;
    CustomField2: string;
    SessionDuration: string;
    CustomField3: string;
    CustomField4: string;
    PARENTSESSIONID: string;
    CustomField6: string;
    BankDeducted: string;
    startTime: string;
    ChargeLabel: string;
  }[];
  errorMessage: string;
  errorCode: string;
}

const now = DateTime.now().setLocale('en-GB');

// Fill those up
const mytLoginDetails = { username: '37393261-1', password: 'W6U3H' };
const influxdbDetails = {
  database: 'manual',
  host: '192.168.100.3',
  port: 8086,
  username: undefined,
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

  const { data: usageHistory } = await axiosInstance.post<UsageHistory>(
    'https://internetaccount.myt.mu/rest-services/selfcare/generic/getMediationEDR',
    {
      subscriberId: mytLoginDetails.username,
      startIndex: 0,
      MaxCount: 35,
      toDate: now.toLocaleString({
        day: 'numeric',
        month: 'short',
        year: 'numeric',
      }),
      fromDate: now.minus({ months: 1 }).endOf('month').toLocaleString({
        day: 'numeric',
        month: 'short',
        year: 'numeric',
      }),
    },
    {
      headers: {
        Authorization: `Bearer ${response.token}`,
      },
    }
  );

  if (!usageHistory) {
    return console.log(`${now.toISO}: Error getting usage history`);
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
        data_used: parseInt(usageHistory.response[0].TotalUsage),
      },
    },
  ]);

  console.log(
    `${now.toISO()}: bandwidth used ${(
      parseInt(usageHistory.response[0].TotalUsage) /
      1024 /
      1024
    ).toFixed(0)} MB`
  );
};

app().catch((e) =>
  console.log(`${now.toISO}: Oops, something went wrong: ${e}`)
);
