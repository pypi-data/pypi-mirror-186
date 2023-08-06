# Package to download files to the Robin Radar API

# new version notifcation -> force user to update

# check version of package API and compare to version of package installed on user's machine

# if version of package API is greater than version of package installed on user's machine, then force user to update

# if version of package API is less than or equal to version of package installed on user's machine, then continue

## How to run the upload script?

If you have a pip package that you have installed, you should be able to run the main script from the command line using the python -m command.

The basic format for running a script from a pip package using the python -m command is as follows:

python -m <package_name>.<module_name>

Where package_name is the name of the package and module_name is the name of the module that contains the script you want to run.

For example, if the package you installed is called "mypackage" and the script you want to run is called "main.py", you would run the following command:

python -m mypackage.main

The above command assume that the package has been properly installed and the python path include this package path.

Another way to do this would be to add the package to your environment variable and run the main script directly.

export PYTHONPATH=$PYTHONPATH:/path/to/mypackage

python /path/to/mypackage/main.py

It's important to note that the exact command you'll need to run will depend on the specific package and its file structure, so you may need to adjust the command accordingly.

If you are not sure about the package_name or module_name you can use pip to check it by typing in the shell:

pip show <package_name>

It will show you the package details including the path where it is located.
