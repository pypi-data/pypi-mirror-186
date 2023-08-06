import os
import sys


try:
	appname = sys.argv[2]
except:
	print('provide a project name')


def create_dir(app):
    project_dir = os.path.join(os.getcwd(), app)
    try:
        os.mkdir(project_dir)
    except FileExistsError:
        print(f"Directory {app} already created.")
        sys.exit()
    file_name = os.path.join(project_dir, 'manage.py')
    create_kalki_file = open(file_name, 'w')
        
    kalki_content = "import sys\ntry:\n\timport settings\nexcept:\n\tpass\ntry:\n\tfrom kalki import kalkiminify\nexcept:\n\tpass\ntry:\n\tfrom kalki import service\nexcept:\n\tpass\ntry:\n\tfrom kalki import create_app\nexcept:\n\tpass\n\ntry:\n\tappname = sys.argv[2]\nexcept:\n\tprint('provide a appname')\n\ndef check_appname():\n\tfor app in settings.APP_NAME:\n\t\tif app == appname:\n\t\t\treturn True\n\ndef startapp():\n\tcreate_app.startapp(appname)\n\ndef compile():\n\tif check_appname():\n\t\tservice.service(appname)\n\telse:\n\t\tprint('Appname do not exists.')\n\t\tprint(\"If the app exists, add the app to APP_NAME in settings.py\")\n\ndef minify():\n\tif check_appname():\n\t\tkalkiminify.kalkiminify(appname)\n\telse:\n\t\tprint('Appname do not exists.')\n\t\tprint(\"If the app exists, add the app to APP_NAME in settings.py\")\n\nif __name__ == '__main__':\n\ttry:\n\t\tglobals()[sys.argv[1]]()\n\texcept IndexError:\n\t\tprint(\"\"\"\n\t\t\tavailable commands-\n\t\t\t\tstartapp\n\t\t\t\tcompile\n\t\t\t\tminify\n\t\t\tUse these commands like-\n\t\t\t\t'python kalki.py startapp' to create working directory\n\t\t\t\t'python kalki.py compile' to create compiled css file\n\t\t\t\t'python kalki.py minify' to create minified css file\n\t\t\t\"\"\")"
    create_kalki_file.write(kalki_content)
    create_kalki_file.close()
    print(
        f"{app} project created successfully.")

def startproject():
    create_dir(appname)



if __name__ == '__main__':
	try:
		globals()[sys.argv[1]]()
	except IndexError:
		print("""
			available commands-
				startproject <project_name>
			Use these commands like-
				'kalki startproject <project_name>' to create working directory
			""")