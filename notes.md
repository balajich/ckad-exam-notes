# JVM Heap memory usage alerts
- It is important to monitor the JVM heap memory usage of application to ensure that it is not running out of memory.
- Long-running applications may run out of memory if the heap memory usage is not monitored.
- HRIS applications run in Tomcat and  Weblogic servers
- At this juncture, appdynamics creates alerts when JVM memory usage is greater than 80% for 5 minutes
- If these alerts coming Task server (Weblogic) these can be ignored. Because Task server runs long-running tasks, and it is normal for it to use more memory.
- If these alerts are coming from other servers, then it is important to investigate the root cause of the memory usage.
- If task server heap memory usage doesn't get back to normal after an  hour. Please let Devops team know about it . There should be a bad report running in the server.
 
# Using SQLDeveloper to connect to Oracle Database using TLS
- As part of the security requirements, the Oracle database is configured to use TLS. TCP port 1521 is disabled and the database is accessible only through TCPS port 2484.