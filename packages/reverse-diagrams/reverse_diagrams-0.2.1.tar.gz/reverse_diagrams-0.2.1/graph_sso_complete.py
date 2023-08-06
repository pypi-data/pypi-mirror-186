
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

                gg_AWSSecurityAuditPowerUsers=Users("AWSSecurityAudit\nPowerUsers")
                gg_AWSSecurityAuditPowerUsers \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSPowerUserAcce\nss")
                mm_AWSSecurityAuditPowerUsers=[] 
                gg_AWSSecurityAuditPowerUsers \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSSecurityAuditPowerUsers 


        with Cluster('Group: AWSControlTowerAdmins'):

                gg_AWSControlTowerAdmins=Users("AWSControlTowerA\ndmins")
                gg_AWSControlTowerAdmins \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSAdministrator\nAccess")
                mm_AWSControlTowerAdmins=[User("velez94@protonma\nil.com"),] 
                gg_AWSControlTowerAdmins \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSControlTowerAdmins 


        with Cluster('Group: AWSLogArchiveAdmins'):

                gg_AWSLogArchiveAdmins=Users("AWSLogArchiveAdm\nins")
                gg_AWSLogArchiveAdmins \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSAdministrator\nAccess")
                mm_AWSLogArchiveAdmins=[] 
                gg_AWSLogArchiveAdmins \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSLogArchiveAdmins 


        with Cluster('Group: AWSSecurityAuditors'):

                gg_AWSSecurityAuditors=Users("AWSSecurityAudit\nors")
                gg_AWSSecurityAuditors \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSReadOnlyAccess")
                mm_AWSSecurityAuditors=[] 
                gg_AWSSecurityAuditors \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSSecurityAuditors 


        with Cluster('Group: AWSLogArchiveViewers'):

                gg_AWSLogArchiveViewers=Users("AWSLogArchiveVie\nwers")
                gg_AWSLogArchiveViewers \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSReadOnlyAccess")
                mm_AWSLogArchiveViewers=[] 
                gg_AWSLogArchiveViewers \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSLogArchiveViewers 


    with Cluster('Account: SecOps'):

        with Cluster('Group: AWSSecurityAuditPowerUsers'):

                gg_AWSSecurityAuditPowerUsers=Users("AWSSecurityAudit\nPowerUsers")
                gg_AWSSecurityAuditPowerUsers \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSPowerUserAcce\nss")
                mm_AWSSecurityAuditPowerUsers=[] 
                gg_AWSSecurityAuditPowerUsers \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSSecurityAuditPowerUsers 


        with Cluster('User: w.alejovl+secops-labs@gmail.com'):

                uu_walejovlsecopslabsgmailcom=User("w.alejovl+secops\n-labs@gmail.com")
                uu_walejovlsecopslabsgmailcom \
                        - Edge(color="brown", style="dotted") \
                        - IAMPermissions("AWSAdministrator\nAccess")

        with Cluster('Group: AWSSecurityAuditors'):

                gg_AWSSecurityAuditors=Users("AWSSecurityAudit\nors")
                gg_AWSSecurityAuditors \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSReadOnlyAccess")
                mm_AWSSecurityAuditors=[] 
                gg_AWSSecurityAuditors \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSSecurityAuditors 


        with Cluster('Group: AWSControlTowerAdmins'):

                gg_AWSControlTowerAdmins=Users("AWSControlTowerA\ndmins")
                gg_AWSControlTowerAdmins \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSOrganizations\nFullAccess")
                mm_AWSControlTowerAdmins=[User("velez94@protonma\nil.com"),] 
                gg_AWSControlTowerAdmins \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSControlTowerAdmins 


    with Cluster('Account: Prod'):

        with Cluster('Group: AWSSecurityAuditPowerUsers'):

                gg_AWSSecurityAuditPowerUsers=Users("AWSSecurityAudit\nPowerUsers")
                gg_AWSSecurityAuditPowerUsers \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSPowerUserAcce\nss")
                mm_AWSSecurityAuditPowerUsers=[] 
                gg_AWSSecurityAuditPowerUsers \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSSecurityAuditPowerUsers 


        with Cluster('Group: DevSecOps_Admins'):

                gg_DevSecOps_Admins=Users("DevSecOps_Admins")
                gg_DevSecOps_Admins \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSAdministrator\nAccess")
                mm_DevSecOps_Admins=[User("DevSecOpsAdm"),] 
                gg_DevSecOps_Admins \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_DevSecOps_Admins 


        with Cluster('User: w.alejovl+prod-labs@gmail.com'):

                uu_walejovlprodlabsgmailcom=User("w.alejovl+prod-l\nabs@gmail.com")
                uu_walejovlprodlabsgmailcom \
                        - Edge(color="brown", style="dotted") \
                        - IAMPermissions("AWSAdministrator\nAccess")

        with Cluster('Group: AWSSecurityAuditors'):

                gg_AWSSecurityAuditors=Users("AWSSecurityAudit\nors")
                gg_AWSSecurityAuditors \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSReadOnlyAccess")
                mm_AWSSecurityAuditors=[] 
                gg_AWSSecurityAuditors \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSSecurityAuditors 


        with Cluster('Group: AWSControlTowerAdmins'):

                gg_AWSControlTowerAdmins=Users("AWSControlTowerA\ndmins")
                gg_AWSControlTowerAdmins \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSOrganizations\nFullAccess")
                mm_AWSControlTowerAdmins=[User("velez94@protonma\nil.com"),] 
                gg_AWSControlTowerAdmins \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSControlTowerAdmins 


    with Cluster('Account: SecurityTooling'):

        with Cluster('Group: AWSSecurityAuditPowerUsers'):

                gg_AWSSecurityAuditPowerUsers=Users("AWSSecurityAudit\nPowerUsers")
                gg_AWSSecurityAuditPowerUsers \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSPowerUserAcce\nss")
                mm_AWSSecurityAuditPowerUsers=[] 
                gg_AWSSecurityAuditPowerUsers \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSSecurityAuditPowerUsers 


        with Cluster('Group: SecOps_Adms'):

                gg_SecOps_Adms=Users("SecOps_Adms")
                gg_SecOps_Adms \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("LabvelSecOpsAdms")
                mm_SecOps_Adms=[User("w.alejovl+secops\n-labs@gmail.com"),] 
                gg_SecOps_Adms \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_SecOps_Adms 


        with Cluster('Group: AWSControlTowerAdmins'):

                gg_AWSControlTowerAdmins=Users("AWSControlTowerA\ndmins")
                gg_AWSControlTowerAdmins \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSAdministrator\nAccess")
                mm_AWSControlTowerAdmins=[User("velez94@protonma\nil.com"),] 
                gg_AWSControlTowerAdmins \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSControlTowerAdmins 


        with Cluster('Group: AWSAuditAccountAdmins'):

                gg_AWSAuditAccountAdmins=Users("AWSAuditAccountA\ndmins")
                gg_AWSAuditAccountAdmins \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSAdministrator\nAccess")
                mm_AWSAuditAccountAdmins=[] 
                gg_AWSAuditAccountAdmins \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSAuditAccountAdmins 


        with Cluster('Group: AWSSecurityAuditors'):

                gg_AWSSecurityAuditors=Users("AWSSecurityAudit\nors")
                gg_AWSSecurityAuditors \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSReadOnlyAccess")
                mm_AWSSecurityAuditors=[] 
                gg_AWSSecurityAuditors \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSSecurityAuditors 


    with Cluster('Account: DevSecOps'):

        with Cluster('Group: AWSSecurityAuditPowerUsers'):

                gg_AWSSecurityAuditPowerUsers=Users("AWSSecurityAudit\nPowerUsers")
                gg_AWSSecurityAuditPowerUsers \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSPowerUserAcce\nss")
                mm_AWSSecurityAuditPowerUsers=[] 
                gg_AWSSecurityAuditPowerUsers \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSSecurityAuditPowerUsers 


        with Cluster('Group: DevSecOps_Admins'):

                gg_DevSecOps_Admins=Users("DevSecOps_Admins")
                gg_DevSecOps_Admins \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("LabvelDevSecOpsU\nsers")
                mm_DevSecOps_Admins=[User("DevSecOpsAdm"),] 
                gg_DevSecOps_Admins \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_DevSecOps_Admins 


        with Cluster('Group: DevSecOps_Admins'):

                gg_DevSecOps_Admins=Users("DevSecOps_Admins")
                gg_DevSecOps_Admins \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSAdministrator\nAccess")
                mm_DevSecOps_Admins=[User("DevSecOpsAdm"),] 
                gg_DevSecOps_Admins \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_DevSecOps_Admins 


        with Cluster('User: w.alejovl+devsecops-labs@gmail.com'):

                uu_walejovldevsecopslabsgmailcom=User("w.alejovl+devsec\nops-labs@gmail.com")
                uu_walejovldevsecopslabsgmailcom \
                        - Edge(color="brown", style="dotted") \
                        - IAMPermissions("AWSAdministrator\nAccess")

        with Cluster('Group: DevSecOps_Admins'):

                gg_DevSecOps_Admins=Users("DevSecOps_Admins")
                gg_DevSecOps_Admins \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("LabvelDevSecOpsRW")
                mm_DevSecOps_Admins=[User("DevSecOpsAdm"),] 
                gg_DevSecOps_Admins \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_DevSecOps_Admins 


        with Cluster('Group: AWSSecurityAuditors'):

                gg_AWSSecurityAuditors=Users("AWSSecurityAudit\nors")
                gg_AWSSecurityAuditors \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSReadOnlyAccess")
                mm_AWSSecurityAuditors=[] 
                gg_AWSSecurityAuditors \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSSecurityAuditors 


        with Cluster('Group: AWSControlTowerAdmins'):

                gg_AWSControlTowerAdmins=Users("AWSControlTowerA\ndmins")
                gg_AWSControlTowerAdmins \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSOrganizations\nFullAccess")
                mm_AWSControlTowerAdmins=[User("velez94@protonma\nil.com"),] 
                gg_AWSControlTowerAdmins \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSControlTowerAdmins 


    with Cluster('Account: Ops'):

        with Cluster('Group: AWSSecurityAuditPowerUsers'):

                gg_AWSSecurityAuditPowerUsers=Users("AWSSecurityAudit\nPowerUsers")
                gg_AWSSecurityAuditPowerUsers \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSPowerUserAcce\nss")
                mm_AWSSecurityAuditPowerUsers=[] 
                gg_AWSSecurityAuditPowerUsers \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSSecurityAuditPowerUsers 


        with Cluster('User: w.alejovl+ct-labs@gmail.com'):

                uu_walejovlctlabsgmailcom=User("w.alejovl+ct-lab\ns@gmail.com")
                uu_walejovlctlabsgmailcom \
                        - Edge(color="brown", style="dotted") \
                        - IAMPermissions("AWSAdministrator\nAccess")

        with Cluster('Group: AWSSecurityAuditors'):

                gg_AWSSecurityAuditors=Users("AWSSecurityAudit\nors")
                gg_AWSSecurityAuditors \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSReadOnlyAccess")
                mm_AWSSecurityAuditors=[] 
                gg_AWSSecurityAuditors \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSSecurityAuditors 


        with Cluster('Group: AWSControlTowerAdmins'):

                gg_AWSControlTowerAdmins=Users("AWSControlTowerA\ndmins")
                gg_AWSControlTowerAdmins \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSOrganizations\nFullAccess")
                mm_AWSControlTowerAdmins=[User("velez94@protonma\nil.com"),] 
                gg_AWSControlTowerAdmins \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSControlTowerAdmins 


    with Cluster('Account: SharedServices'):

        with Cluster('Group: AWSSecurityAuditPowerUsers'):

                gg_AWSSecurityAuditPowerUsers=Users("AWSSecurityAudit\nPowerUsers")
                gg_AWSSecurityAuditPowerUsers \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSPowerUserAcce\nss")
                mm_AWSSecurityAuditPowerUsers=[] 
                gg_AWSSecurityAuditPowerUsers \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSSecurityAuditPowerUsers 


        with Cluster('Group: DevSecOps_Admins'):

                gg_DevSecOps_Admins=Users("DevSecOps_Admins")
                gg_DevSecOps_Admins \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSAdministrator\nAccess")
                mm_DevSecOps_Admins=[User("DevSecOpsAdm"),] 
                gg_DevSecOps_Admins \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_DevSecOps_Admins 


        with Cluster('User: w.alejovl+shared-labs@gmail.com'):

                uu_walejovlsharedlabsgmailcom=User("w.alejovl+shared\n-labs@gmail.com")
                uu_walejovlsharedlabsgmailcom \
                        - Edge(color="brown", style="dotted") \
                        - IAMPermissions("AWSAdministrator\nAccess")

        with Cluster('Group: AWSSecurityAuditors'):

                gg_AWSSecurityAuditors=Users("AWSSecurityAudit\nors")
                gg_AWSSecurityAuditors \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSReadOnlyAccess")
                mm_AWSSecurityAuditors=[] 
                gg_AWSSecurityAuditors \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSSecurityAuditors 


        with Cluster('Group: AWSControlTowerAdmins'):

                gg_AWSControlTowerAdmins=Users("AWSControlTowerA\ndmins")
                gg_AWSControlTowerAdmins \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSOrganizations\nFullAccess")
                mm_AWSControlTowerAdmins=[User("velez94@protonma\nil.com"),] 
                gg_AWSControlTowerAdmins \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSControlTowerAdmins 


    with Cluster('Account: LabVel'):

        with Cluster('Group: AWSSecurityAuditPowerUsers'):

                gg_AWSSecurityAuditPowerUsers=Users("AWSSecurityAudit\nPowerUsers")
                gg_AWSSecurityAuditPowerUsers \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSPowerUserAcce\nss")
                mm_AWSSecurityAuditPowerUsers=[] 
                gg_AWSSecurityAuditPowerUsers \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSSecurityAuditPowerUsers 


        with Cluster('Group: AWSAccountFactory'):

                gg_AWSAccountFactory=Users("AWSAccountFactory")
                gg_AWSAccountFactory \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSServiceCatalo\ngEndUserAccess")
                mm_AWSAccountFactory=[User("velez94@protonma\nil.com"),] 
                gg_AWSAccountFactory \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSAccountFactory 


        with Cluster('Group: AWSControlTowerAdmins'):

                gg_AWSControlTowerAdmins=Users("AWSControlTowerA\ndmins")
                gg_AWSControlTowerAdmins \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSAdministrator\nAccess")
                mm_AWSControlTowerAdmins=[User("velez94@protonma\nil.com"),] 
                gg_AWSControlTowerAdmins \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSControlTowerAdmins 


        with Cluster('Group: AWSSecurityAuditors'):

                gg_AWSSecurityAuditors=Users("AWSSecurityAudit\nors")
                gg_AWSSecurityAuditors \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSReadOnlyAccess")
                mm_AWSSecurityAuditors=[] 
                gg_AWSSecurityAuditors \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSSecurityAuditors 


        with Cluster('Group: AWSServiceCatalogAdmins'):

                gg_AWSServiceCatalogAdmins=Users("AWSServiceCatalo\ngAdmins")
                gg_AWSServiceCatalogAdmins \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSServiceCatalo\ngAdminFullAccess")
                mm_AWSServiceCatalogAdmins=[] 
                gg_AWSServiceCatalogAdmins \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSServiceCatalogAdmins 


    with Cluster('Account: OrganizationManager'):

        with Cluster('Group: AWSSecurityAuditPowerUsers'):

                gg_AWSSecurityAuditPowerUsers=Users("AWSSecurityAudit\nPowerUsers")
                gg_AWSSecurityAuditPowerUsers \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSPowerUserAcce\nss")
                mm_AWSSecurityAuditPowerUsers=[] 
                gg_AWSSecurityAuditPowerUsers \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSSecurityAuditPowerUsers 


        with Cluster('Group: SecOps_Adms'):

                gg_SecOps_Adms=Users("SecOps_Adms")
                gg_SecOps_Adms \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("LabvelSecOpsAdms")
                mm_SecOps_Adms=[User("w.alejovl+secops\n-labs@gmail.com"),] 
                gg_SecOps_Adms \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_SecOps_Adms 


        with Cluster('User: w.alejovl+orgman-labs@gmail.com'):

                uu_walejovlorgmanlabsgmailcom=User("w.alejovl+orgman\n-labs@gmail.com")
                uu_walejovlorgmanlabsgmailcom \
                        - Edge(color="brown", style="dotted") \
                        - IAMPermissions("AWSAdministrator\nAccess")

        with Cluster('Group: AWSSecurityAuditors'):

                gg_AWSSecurityAuditors=Users("AWSSecurityAudit\nors")
                gg_AWSSecurityAuditors \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSReadOnlyAccess")
                mm_AWSSecurityAuditors=[] 
                gg_AWSSecurityAuditors \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSSecurityAuditors 


        with Cluster('Group: AWSControlTowerAdmins'):

                gg_AWSControlTowerAdmins=Users("AWSControlTowerA\ndmins")
                gg_AWSControlTowerAdmins \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSOrganizations\nFullAccess")
                mm_AWSControlTowerAdmins=[User("velez94@protonma\nil.com"),] 
                gg_AWSControlTowerAdmins \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSControlTowerAdmins 


    with Cluster('Account: Dev'):

        with Cluster('Group: AWSSecurityAuditPowerUsers'):

                gg_AWSSecurityAuditPowerUsers=Users("AWSSecurityAudit\nPowerUsers")
                gg_AWSSecurityAuditPowerUsers \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSPowerUserAcce\nss")
                mm_AWSSecurityAuditPowerUsers=[] 
                gg_AWSSecurityAuditPowerUsers \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSSecurityAuditPowerUsers 


        with Cluster('Group: DevSecOps_Admins'):

                gg_DevSecOps_Admins=Users("DevSecOps_Admins")
                gg_DevSecOps_Admins \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSAdministrator\nAccess")
                mm_DevSecOps_Admins=[User("DevSecOpsAdm"),] 
                gg_DevSecOps_Admins \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_DevSecOps_Admins 


        with Cluster('User: w.alejovl+dev-labs@gmail.com'):

                uu_walejovldevlabsgmailcom=User("w.alejovl+dev-la\nbs@gmail.com")
                uu_walejovldevlabsgmailcom \
                        - Edge(color="brown", style="dotted") \
                        - IAMPermissions("AWSAdministrator\nAccess")

        with Cluster('Group: AWSSecurityAuditors'):

                gg_AWSSecurityAuditors=Users("AWSSecurityAudit\nors")
                gg_AWSSecurityAuditors \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSReadOnlyAccess")
                mm_AWSSecurityAuditors=[] 
                gg_AWSSecurityAuditors \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSSecurityAuditors 


        with Cluster('Group: AWSControlTowerAdmins'):

                gg_AWSControlTowerAdmins=Users("AWSControlTowerA\ndmins")
                gg_AWSControlTowerAdmins \
                        - Edge(color="brown", style="dotted", label="Permissions Set") \
                        - IAMPermissions("AWSOrganizations\nFullAccess")
                mm_AWSControlTowerAdmins=[User("velez94@protonma\nil.com"),] 
                gg_AWSControlTowerAdmins \
                        - Edge(color="darkgreen", style="dotted", label="Member") \
                        - mm_AWSControlTowerAdmins 

