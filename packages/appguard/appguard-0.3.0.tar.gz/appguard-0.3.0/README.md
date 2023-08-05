<a href="https://www.extrinsec.com">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://cdn.extrinsec.com/images/logos/logo-exsec-dark.png#gh-dark-mod-only">
    <source media="(prefers-color-scheme: light)" srcset="https://cdn.extrinsec.com/images/logos/logo-exsec-light.png#gh-light-mode-only">
    <img alt="Learn more about how Extrinsec secures and protects your Python applications"/>
  </picture>
</a>

Real time serverless security platform for [Python](https://www.python.org).

```Python
# set required environment variable ES_POLICY_GROUP_NAME as provided or configured in your app, e.g.
# os.environ["ES_POLICY_GROUP_NAME"] = "observeAll.ability";

# load the appguard module
import 'appguard'
```

## Installation

```console
python3 -m pip install appguard
```

It is recommended that you register an account on https://app.extrinsec.com/ and configure your own policy rules for the best protection.

## Features

- Quick and simple setup
- **Observe**, **Deny** or **Grant** any combination of the following
  - outbound network data
  - read/write tmp or app directories
  - create/spawn child processes
- Option to terminate process for policy violations
- Ability to whitelist domains
- Fast & Reliable, no wrapping or monkey-patching of your code
- Easy collaboration between dev and ops teams with role based access
- View all events centrally in the web application

## Docs & Community

- [Website](https://www.extrinsec.com/appguard)
- [App](https://app.extrinsec.com/)
- [FAQ](https://www.extrinsec.com/faq)
- Community Support

## License

© Copyright 2023 Extrinsec LLC, all rights reserved.
