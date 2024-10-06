from telemanom.detector import Detector
import argparse

from telemanom.esn_modeling import ESNModel
from telemanom.modeling import LSTMModel

parser = argparse.ArgumentParser(description='Parse path to anomaly labels if provided.')
parser.add_argument('-l', '--labels_path',
                    default='labeled_anomalies.csv', required=False)
parser.add_argument('-mt', '--model_type_label',
                    default='lstm', required=False)
args = parser.parse_args()

if __name__ == '__main__':
    detector = Detector(labels_path=args.labels_path)
    model_type = ESNModel if args.model_type_label == 'esn' else LSTMModel
    detector.run(model_type=model_type)