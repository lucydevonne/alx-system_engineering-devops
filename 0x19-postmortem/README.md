![alt text]https://github.com/lucydevonne/alx-system_engineering-devops/blob/master/download.jpg?raw=true


Postmortem Report: Internal System Error Causing Incorrect File Extension
May 14, 2023

By the IT Support Team

On May 13, 2023, we experienced an issue in our IT system that resulted in incorrect file extensions. We understand that this issue has affected our users, and we apologize for any inconvenience this may have caused. This report aims to provide details about the nature of the issue, the root cause, our response, and the actions we are taking to prevent similar issues in the future.


Issue Summary
On May 14th, 2023, between 2:00 PM and 3:00 PM (GMT), users accessing a website running on Apache were unable to access the site and received a 500 error message. The impact rate was estimated to be 100% for all users attempting to access the site during the outage.


Timeline (all times Pacific Time)
10:30 AM: System update starts
11:00 AM: Users report incorrect file extensions
11:05 AM: IT support team alerted
11:10 AM: Investigation begins
11:30 AM: Root cause identified
11:45 AM: Fix implemented
12:00 PM: All affected files restored


Root Cause
After investigating the issue, it was determined that the root cause was a misconfigured file extension in one of the PHP files used by the website. Specifically, the file extension was written as "phpp" instead of "php".


Resolution and Recovery
At 11:10 AM PT, the IT support team was alerted about the issue and immediately started investigating. At 11:30 AM, the root cause of the issue was identified, and a fix was implemented. The fix involved correcting the script to check the file type before updating the extension. The IT support team ensured that all affected files were restored by 12:00 PM.


Corrective and Preventative Measures
To address the underlying cause of the issue and to prevent similar issues in the future, the following actions will be taken:

1. Review and revise the script to ensure that it only updates the extensions of the intended file types.
2. Implement an additional check to validate that the file type matches before updating the extension.
3. Create a staging environment for system updates to test scripts before deploying them to the production environment.
4. Conduct a comprehensive review of all scripts and codes to ensure their functionality and security.
5. Develop a process to notify users of any system issues and updates that may affect their files.


Conclusion
We understand the impact that this issue has had on our users, and we apologize for any inconvenience this may have caused. We have taken steps to fix the issue and prevent similar issues in the future. We will continue to improve our systems and processes to ensure the highest level of service to our users. 

Sincerely,
The IT Support Team
