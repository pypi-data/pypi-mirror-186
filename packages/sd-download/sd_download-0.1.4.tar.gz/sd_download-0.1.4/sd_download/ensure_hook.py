import os

script_location = '/opt/robin/scripts/sd/pre_hook.py'

def ensure_hook():

    hook_file = "/etc/apt/apt.conf.d/100-robinsw"
    contents = 'APT::Update::Pre-Invoke  {"/bin/python script_location";};'

    contents = contents.replace('script_location', script_location)

    if os.path.isfile(hook_file):
        print("Hook file exists, checking contents")
        # Ensure the contents of the file match the contents of the variable
        with open(hook_file, "r") as stream:
            if stream.read() == contents:
                print("Hook file contents match")
                return True
            else:
                print("Hook file contents do not match, overwriting.")
                # Copy the current file to a backup
                os.rename(hook_file, hook_file + ".bak")
                with open(hook_file, "w") as stream:
                    stream.write(contents)
                    return True
    else:
        print("Hook file does not exist, creating.")
        with open(hook_file, "w") as stream:
            stream.write(contents)
            return True