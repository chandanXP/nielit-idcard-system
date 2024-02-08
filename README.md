##Pythonanywhere.com

 cd /your/project/path
 
 **ZIP project**: zip -r myzipfile vishal

 **Unzip your project**: unzip yourzipfile.zip
 
 **NOT FOUND ERROR***: python3.10 manage.py collectstatic
 
 **STATIC FILES NOT FOUND**: Change the static DIR path from web tab


##Hosting Django project on pythonanywhere.com

1. Go to **pythonanywhere.com** and sign in.

2. authenticate your accounts using an email link (you will not be able to start projects unless you do this).

3. Navigate to the **web** tab in your PythonAnywhere account. 

4. Create a new webapp. 

5. Select **Django** as your framework.

6. Select the latest Python interpreter **(python3.10)**.

7. Set your project a name (it must be the same as your local host project).

8. Your Django project will be created by default. (Of course, this is not your project!)

9. Navigate to the project file tab and click the upload button to upload your project (zip file size 100MB).

10. Now, from the menu, open a console bash terminal and input: **unzip YourProject.zip**

11. open the given link and your project will be running on **yourprojectname.pythonanywhere.com**


##Notes:

1. Go to the web tab and press the reload button (you must reload every time you make significant changes or if you are using a low-end machine).

2. Click the provided link to launch your project.

3. If your project is not working, is crashing, or has an error, you can manually update the file/dir. path in the dashboard for static/media/database/projectpath/wsgi.py files. This is a common task in PythonAnywhere project hosting.

4. If the project fails to work due to any request/response/server type issues, there is a log file for server activity that records all server-related activities. You can locate and resolve the problem here. 

5. The same applies for unknown errors. There is an error log file that records any errors that occur while your project is running. It is also very common to detect errors using these logs.

6. Do not delete or any other file PythonAnywhere created for your Django; you may only delete the default project folder (including manage.py) or files already in your uploaded project.

7. The project gets deleted after three months, so must keep visiting and reloading the project. (save a copy of your project on GitHub or somewhere else you will lose it). Yes! It is also very common to lose a project on PythonAnywhere.)

## Handling Card Generation Errors

If you encounter an error while generating cards with the message "Error: if error occurs while generating cards, please make sure that you have entered date fields of student/employee card in the admin panel," follow these steps to troubleshoot and resolve the issue:

1. **Check Admin Panel Entries:**
   - Ensure that you have entered valid date fields for both student and employee cards in the admin panel of your Django project.

2. **Verify Date Entries:**
   - Double-check the start and end date fields for student and employee cards to ensure they are correctly formatted and have valid values.

3. **Admin Panel Configuration:**
   - Navigate to the admin panel of your Django application.
   - Locate the sections related to student and employee card configurations.
   - Confirm that all required date fields are filled out appropriately.

4. **Debugging:**
   - If the issue persists, inspect the Django application logs for any specific error messages related to card generation.
   - Utilize Django's debugging tools to identify the exact source of the error in your code.

5. **Update and Retry:**
   - If you find any discrepancies in the date entries or configuration, make the necessary updates in the admin panel.
   - Retry the card generation process after ensuring that all required information is accurately entered.


