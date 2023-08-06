from setuptools import setup, find_packages
import codecs
import os

#change to dict
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)),'README.md'), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.12'
DESCRIPTION = "Big automation package for ADB"

# Setting up
setup(
    name="adbkit",
    version=VERSION,
    license='MIT',
    url = 'https://github.com/hansalemaos/adbkit',
    author="Johannes Fischer",
    author_email="<aulasparticularesdealemaosp@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    #packages=['a_cv2_imshow_thread', 'a_cv2_shape_finder', 'a_cv_imwrite_imread_plus', 'a_pandas_ex_adb_execute_activities', 'a_pandas_ex_adb_settings_to_df', 'a_pandas_ex_adb_to_df', 'a_pandas_ex_csv_plus', 'a_pandas_ex_image_tools', 'a_pandas_ex_logcat2df', 'a_pandas_ex_tesseract_multirow_regex_fuzz', 'adb_grep_search', 'adb_unicode_keyboard', 'androdf', 'flatten_everything', 'getevent_sendevent', 'kthread', 'numpy', 'opencv_python', 'pandas', 'Pillow', 'psutil', 'pyperclip', 'regex', 'sendevent_getevent_keyboard', 'sendevent_touch', 'subprocess_print_and_capture', 'touchtouch'],
    keywords=['adb', 'android', 'automation', 'shell', 'root'],
    classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only', 'Programming Language :: Python :: 3.9', 'Topic :: Scientific/Engineering :: Visualization', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Text Editors :: Text Processing', 'Topic :: Text Processing :: General', 'Topic :: Text Processing :: Indexing', 'Topic :: Text Processing :: Filters', 'Topic :: Utilities'],
    install_requires=['a_cv2_imshow_thread', 'a_cv2_shape_finder', 'a_cv_imwrite_imread_plus', 'a_pandas_ex_adb_execute_activities', 'a_pandas_ex_adb_settings_to_df', 'a_pandas_ex_adb_to_df', 'a_pandas_ex_csv_plus', 'a_pandas_ex_image_tools', 'a_pandas_ex_logcat2df', 'a_pandas_ex_tesseract_multirow_regex_fuzz', 'adb_grep_search', 'adb_unicode_keyboard', 'androdf', 'flatten_everything', 'getevent_sendevent', 'kthread', 'numpy', 'opencv_python', 'pandas', 'Pillow', 'psutil', 'pyperclip', 'regex', 'sendevent_getevent_keyboard', 'sendevent_touch', 'subprocess_print_and_capture', 'touchtouch'],
    include_package_data=True
)
#python setup.py sdist bdist_wheel
#twine upload dist/*