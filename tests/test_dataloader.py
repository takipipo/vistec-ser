from vistec_ser.datasets import DataLoader, FeatureLoader
from vistec_ser.utils.config import Config
import sys
import os


def main(argv):
    config_path, csv_path = argv[1], argv[2]
    assert os.path.exists(config_path), f"Config path `{config_path}` does not exists."
    assert os.path.exists(csv_path), f"CSV path `{csv_path}` does not exists."

    config = Config(path=config_path)
    feature_loader = FeatureLoader(config=config.feature_config)
    data_loader = DataLoader(feature_loader=feature_loader, csv_paths=csv_path, augmentations=config.augmentations)
    dataset = data_loader.get_dataset(batch_size=2)
    for x, y in dataset:
        print(x.shape, y)


if __name__ == '__main__':
    main(sys.argv)