from pathlib import Path

from Utils.Helper import get_project_root

DEAP_ELECTRODES = ["Fp1", "AF3", "F3", "F7", "FC5", "FC1", "C3", "T7", "CP5", "CP1", "P3", "P7", "PO3", "O1", "Oz",
                   "Pz", "Fp2", "AF4", "Fz", "F4", "F8", "FC6", "FC2", "Cz", "C4", "T8", "CP6", "CP2", "P4", "P8",
                   "PO4", "O2"]

FREQUENCIES = ["Theta", "Alpha", "LowerBeta", "UpperBeta", "Gamma"]

ROOT_PATH = get_project_root()
RAW_DATA_PATH = Path(ROOT_PATH, "Data", "RAW_DEAP_DATASET")
PREPROCESSED_DATA_PATH = Path(ROOT_PATH, "Data", "PREPROCESSED_DEAP_DATA")
FINAL_DATASET_PATH = Path(ROOT_PATH, "Data", "FINAL_DEAP_DATASET")
SAVED_MODEL_GRAPH_PATH = Path(ROOT_PATH, "Data", "SAVED_MODEL_GRAPH")
SAVE_TRAINED_MODEL_PATH = Path(ROOT_PATH, "Data", "SAVED_TRAINED_MODEL")
