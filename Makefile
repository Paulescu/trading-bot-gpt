.PHONY: init debug_technical_indicators run_technical_indicators backfill_technical_indicators

### Install ###

# install Poetry and Python dependencies
init:
	curl -sSL https://install.python-poetry.org | python3 -
	poetry install


### Technical Indicators Pipeline ###

# run the feature-pipeline locally and print out the results on the console
debug_technical_indicators:
	poetry run python -m bytewax.run "src.dataflow:get_dataflow(execution_mode='DEBUG')"
	
# run the feature-pipeline and send the feature to the feature store
run_technical_indicators:
	poetry run python -m bytewax.run "src.technical_indicators_pipeline:get_dataflow()"

# backfills the feature group using historical data
backfill_technical_indicators:
	poetry run python src/backfill_technical_indicators.py --from_day $(from_day) --product_id XBT/USD

