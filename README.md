# breweries-case

This data engineering project consumes data from an API, transforms it, and persists the data in a Data Lake following the Medallion Architecture with three layers:

Bronze: Raw data extracted from the API.
Silver: Transformed data, stored in Parquet format.
Gold: Aggregated data (count of breweries by type and state) stored in CSV format.

Used Astro with Airflow for orchestration. Docker for containerization. 

Some points that I would like to improve in the project:

- Create terraform to pass infra-as-code to build better all the componenets
- Create a configuration with GCP using dataform or DBT
- Monitoring 
