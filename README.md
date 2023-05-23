# Anonymizing Data in Ephemeral Environments

This is a demo application for ephemeral development environments, such as testing, staging, and sandbox setups. It can be used for reference or as a starting point to build vendor specific architectures that work with Privacy Dynamics. The application is designed to be as simple and basic as possible.

## A reference architecture
The reference architecture we propose is designed specifically for ephemeral development environments. These environments often contain subsets of production data, making it essential to safeguard Personally Identifiable Information (PII) and other sensitive details.

### Key components:

1. Source data. This component represents the data that needs to be anonymized. It could be a database, file storage, or any other data repository. In this example, the source data is a PostgreSQL container seeded from a synthetically generated JSON document.
2. Anonymization engine. The anonymization engine is the core component responsible for processing and transforming data to remove sensitive information. Privacy Dynamics serves as the anonymization engine in this example.
3. Anonymized data. An anonymized copy of the source data that is used for development and testing purposes while protecting individual privacy.

The application contains two services, a front-end and back-end, both written in Python. The back-end contains a fake dataset of users to represent a production database.

For the demonstration, two instances of the app should be started. One instance to represent a production application and the second instance to represent a development or preview environment. Privacy Dynamics connects to the first instance, anonymizes data in memory, and writes the anonymized copy to the second instance.

![](docs/Basic%20Anonymizing%20Data%20for%20Dev%20and%20Test%20Evironments.jpg)

## Leveraging Privacy Dynamics
The demonstration relies on the [Privacy Dynamics Software-as-a-Service (SaaS)](https://www.privacydynamics.io) platform to anonymize the dataset. In order for Privacy Dynamics to work, it must be able to connect to both the source and destination databases. In most cases, networking adjustments must be made to make the databases accessible by Privacy Dynamics.

![](docs/Anonymizing%20Data%20for%20Dev%20and%20Test%20Evironments.jpg)

Once connectivity to the databases is established, a base environment can be used to store an anonymized copy of production data, refreshed on an hourly, daily, or weekly schedule. Database snapshots are used to copy and replicate the anonymized data to _n_ number of remote environments.

## Getting started
You can run a single instance of the application locally. All you need to get started is [Docker](https://www.docker.com/) installed on your local machine.

1. Start the application with `docker compose -up --build`. This will seed the PostgreSQL database with data from the JSON file.
2. Navigate to `http://localhost:5000` in your browser.
