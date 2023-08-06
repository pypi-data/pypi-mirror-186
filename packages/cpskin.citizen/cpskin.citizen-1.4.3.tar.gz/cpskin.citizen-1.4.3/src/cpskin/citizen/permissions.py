# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from AccessControl.SecurityInfo import ModuleSecurityInfo
from Products.CMFCore.permissions import setDefaultRoles


security = ModuleSecurityInfo("cpskin.citizen")

security.declarePublic("ModifyCitizenContent")
ModifyCitizenContent = "Modify citizen content"
setDefaultRoles(ModifyCitizenContent, ("Manager", "Citizen Editor"))

security.declarePublic("AdminCitizenContent")
AdminCitizenContent = "Admin citizen content"
setDefaultRoles(
    AdminCitizenContent, ("Manager", "Site Administrator", "Reviewer", "Editor")
)
