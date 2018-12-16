The source code for the grader.

Unfortunately, Google yells at me for sharing the credentials.
So they will have to downloaded from our shared drive, copy the json file
into the directory and it should work.

If any bugs occur, let me know. Will update as soon as possible.


Also, don't forget to download gspread from pip!

pip install gspread


Currently, there are two ways to update grades.

Per individual student:
  This will iterate through a student and the week's assignments. Both student and week are parameters that must be provided. Student is not case sensitive. Week must be an int that is NOT zero indexed. However, it could be if needed.

Batch:
  Iterate through all the students and performs the same operations as the individual grading.
