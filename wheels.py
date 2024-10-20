import os
import subprocess

# File paths
files = [
    "/Users/azlanirshad/test3/logs/azlan/develop/conf/dev/ais_tod_1/impl.conf",
    "/Users/azlanirshad/test3/logs/azlan/develop/conf/dev/ais_tod_2/impl.conf",
    "/Users/azlanirshad/test3/logs/azlan/develop/conf/dev/ais_tod_1/imf.conf",
    "/Users/azlanirshad/test3/logs/azlan/develop/conf/dev/ais_tod_2/imf.conf"
]

# Sed command
sed_command = (
    "sed -i '' "
    "'/^IMEL_RBProfilesDbConnector_Command_timeout/s/=.*/=/; "
    "/^IMEL_RBProfilesDoConnector_Connection_timeout/s/=.*/=/; "
    "/^IMEL_RBProfilesDoConnector_Default_database/s/=.*/=/; "
    "/^IMEL_RBProfilesDoConnector_username/s/=.*/=/; "
    "/^IMEL_RBProfilesDoConnector_password/s/=.*/=/; "
    "/^IMEL_RBProfilesDoConnector_DSN/s/=.*/=/; "
    "/^IMEL_RBProfilesDoConnector_TNS_server/s/=.*/=/; "
    "/^FF_PROFILES_dBConnector_servername/s/=.*/=/g'"
)

# Execute the sed command for each file
for file in files:
    subprocess.run(f"{sed_command} {file}", shell=True)
    print(f"Values after '=' have been modified for {file}")

# Send email notification
email_subject = "Subject: Executed!"
email_body = "File has been modified"
email_command = f'echo -e "{email_subject}\n\n{email_body}" | msmtp azlanirshad@gmail.com'
os.system(email_command)

print("Email sent!")