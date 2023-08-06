# OASIS4 Data Interface

This package is intended to facilitate access to OASIS4 data from DJANGO for modules that require it.

The system does not expose any type of service, as if it exposes some of the models, with their handling classes, of the OASIS4 base for its access.
## Models
* Classification: This model is required for *OasisProduct* model.
* Geographiclocation: This model is required for *Client* model.
* Client: This model represents the Client table on Oasis4 database.
* Discount: This model represents the Discount table on Oasis4 database.
* OasisProduct: This model represents the Product table on Oasis4 database.

