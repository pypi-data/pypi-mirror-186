
from diagrams import Diagram, Cluster

from diagrams.aws.management import Organizations, OrganizationsAccount, OrganizationsOrganizationalUnit
from diagrams.aws.general import Users, User

with Diagram("SSO-State", show=False, direction="TB"):
    gg = Users("Group")
    uu= User("User")
