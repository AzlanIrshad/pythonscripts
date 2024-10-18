import subprocess

files = [
    "/Users/azlanirshad/test3/logs/azlan/develop/conf/dev/ais_tod_1/impl.conf",
    "/Users/azlanirshad/test3/logs/azlan/develop/conf/dev/ais_tod_1/imf.conf",
    "/Users/azlanirshad/test3/logs/azlan/develop/conf/dev/ais_tod_1/impl.conf",
    "/Users/azlanirshad/test3/logs/azlan/develop/conf/dev/ais_tod_2/imf.conf",
]

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

for i in files:
    subprocess.run(f" {sed_command} {i}", shell=True)
    print(f"Values after = are deleted! from {i}")
