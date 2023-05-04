# Anonymizing Data in Ephemeral Environments

This is a demo application for ephemeral environments. It can be used as a template to anonymize production data for remote, development, and preview environments or it can be used as a starting point to build vendor specific architectures that work with Privacy Dynamics. The application is designed to be as simple and basic as possible.

## A reference architecture
The application can be used as a reference architecture to anonymize production data for ephemeral environments. The application contains two services, a front-end and back-end, both written in Python. The back-end contains a fake dataset of users to represent a production database.

For the demonstration, two instances of the app should be started in ephemeral environments. One instance to represent a production application and the second instance to represent a development environment.

## Leveraging Privacy Dynamics
The demonstration relies on the Privacy Dynamics Software-as-a-Service (SaaS) platform to anonymize that dataset. In order for Privacy Dynamics to work, it must be able to connect to both the source database and the destination database. In most cases, networking adjustments must be made to make the databases accessible by Privacy Dynamics.