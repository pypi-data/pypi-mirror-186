# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone import api
from plone.app.layout.viewlets import common as base
from plone.app.stagingbehavior.utils import get_working_copy

from cpskin.citizen import utils


class CitizenBaseViewlet(base.ViewletBase):
    def update(self):
        self.current_user = api.user.get_current()
        if self.can_view:
            self.annotations = utils.get_annotations(self.context)

    @property
    def can_view(self):
        return True

    @property
    def comment(self):
        return self.annotations.get("comment", None)

    @property
    def validation_required(self):
        return self.annotations.get("validation_required", False)

    @property
    def has_claims(self):
        return len(self.annotations.get("claim", [])) > 0

    @property
    def awaiting_claims(self):
        claims = []
        for claim in utils.get_claims(self.context):
            user_id, reason = claim
            user = api.user.get(userid=user_id)
            if user:
                claims.append(
                    {
                        "id": claim,
                        "user_id": user_id,
                        "username": user.getProperty("fullname"),
                        "email": user.getProperty("email"),
                        "reason": reason,
                    }
                )
        return claims


class CitizenEditionViewlet(CitizenBaseViewlet):
    def update(self):
        super(CitizenEditionViewlet, self).update()
        if self.can_view:
            self.have_claimed = utils.have_claimed(self.current_user, self.context)

    @property
    def can_view(self):
        if api.user.is_anonymous() is True:
            return False
        return utils.is_citizen(self.current_user)

    @property
    def can_edit(self):
        return utils.can_edit_citizen(self.current_user, self.context)

    @property
    def can_claim(self):
        return utils.can_claim(self.current_user, self.context)

    @property
    def can_cancel(self):
        if utils.can_edit_citizen(self.current_user, self.context) is False:
            return False
        return self.context == get_working_copy(self.context)

    @property
    def can_ask_validation(self):
        if self.context != get_working_copy(self.context):
            return False
        return not self.validation_required

    @property
    def show_fieldset(self):
        if self.can_edit or self.can_cancel or self.can_ask_validation:
            return True
        if self.can_claim and not self.have_claimed:
            return True
        return False


class CitizenAdminViewlet(CitizenBaseViewlet):
    pass


class CitizenProposeContentViewlet(CitizenBaseViewlet):
    pass


class CitizenInfoViewlet(CitizenBaseViewlet):
    @property
    def can_view(self):
        if api.user.is_anonymous() is True:
            return False
        return utils.is_citizen(self.current_user)

    @property
    def url(self):
        return "{0}/citizen-dashboard/".format(
            api.portal.get_navigation_root(self.context).absolute_url()
        )
