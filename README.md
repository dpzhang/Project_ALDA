# Project ALDA

CAPP 30122: Computer Science with Applications-2

The University of Chicago | Winter 2017

## About this repository:
This repository contains the final course project for CAPP 30122. 

## About all sub-directories:
* <code>AldaCourse</code>: contains all individual components of Project ALDA 
listed below together with a Django interface.

* <code>CourseCrawler</code>: contains all scripts necessary to scrape course 
informations.

* <code>CourseEvaluation</code>: contains all scripts necessary to scrap 
course evalations.

* <code>NLTK</code>: contains python scripts used to select the top 6 positive
 and negative words from each evaluation comments.

* <code>ScheduleVisualization</code>: contains python scripts and 
template.xlms file used to create all possible combinations of non-conflict 
courses schedules based on user input. 

* <code>Project_Info</code>: contains project description files and 
the presentation slides.

## Required Packages:
* Selenium (v3.3.1)
* Openpyxl (v2.4.5)
* Django (v1.10.6)
* PhantomJS (v2.1.1) 

## How to install all required packages on **Ubuntu** (super eazy):
1. Fire up a terminal, and go to the directory you want to store AldaCourse.

2. In the directory of your choice, run this command to clone the git 
 epository: <br /> 
<code>git clone https://github.com/dpzhang/Project_ALDA.git</code>

3. After cloning the git repo, you will find a new local sub-directory 
called **Project_ALDA**.

4. In the home directory of **Project_ALDA**, type in 
<code>sh alda_install.sh</code>. 
    + After typing in this bash command, you might be asked to input the 
      password of your machine.
    + After inputting your password, Linux would start to install all required
      packages so as to ensure AldaCourse could run successfully and 
      smoothly in your machine.
    + **Friendly Reminder**: you only need to install once, and it might 
      take about 30s to 1min to finish all required installations. 
      (patience is a virtue:sunglasses:)

## How to launch AldaCourse on **Ubuntu**:
1. Go to the home directory of AldaCourse in your machine and type in 
<code>sh alda_prep.sh</code>.
    + If you are a first-time user and just finished installing all packages 
following the tutorial above, you can actually just stay in the same terminal 
window and input the command <code>sh alda_prep.sh</code>.
    + **Notice**: after typing in <code>sh alda_prep.sh</code>, you will find 
the current terminal you are using could no longer input other bash command. 

2. **Open a new terminal in the same directory**, and type in 
<code>sh alda_init.sh</code>. It would automatically launch your default web 
browser and you will see our amazing interface, powered by Django.

## How to use our program:
### I. Schedule Builder
* Once you have successfully see our beautiful interface, the first thing you 
want to do, of course, is to input **3 different** classes you want to take 
in the next quarter here at UChicago!

* After putting in **3 different** courses, click on the "Search" button below. 
It will show you a table of course information, including 
    + Course Control Numbers (CCN) -- you can also click on it to see the 
course description
    + Section numbers 
    + Course Name
    + Undergrad/Grad section 
    + Day/Time
    + Instructor Name(s)
    + Location
    + Lec/SEM 

* **Notice**: you might be seeing a course **of the same section number** occur 
twice in the list. This is because that particular course would have both 
undergraduate and graduate in the same lecture. 

* In the very first column of the course table, you are able to check the empty 
boxes to indicate which courses you would like to take (If you are a greedy 
person, you can also check all boxes that are available). Based on the 
combination of courses you select, AldaCourse can intelligently generate all 
feasible and non-conflicted course schedules that best staisfy your demand.

* After checking the boxes and indicating your course selection, click on the 
"Download Schedules" button below. There would be two possible outcomes:
    1. You will see a message called "Your courses schedules are generated 
and have already been downloaded to your AldaCourse directory". The generated 
course schedules could be found in 
<code>./Project_Alda/AldaCourse/aldacourse/schedule#.xlsx</code>. The output 
course schedule are all in <code>.xlsx</code> spreadsheet format and the number 
of generated spreadsheets will soley depend on the combination of courses you 
select. 
    2. If you see a message like "There's conflict in your course selection. 
We couldn't generate schedule.", it means based on your course selection, there 
is no feasible schedules available. So... think about other course options.

### II. Course Evaluation
* If you want to know the evaluation of the instructor of a particular course 
that you want to take, just simply click on the instructor name in the table.

* In case a class is taught by multiple professors, AldaCourse would bring you 
to a page to select the instructor you are interested in. 

* After checking the box before the name of one instructor, click on 
"Instructor Evaluation" button. You will then see the evaluation
of that insturctor in a **clean**, **consistent**, **organized** and 
**systematic** format.

### III. Open-spot Reminder
* In case a popular class that you want to take is already full and no more 
empty seat available at the time, no worries, AldaCourse is made to resolve 
this issue right for you.

* Check the box of that popular course that is currently full, and input your 
email address in the "Email Address Option" below the table.

* Finally, click the "Get Notification" button. 
    + **Warning**: our interface would generate a "Timeout Exception" warning 
message under poor internet environments. We suggest to shut down the current 
AldaCourse server and re-launch AldaCourse. 

* Congratualations, now you will be one of the first persons 
to receive an email of notification knowing when that popular course will have 
an empty seat.
    + **Disclaimer**: this AldaCourse function does not guarantee you will be 
able to get the course you want. Some other factors, such as how often you 
check your emails or how fast you can type and click on your laptop, are 
extraordinarily crucial. So... Good luck!

## Contributors
**Alice Mee Seon Chung** [Alicechung](https://github.com/Alicechung)

**Luxi Luke Han** [magicahan](https://github.com/magicahan)

**Dongping Gabriel Zhang** [dpzhang](https://github.com/dpzhang)

**Ningyin Ariel Xu** [sixisxu](https://github.com/sixisxu)

We would like to express our sincere gratitude to **Dr. Matthew Wachs** and 
**Dr. Amitabh Chaudhary** for your teaching, guidance, and support throughout 
the quarter.
