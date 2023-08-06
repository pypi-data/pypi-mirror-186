
from diagrams import Diagram, Cluster

from diagrams.aws.management import Organizations, OrganizationsAccount, OrganizationsOrganizationalUnit

with Diagram("Organizations-State", show=False, direction="TB"):
    ou = OrganizationsOrganizationalUnit("OU")
    oa = OrganizationsAccount("Account")

    with Cluster('Organizations'):

        oo = Organizations('o-9tlhkjyoii\n029921763173\nr-w3ow')

        ou_Sandbox= OrganizationsOrganizationalUnit("ou-w3ow-1sumtdvp\nSandbox")

        oo>> ou_Sandbox

        ou_Security= OrganizationsOrganizationalUnit("ou-w3ow-oqvta8tc\nSecurity")

        oo>> ou_Security

        ou_Workloads= OrganizationsOrganizationalUnit("ou-w3ow-1lpmyfug\nWorkloads")

        oo>> ou_Workloads

        ou_Dev= OrganizationsOrganizationalUnit("ou-w3ow-k24p2opx\nDev")

        oo>> ou_Dev

        ou_DevSecOps= OrganizationsOrganizationalUnit("ou-w3ow-b334bby6\nDevSecOps")

        oo>> ou_DevSecOps

        ou_Core= OrganizationsOrganizationalUnit("ou-w3ow-93hiq3zr\nCore")

        oo>> ou_Core

        ou_PolicyStaging= OrganizationsOrganizationalUnit("ou-w3ow-18verpsm\nPolicy Staging")

        oo>> ou_PolicyStaging

        ou_Suspended= OrganizationsOrganizationalUnit("ou-w3ow-7vunsbkd\nSuspended")

        oo>> ou_Suspended

        ou_Shared= OrganizationsOrganizationalUnit("ou-w3ow-w7dzhzcz\nShared")

        oo>> ou_Shared

        ou_Infrastructure= OrganizationsOrganizationalUnit("ou-w3ow-9q06w8rz\nInfrastructure")

        oo>> ou_Infrastructure

        ou_BULab= OrganizationsOrganizationalUnit("ou-w3ow-qa633svy\nBU-Lab")

        ou_Workloads>> ou_BULab

        ou_Prod= OrganizationsOrganizationalUnit("ou-w3ow-4sdr4ejy\nProd")

        ou_BULab>> ou_Prod

        ou_SDLC= OrganizationsOrganizationalUnit("ou-w3ow-vop5vccd\nSDLC")

        ou_BULab>> ou_SDLC

        ou_Core>> OrganizationsAccount("884478634998\nLog archive")

        ou_Security>> OrganizationsAccount("835863553119\nSecOps")

        ou_Prod>> OrganizationsAccount("582441254763\nProd")

        ou_Core>> OrganizationsAccount("895882538541\nSecurityTooling")

        ou_DevSecOps>> OrganizationsAccount("105171185823\nDevSecOps")

        ou_Infrastructure>> OrganizationsAccount("994261317734\nOps")

        ou_Infrastructure>> OrganizationsAccount("155794986228\nSharedServices")

        oo >> OrganizationsAccount("029921763173\nLabVel")

        ou_Security>> OrganizationsAccount("837696987585\nOrganizationMana\nger")

        ou_SDLC>> OrganizationsAccount("571340586587\nDev")
