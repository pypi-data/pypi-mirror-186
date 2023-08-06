
from diagrams import Diagram, Cluster, Edge

from diagrams.aws.management import Organizations, OrganizationsAccount, OrganizationsOrganizationalUnit
from diagrams.aws.general import Users, User
from diagrams.aws.security import IAMPermissions
with Diagram("IAM Identity Center", show=False, direction="LR"):
    gg = Users("Group")
    uu = User("User")
    pp= IAMPermissions("PermissionsSet")
    ou = OrganizationsOrganizationalUnit("PermissionsAssignments")

    with Cluster('Account: Log archive'):

        with Cluster('Group: AWSSecurityAuditPowerUsers'):
