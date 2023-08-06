# CertfrTracker

This package is under GNU License project.

## Links 

- [pypi](https://pypi.org/project/CertfrTracker/)
- [gitlab](https://gitlab.com/arthur_muraro/python-certfr/-/tree/pypi-package/)
- [CertfrTracker-CLI gitlab](https://gitlab.com/arthur_muraro/python-certfr)

## inventory model (the data you'll provide to CertfrTracker) :

To use the CertfrTracker package you will need 3 differents array containing for each : "the name of your components", "their versions", "a starting date for the comparing system to begin with".

example :

- technos = [ Drupal, Apache, PHP]

- versions = [ 1.3.4, 2.4.49-Alpha, 8.1.8]

- dates = [ "JJ-MM-AAAA", "JJ-MM-AAAA", "JJ-MM-AAAA" ]

All the Arrays must have the same length.

## output model (the data that will be sent back to you by CertfrTracker) :

Here is how the data is organised when CertfrTracker send back it's outptut :

It's an array of "Plain Object" containing all this variables for each indexes :

    alert_id        # id of the Alert                               | String | CVE-2022-1234, CERTFR-2022-ALE-004, CERTFR-2022-AVI-004
    techno          # Name of the Techno                            | String | ex: Apache, Postgresql, Openjdk
    version         # Version of the Techno                         | String | ex: 1.2.3, 1.2, 1.2.3-beta
    status          # Nature of Alert                               | String | Open or Applicable
    score           # CVSS or NVD Score                             | Float  | between 1 and 10
    publish_date    # Publish Date                                  | String | ex: "2020-06-21
    update_date     # Update Date                                   | String | ex: "2020-06-21
    description     # Alert Description                             | String
    source          # url of the alert                              | string
    details         # external that could provide more informations | string

## How to use CertfrTracker Package ?

first you'll need to install the package :

```python
pip install CertfrTracker
```

then, to use this package :

```python
# import
from CertfrTracker import Router

# initiate the class
certfr_tracker = Router.Router()
# you can also specify the path to the database by doing this :
certfr_tracker = Router.Router(db_file="my_file.db")

# update the database (AVIS and ALERTS)
certfr_tracker.update_database()
# only update ALERTS
certfr_tracker.update_database("NextAlert")
# only update AVIS
certfr_tracker.get_certfr_data("NextAvis")

# comparing alerts with complete inventory 
technos = [ "Drupal", "Apache", "PHP"]
versions = [ "1.3.4", "2.4.49-Alpha", "8.1.8"]
_dates = [ "01-01-2014", "01-01-2014", "01-01-2014" ]
reports = certfr_tracker.compare_inventory_with_alerts(technos=technos, versions=versions, dates=_dates)

# comparings alerts with one technology
reports = []
techno = "Drupal"
version = "1.3.4"
_date = "01-01-2014"
reports += certfr_tracker.compare_one_techno_with_alerts(techno=techno, version=version, _date=_date)

# destroy the class instanciation
del certfr_tracker
```

## packaging

update the toml to the new version and then :

```bash
git add pyproject.toml README.md
git commit -m "pushing next release"
git push
git rm dist/*
python3 -m build
git add dist/*
git commit -m "pushing last build"
git push
python3 -m twine upload dist/*
pip install CertfrTracker
```