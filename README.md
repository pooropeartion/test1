# Fair Billing

* we have created the log files for the username and sessions *
* the data comes from the logs files whiile creatoing the username along with start and stop ....
* entries ganerates the timestamps [the HH:MM:SS ] *
* we are displaying the logs data in the file along with username, sessions and total time *

# Getting Started 

1. Python 3.11.4


## Solution
### Approach: ............................

* i have crested three functions  *
1. create_log_file :
   The create log file logic will write the log entries data into the file 
2. calculate_sessions :
   created three empty dictionaries 

   Ignore invalid lines without a valid timestamp, username, and action
   Update earliest start time and latest end time
   Check if it's the start or end of a session

   Calculate the number of sessions and total duration for each user

3. write_summary_to_log :
    we are adding the User_name : Session : Total_Timein to log file after creating the logs.

* I am giving user input as below :

    Enter username: 
    Enter action (Start/End): 
    Do you want to enter another log entry? (y/n): 
    



### code flow

* Once you run the code with python filename.py file path or filename [billing.tx] *
* The log file will genearte along with data entries with calculate_sessions code and store into the specified path.*
* After creating the logs data, and displaying username, sessions and total duration in the file.

## Prerequisite

* Install python latest version into your local machine *
* After Set up the python :
    
    Run the below command in code editor terminal :
    python filename.py filename billing.txt [entire path or only .txt filename]

After the run the above command the below input will display on the terminal:

Enter username: long
Enter action (Start/End): start
Do you want to enter another log entry? (y/n): y 


### How to Run
```sh
git clone ........................................................
....................
```
### Input Example 
```sh
.........................................
```

### Output Example(terminal)
Note : I did this on windows os with VS code editor
```sh 
Enter username: long
Enter action (Start/End): start
Do you want to enter another log entry? (y/n): y 

```


