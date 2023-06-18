# Fraud Detection - Auckland Capital Bank
The Jupyter notebooks and resulting pipeline and dashboard for this project demonstrate the collection, interrogation and presentation of data relating to credit card transactions. The scenario presented below is fictional and was undertaken for the developer's Data Analytics milestone project as part of [Code Institute's](https://codeinstitute.net/global/) Diploma in Full Stack Software Development.

## Scenario
Scams and other fraudulent activity are a growing problem in New Zealand and may cost the economy as much as $9.8b a year, according to the Series Fraud Office.[^1]

[^1]: https://www.ey.com/en_nz/financial-services/how-can-we-tackle-the-costs-of-scams-in-new-zealand

## Dataset

- The dataset for this study is sourced from [Kaggle](https://www.kaggle.com/datasets/dhanushnarayananr/credit-card-fraud).
- It contains 1 million rows representing individual credit card transactions. The data is licensed under [CC0](https://creativecommons.org/publicdomain/zero/1.0/) and therefore is in the public domain.
- For the purposes of the scenario, outlined above, we might imagine that the data is provided to the study from Auckland Capital Bank.
- The dataset has 8 columns representing information about each transaction. The details are below:

| Variable (type)                        | Meaning                                                                         | Notes & Assumptions                                                                                                                                                                          | Range |
| -------------------------------------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| distance_from_home (float)             | The distance from home where the transaction happened.                          | There is no unit of measurement specified. It is assumed that they are a linear scale (rather than a logarithmic scale, for example) but this is should be consideration in any conclusions. | tbc   |
| distance_from_last_transaction (float) | The distance from the last transaction made on the card.                        | There is no unit of measurement specified. It is assumed that they are a linear scale (rather than a logarithmic scale, for example) but this is should be consideration in any conclusions. | tbc   |
| ratio_to_median_purchase_price (float) | The ratio of the price in this transaction to the median purchase price.        | It is ambiguous as to whether this refers to median price of the whole set or of an assumed user. Intuitively, the latter is assumed,.                                                       | tbc   |
| repeat-retailer (float)                | The retailed appears elsewhere in the dataset                                   | Encoded as a float (1.0 for True, 0.0 for False)                                                                                                                                             | tbc   |
| used_chip (float)                      | The purchaser used their embedded mircochip during this transaction             | Encoded as a float (1.0 for True, 0.0 for False)                                                                                                                                             | tbc   |
| used_pin_number (float)                | The purchaser used their Personal Identification Number during this transaction | Encoded as a float (1.0 for True, 0.0 for False)                                                                                                                                             | tbc   |
| online_order (float)                   | The transaction occurred online                                                 | Encoded as a float (1.0 for True, 0.0 for False)                                                                                                                                             | tbc   |
| fraud(float)                           | The transaction is fraudulent                                                   | Encoded as a float (1.0 for True, 0.0 for False)                                                                                                                                             | tbc   |