# **MEETY Version 2.0**


##### ***Meety version 2.0*** is a social media site designed to perform like similar upstream social media sites for example Facebook, Instagram etc.

#### For the visual representaion click the [video](https://youtu.be/VCTOlDk5BRM)
---


## **Distinctiveness and Complexity:**

* ### Distinctiveness
    ##### Despite being a social network project Meety version 2.0 is way more distinct from Meety version 1.0. Where Meety version 1.0 is an one app project, Meety has ***six*** different app with better functionality. It has more features like ***Notification*** panel, ***Real-time Chatting*** option, and ***Story*** sharing features. There is an option like ***Hash Tag*** by which it can show all posts from different users with the same tag. The ***Direct Message*** option provides the user to chat from both party simultaniously like other chat apps. The ***Notification*** has different notifiers for different actions. Unlike Meety version 1.0., the ***Story*** has its own session which will end after a certain time. There is a feature ***Change Password*** which allows user to change their password. In the profile there are two different options like posts where user can see their own post and saved where they can see the bookmarked post that they saved from others. There is an option called ***Explore*** where users can find other users and hash tags. There is a feature in post where user can add caption and hash tag for their posts. Unlike Meety version 1.0, the post will only be shown to the user if the user follows that user which have the post. There is different media folder for different user.

* ### Complexity
    ##### ***Meety version 2.0*** is complex enough than other Meety version 1.0 in many aspects. It has six different apps designed to perform better both is development and creating future upgrades. The ***Notification*** has different notifiers for example, if a user follow some user the notification panel will say exactly that user is being followed. Similarly, if some user reacts in any post it will notify only about that and if someone comments it will show that user has commented. For different actions it will show different notifications. In ***Direct Message*** the user can chat from both end at the same time. To make it work, Meety version 2.0 uses ***Celery*** that is a class that can be created out of any callable. It performs dual roles in that it defines both what happens when a task is called (sends a message), and what happens when a worker receives that message. Any user can search any user by typing their name in search to start chat for the first time and after that it will stay in inbox. The ***Story*** is complex enough too. It has its own session after which it will be deleted. The password changing feature has ability to identify if the previous password is same as the new password or not and retyping of a password is same as the newly typed password or not. If it is not it will prompt the user what is wrong there. The hash tag functions have the ability to show all posts under the same tag. The ***Post*** is not just can show the post but also the caption and tags with it will be visible. The template of the project is located in the project file so that all app can connect and for that there is a template call method in the other apps. The whole site is mobile responsive has more than one models. The Post is now can not only take pictures as input but also can take videos. Profile can have different urls which enables user to connect their other social media or any sites in their profile.

* ### Contents
    * #### Comment
        ##### In this file there is a model for storing comments and display with the proper view function. To collect the comments there is a form. To handle everything from an admin, there is an admin file.

    * #### Direct Message
        ##### Here, there is a model for messages to store with the UUID which is processed with views.py. The url to connect with template and show on webpage via HTML. The admin panel can handle its components.

    * #### Notification
        ##### The notification has its model to store different notifications and can show it properly with views. It has it's own url so that it can be connected with HTML. It has admin control right.

    * #### Post
        ##### Post has it's model to store all the posts with caption and hash tags. It can have both images and videos and store inside it. The posts can be streamed properly with its view file. To collect the input properly is has a form. It has its url to connect with HTML and has admin rights.

    * #### Profile
        ##### Profile has its model to store different data. It can store other urls. It can store the user's posts that they created once and saved files. To store data properly it has form. All the data can be processed theough views. It has url to connect with HTML. It can be controlled by the admin.

    * #### Story
        ##### Story has a model which can store data for limited amount of time. After a certain time it will be deleted from the model. To collect data it has forms. Moreover, to show data properly it has views. To control the time of disappearance it has tasks file. It can be controlled by admin and it has url to connect with HTML.

    * #### Meety_
        ##### This is the main project file of this project. It contains template where all the HTML files are located. The template has two folders one is for registration and other is for Direct Message. It has static file in which there is CSS, JavaScript and default images like logo of the Meety. It has settings.py which controls the entire project and url to connect all the apps centrally with the templates. There is a file called celery.py which implements celery functionalities to perform smooth direct messages from both end.

    * #### Media
        ##### The media contains all users media files and saves in a different folders.

* ### How to run
    ##### To run the project you need to install all the requirements. To install all the requirements you can open the terminal and write the following code.
    ```
    pip install -r requirements.txt
    ```
    Then you need to migrate the project. To migrate run the codes.
    ```
    pyhton manage.py makemigrations
    ```
    ```
    python manage.py migrate
    ```
    After that you need to run the server. To run the server:
    ```
    python manage.py runserver
    ```
    After that, go to the url and in the url bar type:
    ```
    localURL_number/user/login
    ```
    You will be prompted the login page where you can login and if have no account you can create an account.

* ### Other info
    ##### In the video presentation the site was in light theme for better visualization. However, the main project is designed with the dark theme. Therefore, after running the project it will start with the dark theme.
---