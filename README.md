# Data Engineering Project: API Data Pipeline with Medallion Architecture

This data engineering project is designed to build an end-to-end data pipeline that consumes data from an API, transforms it, and stores it in a Data Lake using the Medallion Architecture. This approach organizes data into three layers to support efficient processing and analytics.

## Project Overview

### Medallion Architecture Layers
**Bronze Layer**: Raw data extracted directly from the API, stored in its original format for future reference.

**Silver Layer**: Transformed data stored in Parquet format, making it ready for more efficient querying and processing.

**Gold Layer**: Aggregated data (such as brewery count by type and state), saved in CSV format and optimized for analytical queries.

### Key Technologies

**Apache Airflow**: Used for orchestration, ensuring reliable scheduling and execution of the ETL pipeline.
**Docker**: Provides containerization for seamless project setup, ensuring consistency across environments.

## Project Structure

- **DAGs**: Contains the Airflow DAG files, which define the ETL workflow steps and schedules.
- **Scripts**: Transformation and aggregation scripts to process the data from raw to refined states.
- **Docker Compose**: Set up for running Airflow and other dependencies in containers.
- **Configuration**: Settings for environment variables, Airflow configuration, and API connection details.

## Future Improvements

- **Infrastructure as Code with Terraform**: Automate and streamline the setup of cloud infrastructure, making deployment more scalable and maintainable.
- **GCP Integration with Dataform or DBT**: Implement Dataform or DBT for managing data transformations, especially if using Google Cloud Platform for hosting the data lake.
- **Monitoring**: Add monitoring tools and dashboards to track data quality, pipeline performance, and alerts for failure handling.
