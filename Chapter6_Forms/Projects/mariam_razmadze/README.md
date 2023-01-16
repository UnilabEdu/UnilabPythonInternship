Basically the same as my previous project "team-app", but html formss are converted into flask-wtf.

Status: COMPLETE. WARNING: Looks better on large screen, small/medium size screen views are ok for now, but not great.

PLEASE Test it out and let me know if you find any bugs or if you have any suggestions for improvement. Thanks.

Overview: To start using the app, first you should register and login. Your Status will be intern initially, but admin can change the status to Senior or Junior. They have distinctive colors - senior is dark blue, junior is light blue and intern is bright pink and these colors follow the users throughout the entire application so that you can always easily tell which user has which status. After you log in, you can start asking or/and answering questions.

Each questions you ask has to have a specific addressee, which you select from the user list.

Intern can only ask questions, but not answer them.

Junior can ask questions and also answer questions.

Seniors only answer questions.

So depending on your status, your navbar is different, meaning you won't see the "answer" link if you're an intern or you won't see the "ask question" link if you're a senior. And you won't see either, if you're not logged in.

If you are a junior or senior, you can go to "answer" link from your navbar, where you will see all the questions that other users asked you (if nobody asked you anything, this page will be empty). Once you answer the question, it will disappear from that page and will appear on the home page, where all the answered questions are displayed chronologically. If you want to test this out but you are too lazy to create accounts, then just log in as one of the precreated accounts. For example, enter "Michael Scott" in username and "asdf" in password and you will be logged in.

Only admin user can see the "user setup" link in her/his navbar, where she/he can change the status of all the users. You can test this too, if you log in as admin. For that, enter "admin" in username and "asdf" in password. After that You can change status of all users, which dynamically changes their color. You should try it, it's fun 😄

All the answered questions are saved chronologically. If you click on the question directly, it will take you to the page where you can see its answer too. Everyone can see the answered questions, which means that before you ask questions, you should see the home page and if your question is already there, you no longer have to ask it, which saves time for seniors and juniors (which is one of the main purposes of the app).

Built with Python and Flask.

This project was done for UNILAB Python Accelleration Program.

Deployed on PythonAnywhere.

DEPLOYMENT: [View deployment](http://wtfteamapp.pythonanywhere.com/)
