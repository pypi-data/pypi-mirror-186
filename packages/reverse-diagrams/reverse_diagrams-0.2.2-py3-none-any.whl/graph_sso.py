
from diagrams import Diagram, Cluster

from diagrams.aws.management import Organizations, OrganizationsAccount, OrganizationsOrganizationalUnit
from diagrams.aws.general import Users, User

with Diagram("SSO-State", show=False, direction="TB"):
    gg = Users("Group")
    uu= User("User")

    with Cluster('Groups'):

        gg_0= Users("AWSSecurityAudit\nors")

        gg_1= Users("AWSServiceCatalo\ngAdmins")

        gg_2= Users("AWSAuditAccountA\ndmins")

        with Cluster("SecOps_Adms"):

                gg_3= [User("w.alejovl+secops\n-labs@gmail.com"),]

        gg_4= Users("AWSLogArchiveAdm\nins")

        gg_5= Users("AWSSecurityAudit\nPowerUsers")

        with Cluster("AWSControlTowerAdmins"):

                gg_6= [User("velez94@protonma\nil.com"),]

        with Cluster("AWSAccountFactory"):

                gg_7= [User("velez94@protonma\nil.com"),]

        gg_8= Users("AWSLogArchiveVie\nwers")

        with Cluster("DevSecOps_Admins"):

                gg_9= [User("DevSecOpsAdm"),]
