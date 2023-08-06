from pathlib import Path

import pandas as pd
from config.core import DATASET_DIR, config
from pipeline import formation_energy_pipe
from processing.data_manager import load_dataset, save_pipeline
from sklearn.model_selection import train_test_split


def run_training() -> None:
    """Train the model."""

    # read training data
    data = load_dataset(file_name=config.app_config.dft_calc_train)

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.model_config.input_features],
        data[config.model_config.target],
        test_size=config.model_config.test_size,
        random_state=config.model_config.random_state,
    )

    test_set = pd.concat([X_test, y_test], axis=1)
    test_set.to_csv(Path(f"{DATASET_DIR}/{config.app_config.test_split}"))

    # fit model
    formation_energy_pipe.fit(X_train, y_train)

    # persist trained model
    save_pipeline(pipeline_to_persist=formation_energy_pipe)


if __name__ == "__main__":
    run_training()
