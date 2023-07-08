# Fraud Detection - Auckland Capital Bank
The Jupyter notebooks and resulting pipeline and dashboard for this project demonstrate the collection, interrogation and presentation of data relating to credit card transactions. The scenario presented below is fictional and was undertaken for the developer's Data Analytics milestone project as part of [Code Institute's](https://codeinstitute.net/global/) Diploma in Full Stack Software Development.

## Scenario
Scams and other fraudulent activity are a growing problem in New Zealand and may cost the economy as much as $9.8b a year, according to the [Serious Fraud Office.]( https://www.ey.com/en_nz/financial-services/how-can-we-tackle-the-costs-of-scams-in-new-zealand)

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

## Business Requirements

Auckland Capital Bank want to know more about the key markers for potentially fraudulent activity in order to minimise their financial loss due to fraudulent activity. They also would like to safeguard their customers from this loss and would like to ensure they are giving customers the optimal advice about fraud prevention.

1. ACB would like to understand the patterns in the transaction data to better understand the most relevant variables correlated to a fraudulent transaction.
2. ACB would like to be able to 'flag' potentially fraudulent transactions at Point of Sale for further investigation

## Project Hypotheses & Validation

The Senior Management team of ACB have put forward two hypotheses for testing during this study:

- The further away from home that a transaction occurs, the more likely it is to be fraudulent.
  - A correlation study will be undertaken to assess this.
- Online transactions are more likely to be fraudulent than in-person transactions.
  - A correlation study will be undertaken to asses this.

## Project Rationale

## Make this more user story focussed.

- **Business Requirement 1:** Data Visualisation and Correlation study
  - This study will interrogate the transaction data, described above.
  - It will conduct a correlation study (Pearson and Spearman) to understand better how the variables are correlated to Fraud.
  - It will plot the main variables against Fraud to visualise insights.
- **Business Requirement 2:** Classification Pipeline
  - ACB want to predict if a transaction is fraudulent. This will require a binary classifier.

  ## ML Business Case

### Scope and Objective

A ML model will be used to predict if a transaction is fraudulent. It will use the historical transaction data, as described above. The target variable ('fraud') is categorical and contains 2-classes. It is a supervised, 2-class, single-label classification model output: 0 (not fraudulent), 1 (fraudulent).

The objective of the project is to allow ACB to safeguard customers and minimise financial loss due to fraud.

### Measuring Success

ACB have set clear metrics of such success, which are:

- **90% Recall for Fraud.** This will protect the vast majority of customers at risk of fraud.
- **90% Precision for Fraud.** ACB does not want to unnecessarily contact or take preventative action (such as freezing cards) for customers who are making genuine transactions. This has been shown to reduce customer satisfaction and trust in the bank.

### Outputs

The model output is defined as a flag, indicating if a transaction and _the associated probability of fraud!?!!??!!!?!?._
*For this proof of concept, individual transactions will be entered into the dashboard. In future these will be able to be done in bulk*

### Heuristics

Currently ACB does not employ any approach to predicting fraudulent transactions.

### Describe training data...