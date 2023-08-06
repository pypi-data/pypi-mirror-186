import os
import warnings
warnings.filterwarnings("ignore")

def init_settings_directory():
    """Create the user settings directory.
    """
    user_settings_dir = os.path.join(os.path.expanduser("~"),".pygenplot")
    if not os.path.exists(user_settings_dir):
        try:
            os.makedirs(user_settings_dir)
        except:
            print("Can not create user settings directory")

init_settings_directory()
