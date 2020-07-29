# gam-sso

Contains mapping YAML per domain plus python package to update the G-Suite users.

1. Install GAM (https://github.com/jay0lee/GAM) and follow instructions to authenticate to your domain
2. Install `gammit` python package from this repository `pip install -e ./python-pkg/gammit`
3. Configure your users in `python-pkg/gammit/gammit/mapping/{DOMAIN.com}.yml`
4. Update users `gam update -d {DOMAIN.com}`
