# Change Log

## [0.1.0](https://github.com/code4romania/pyngohub/releases/tag/0.1.0)(2025-02-12)

* Bump the minor version to `0.1.0` since the package has passed the production test
* Bring back compatibility with Python 3.11


## [0.0.10](https://github.com/code4romania/pyngohub/releases/tag/0.0.10)(2025-02-03)

* Fix the cities in the `organization.activity_data`
* Fix the organization_city/_county from the `organization.general_data`


## [0.0.9](https://github.com/code4romania/pyngohub/releases/tag/0.0.9)(2024-10-03)

* Fix the regions of an `organization.activity_data`
* Add `BaseDataClass` to all the dataclasses


## [0.0.8](https://github.com/code4romania/pyngohub/releases/tag/0.0.8)(2024-09-26)

* Normalize the API responses for user profile and organization data
* Implement better error handling for the API
* Add a retry mechanism for the API


## [0.0.7](https://github.com/code4romania/pyngohub/releases/tag/0.0.7)(2024-09-24)

* Return dataclass-based objects from the API


## [0.0.6](https://github.com/code4romania/pyngohub/releases/tag/0.0.6)(2024-09-17)

* Fix the check for a user's access to an application


## [0.0.5](https://github.com/code4romania/pyngohub/releases/tag/0.0.5)(2024-09-17)

* Add user/organization endpoints for getting information
  * add new organization and user endpoints
    * get a user's profile
    * get an NGO user's organization's profile
    * get the applications of an organization's user
    * get the list of apps
    * get organization information
    * get user(s) information
  * checks for users making use of these endpoints
    * check if a user has an application (self and other users)
    * check if an organization has an application
* Improve the management of tests with tox
* Improve the documentation


## [0.0.4](https://github.com/code4romania/pyngohub/releases/tag/0.0.4)(2024-08-21)

* Add code to work with the public endpoints (i.e., `health`, `version`, `file`, `nomenclatures/*`)


## [0.0.3](https://github.com/code4romania/pyngohub/releases/tag/0.0.3)(2024-08-01)

* Create `publish` & `release` workflows
* Add a workflow for running tests & other checks
* Update the README
* Add a `tox` configuration


## [0.0.2](https://github.com/code4romania/pyngohub/releases/tag/0.0.2)(2024-07-31)

* Update the README
* Update the project classifiers


## [0.0.1](https://github.com/code4romania/pyngohub/releases/tag/0.0.1)(2024-07-30)

* Initial code for the package.
