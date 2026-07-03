import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path, override=True)

assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))

os.environ.setdefault("WRAPPER_STAGE_IN", os.path.join(assets_dir, "stagein.yaml"))
os.environ.setdefault(
    "WRAPPER_STAGE_IN_FILE", os.path.join(assets_dir, "stagein-file.yaml")
)
os.environ.setdefault("WRAPPER_STAGE_OUT", os.path.join(assets_dir, "stageout.yaml"))
