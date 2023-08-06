from datasets import Value

GANTRY_FOLDER = ".dataset_metadata"
DATASET_MANIFEST_FILE = f"{GANTRY_FOLDER}/.gantry_manifest.jsonl"  # manifest file
DATASET_HEAD_FILE = f"{GANTRY_FOLDER}/HEAD"  # current head commit info
STASH_FOLDER = f"{GANTRY_FOLDER}/.dataset_stash"
DATASET_STASH_FILE = f"{STASH_FOLDER}/.stash.json"
HF_FOLDER = f"{GANTRY_FOLDER}/huggingface"
TABULAR_MANIFESTS = "tabular_manifests"
DATASET_CONFIG_FILE = "dataset_config.yaml"
DATASET_FEATURES_KEY = "features"
DATASET_FEEDBACK_KEY = "labels"
BACKUP_SUFFIX = "_backup"
NEW_SUFFIX = "_new"

FILE_NAME = "file_name"
NEW_FILES = "new_files"
MODIFIED_FILES = "modified_files"
DELETED_FILES = "deleted_files"
UNCHANGED_FILES = "unchanged_files"
SHA256 = "sha256"
URL = "url"


METADATA_S3_FILE_VERSION = "metadata_s3_file_version"


FILE_PATH = "file_path"
OBJ_KEY = "obj_key"
VERSION_ID = "version_id"

# TODO: add support to cast image/video/audio from string to the file
GANTRY_2_HF_DTYPE = {
    "Float": Value(dtype="float64", id=None),
    "Text": Value(dtype="string", id=None),
    "Integer": Value(dtype="int64", id=None),
    "Boolean": Value(dtype="bool", id=None),
    "Categorical": Value(dtype="string", id=None),
    "UUID": Value(dtype="string", id=None),
    "Datetime": Value(dtype="timestamp[ns, tz=UTC]", id=None),
    "Json": dict(),
    "Image": Value(dtype="string", id=None),
    "Audio": Value(dtype="string", id=None),
    "Video": Value(dtype="string", id=None),
    "File": Value(dtype="string", id=None),
    "Array<String>": Value(dtype="string", id=None),  # this is temporary we need to do casting
    "Array<Float>": Value(dtype="string", id=None),
    "Array<Integer>": Value(dtype="string", id=None),
    "Array<Boolean>": Value(dtype="string", id=None),
    "Array<UUID>": Value(dtype="string", id=None),
    # "Array<String>": Sequence(feature=Value(dtype="string", id=None), length=-1, id=None),
    # "Array<Float>": Sequence(feature=Value(dtype="float64", id=None), length=-1, id=None),
    # "Array<Integer>": Sequence(feature=Value(dtype="int64", id=None), length=-1, id=None),
    # "Array<Boolean>": Sequence(feature=Value(dtype="bool", id=None), length=-1, id=None),
    # "Array<UUID>": Sequence(feature=Value(dtype="string", id=None), length=-1, id=None),
    "Unknown": Value(dtype="null", id=None),
}

EMPTY_STR_SHA256 = "47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU="
