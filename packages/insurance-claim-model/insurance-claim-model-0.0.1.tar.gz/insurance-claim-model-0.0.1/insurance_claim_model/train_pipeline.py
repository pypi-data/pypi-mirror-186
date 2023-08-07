import numpy as np
from processing.data_manager import load_dataset, save_pipeline
from sklearn.model_selection import train_test_split

from insurance_claim_model.config.core import config
from insurance_claim_model.pipeline import predict_pipe


def run_training() -> None:
    data = load_dataset(file_name=config.app_config.training_data_file)
    X_train, X_test, y_train, y_test = train_test_split(
        data.drop([config.model_config.target], axis=1),
        data[config.model_config.target],
        test_size=config.model_config.test_size,
        random_state=config.model_config.random_state,
    )

    y_train = np.log(y_train)
    predict_pipe.fit(X_train, y_train)

    save_pipeline(pipeline=predict_pipe)


if __name__ == "__main__":

    run_training()
