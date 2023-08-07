# forecast_ensemble

forecast_ensemble combines multiple models into a single forecast and returns a combined package of models, their
evaluated results including a composite score

## Usage

The forecast is run using `main.py` with the following options

## Request Requirements

The required input format is a JSON with the following fields:

Required:

- `data_filepath`: filepath of the time series data to run the ensemble on
- `target_column`: name of the input column
- `aggregate_operation`: string operation to apply to target_column to create the time series
- `output_directory`: directory to return the result JSON to
