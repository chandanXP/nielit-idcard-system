#Pythonanywhere.com

 cd /your/project/path
 
 ZIP project from pythonanywhere.com: zip -r myzipfile vishal

 Unzip your project: unzip yourzipfile.zip
 
 NOT FOUND ERROR: python3.10 manage.py collectstatic
 
 STATIC FILES NOT FOUND : Change the static DIR path from web tab


#Hosting Django project on pythonanywhere.com

1. Go to pythonanywhere.com and sign in.

2. authenticate your accounts using an email link (you will not be able to start projects unless you do this).

3. Navigate to the "web" tab in your PythonAnywhere account. 

4. Create a new webapp. 

5. Select "Django" as your framework.

6. Select the latest Python interpreter.

7. Set your project a name (it must be the same as your local host project).

8. Your Django project will be created by default. (Of course, this is not your project!)

9. Navigate to the project file tab and click the upload button to upload your project (zip file size 100MB).

10. Now, from the menu, open a console bash terminal and input > unzip YourProject.zip

11. open the given link and your project will be running on “yourprojectname.pythonanywhere.com”


#Notes:

1. Go to the web tab and press the reload button (you must reload every time you make significant changes or if you are using a low-end machine).

2. Click the provided link to launch your project.

3. If your project is not working, is crashing, or has an error, you can manually update the file/dir. path in the dashboard for static/media/database/projectpath/wsgi.py files. This is a common task in PythonAnywhere project hosting.

4. If the project fails to work due to any request/response/server type issues, there is a log file for server activity that records all server-related activities. You can locate and resolve the problem here. 

5. The same applies for unknown errors. There is an error log file that records any errors that occur while your project is running. It is also very common to detect errors using these logs.

6. Do not delete or any other file PythonAnywhere created for your Django; you may only delete the default project folder (including manage.py) or files already in your uploaded project.

7. The project gets deleted after three months, so must keep visiting and reloading the project. (save a copy of your project on GitHub or somewhere else you will lose it). Yes! It is also very common to lose a project on PythonAnywhere.)
