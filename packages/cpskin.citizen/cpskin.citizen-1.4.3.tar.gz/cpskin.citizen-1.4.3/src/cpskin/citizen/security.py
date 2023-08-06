# -*- coding: utf-8 -*-

from cpskin.citizen import _
from cpskin.citizen import utils
from plone import api
from plone.protect.auto import safeWrite


def _get_draft_folders():
    portal = api.portal.get()
    lrfs = api.content.find(context=portal, portal_type="LRF")
    if not lrfs:
        return [portal[utils.DRAFT_FOLDER_ID]]
    return [lrf.getObject()[utils.DRAFT_FOLDER_ID] for lrf in lrfs]


def _get_dashboard_folders():
    portal = api.portal.get()
    lrfs = api.content.find(context=portal, portal_type="LRF")
    folders = []
    if not lrfs:
        base_folder = portal[utils.DASHBOARD_FOLDER_ID]
        folders.append(base_folder)
        folders.extend([base_folder[e] for e in utils.DASHBOARD_FOLDERS_IDS])
        return folders
    for lrf in lrfs:
        base_folder = lrf.getObject()[utils.DASHBOARD_FOLDER_ID]
        folders.append(base_folder)
        folders.extend([base_folder[e] for e in utils.DASHBOARD_FOLDERS_IDS])
    return folders


class ManageSecurity(object):
    def __init__(self, request):
        self.request = request
        self.report = {}
        self.draft_folders = _get_draft_folders()
        self.dashboard_folders = _get_dashboard_folders()

    def add_report_msg(self, obj, msg, type="error"):
        url = obj.absolute_url()
        if url not in self.report:
            self.report[url] = []
        self.report[url].append((type, msg))
        return self.report

    def _manage_role_acquisition(self, obj, block=True):
        """ Manage local role acquisition for a contentish object """
        if block is True:
            expected_value = 1
            me = api.content.disable_roles_acquisition
            msg = (
                _("Role acquisition was disabled"),
                _("Role acquisition already disabled"),
            )
        else:
            expected_value = 0
            me = api.content.enable_roles_acquisition
            msg = (
                _("Role acquisition was enabled"),
                _("Role acquisition already enabled"),
            )
        if getattr(obj, "__ac_local_roles_block__", 0) != expected_value:
            safeWrite(obj, self.request)
            me(obj=obj)
            self.add_report_msg(obj, msg[0], type="error")
        else:
            self.add_report_msg(obj, msg[1], type="info")

    def _manage_local_roles(self, obj, roles):
        """ Manage local roles for an object """
        for user, current_roles in obj.get_local_roles():
            if user not in roles.keys():
                safeWrite(obj, self.request)
                obj.manage_delLocalRoles([user])
                self.add_report_msg(
                    obj, _("Remove local roles for user {0}").format(user), type="error"
                )
        current_local_roles = {k: v for k, v in obj.get_local_roles()}
        for user, new_roles in roles.items():
            if user not in current_local_roles.keys():
                safeWrite(obj, self.request)
                obj.manage_setLocalRoles(user, new_roles)
                self.add_report_msg(
                    obj, _("Add local roles for user {0}").format(user), type="error"
                )
            else:
                if new_roles != current_local_roles[user]:
                    safeWrite(obj, self.request)
                    obj.manage_setLocalRoles(user, new_roles)
                    self.add_report_msg(
                        obj,
                        _("update local roles for user {0}").format(user),
                        type="error",
                    )
                else:
                    self.add_report_msg(
                        obj,
                        _("local roles are correct for user {0}").format(user),
                        type="info",
                    )

    def migrate(self):
        self._migrate_draft_folders()
        self._migrate_dashboard_folders()
        return self.report

    def _migrate_draft_folders(self):
        # Fix permissions on folder (No citizen users must have access to draft folder)
        # Do not acquire from parent folder
        for draft_folder in self.draft_folders:
            # role acquisition must be disabled
            self._manage_role_acquisition(draft_folder, block=True)
            self._manage_local_roles(draft_folder, roles={"admin": ("Owner",)})

    def _migrate_dashboard_folders(self):
        # Ensure that permissions on dashboard folders are corrects
        # Root : citizen can view / do not acquire from parent folder
        # Mes contenus, citizen-map : citizen -> can view
        # citizen-content, citizen-claims, citizen-propose-content : inherit from parent folder (citizen -> can view)
        # admin-claims, admin-content : citizen can not view
        security_map = {
            "citizen-dashboard": {
                "roles": {"admin": ("Owner",), "Citizens": ("Reader",)},
                "block": True,
            },
            "citizen-content": {"roles": {"admin": ("Owner",)}, "block": False},
            "citizen-claims": {"roles": {"admin": ("Owner",)}, "block": False},
            "citizen-map": {"roles": {"admin": ("Owner",)}, "block": False},
            "citizen-propose-content": {"roles": {"admin": ("Owner",)}, "block": False},
            "admin-content": {"roles": {"admin": ("Owner",)}, "block": True},
            "admin-claims": {"roles": {"admin": ("Owner",)}, "block": True},
        }
        for dashboard_folder in self.dashboard_folders:
            security = security_map.get(dashboard_folder.id)
            self._manage_role_acquisition(dashboard_folder, block=security["block"])
            self._manage_local_roles(dashboard_folder, security["roles"])
