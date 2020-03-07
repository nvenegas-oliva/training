
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import argparse
import logging
from google.oauth2 import service_account

logging.getLogger().setLevel(logging.INFO)

CREDENTIALS = service_account.Credentials.from_service_account_file("service.json")

logging.info("Credentials status: {0}".format(CREDENTIALS.valid))


def main(args):
    # model aprams
    params = {
        "learning_rate": args.learning_rate,
        "n_estimators": args.ntrees,
        "subsample": args.subsample,
        "max_depth": args.max_depth
    }

    # cargar la datra
    data = pd.read_gbq("SELECT * FROM `TEMP.WINE_DATASET`",
                       project_id="spike-sandbox",
                       credentials=CREDENTIALS,
                       dialect="standard")

    train, test = train_test_split(data, test_size=0.3)
    training_cols = [col for col in data.columns if col != "quality"]
    target = "quality"

    # entrenar modelo
    model = GradientBoostingRegressor(**params)
    model.fit(train[training_cols], train[target])
    predictions = model.predict(test[training_cols])

    # generar metricas
    mse = mean_squared_error(test[target], predictions)
    mae = mean_absolute_error(test[target], predictions)

    logging.info("MSE: {0}, MAE: {1}".format(mse, mae))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--ntrees', type=int)
    parser.add_argument('--learning_rate', type=float)
    parser.add_argument('--subsample', type=float)
    parser.add_argument('--max_depth', type=int)
    args = parser.parse_args()
    main(args)
