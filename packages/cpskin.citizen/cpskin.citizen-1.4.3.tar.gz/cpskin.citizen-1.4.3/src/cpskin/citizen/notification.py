# -*- coding: utf-8 -*-

from Products.CMFPlone.utils import safe_unicode
from cpskin.citizen import _
from cpskin.citizen.browser.settings import ISettings
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from plone import api
from smtplib import SMTPException
from zope.i18n import translate


def _generate_email(body, obj):
    html = safe_unicode(
        """<html><body style="font-family: arial;">{0},<br><br>""" "{1}</body></html>"
    )
    html_body = html.format(translate(_("Hello"), context=obj.REQUEST), body)
    msg = MIMEMultipart("alternative")
    msg.attach(MIMEText(html_body.encode("utf-8"), "html", "UTF-8"))
    return msg


def _get_recipient(userid):
    """ Return the email address for the given userid """
    user = api.user.get(userid=userid)
    if user:
        return user.getProperty("email")


def _get_admin_recipients():
    record = api.portal.get_registry_record(
        interface=ISettings, name="manager_email", default=""
    )
    if not record:
        return []
    return record.split(";")


def _send_email(recipient, sender, subject, body):
    """ Wrapper for plone.api.send_email function that handle special usecases """
    try:
        api.portal.send_email(
            recipient=recipient, sender=sender, subject=safe_unicode(subject), body=body
        )
    except SMTPException:
        pass


def notify_content_validated(obj):
    """ Send an email to notify the citizen owner(s) of the document that the content
    was published
    """
    citizens = getattr(obj, "citizens", [])
    if not citizens:
        # This can happen when this is not a citizen manage content
        return
    portal = api.portal.get()
    title = translate(
        _(u"You have a message about a content that you manage on {portal_url}"),
        context=obj.REQUEST,
    )
    title = title.format(portal_url=portal.absolute_url())
    body = translate(
        _(
            u"""The content "{title}" that you manage on the website {portal_url}"""
            u"""<a href="{link}" alt="{title}">requires a modification from you</a>"""
        ),
        context=obj.REQUEST,
    )
    body = body.format(
        link=obj.absolute_url(), title=obj.title, portal_url=portal.absolute_url()
    )

    for citizen in citizens:
        recipient = _get_recipient(citizen)
        _send_email(recipient, portal.email_from_address, title, _generate_email(body, obj))


def notify_content_refused(obj):
    """ Send an email to notify the citizen owner(s) of the document that a change
    must be made
    """
    citizens = getattr(obj, "citizens", [])
    if not citizens:
        # This can happen when this is not a citizen manage content
        return
    portal = api.portal.get()
    title = translate(
        _(u"You have a message about a content that you manage on {portal_url}"),
        context=obj.REQUEST,
    )
    title = title.format(portal_url=portal.absolute_url())
    body = translate(
        _(
            u"""The content "{title}" that you manage on the website {portal_url}"""
            u"""<a href="{link}" alt="{title}">was published online</a>"""
        ),
        context=obj.REQUEST,
    )
    body = body.format(
        link=obj.absolute_url(), title=obj.title, portal_url=portal.absolute_url()
    )

    for citizen in citizens:
        recipient = _get_recipient(citizen)
        _send_email(recipient, portal.email_from_address, title, _generate_email(body, obj))


def notify_content_awaiting_validation(obj, user):
    """ Send an email to notify the administrator that a new content
    is awaiting for review
    """
    portal = api.portal.get()
    title = translate(
        _(u"You have a request about a citizen content on {portal_url}"),
        context=obj.REQUEST,
    )
    title = title.format(portal_url=portal.absolute_url())
    body = translate(
        _(
            u"""<a href="{link}" alt="{title}">A review for a citizen content</a>"""
            u"was requested by {name}"
        ),
        context=obj.REQUEST,
    )
    body = body.format(
        link=obj.absolute_url(),
        title=obj.title,
        name=user.getProperty("fullname").decode("utf8"),
    )

    recipients = [portal.email_from_address]
    recipients.extend(_get_admin_recipients())
    for recipient in recipients:
        _send_email(recipient, portal.email_from_address, title, _generate_email(body, obj))


def notify_content_awaiting_access(obj, user):
    """ Send an email to notify the administrator that an access to a content
    is awaiting for approval
    """
    portal = api.portal.get()
    title = translate(
        _(u"You have a request about a citizen content on {portal_url}"),
        context=obj.REQUEST,
    )
    title = title.format(portal_url=portal.absolute_url())
    body = translate(
        _(
            u"""<a href="{link}" alt="{title}">A new access request</a> from {name} """
            u"for a citizen content is awaiting for approval"
        ),
        context=obj.REQUEST,
    )
    body = body.format(
        link=obj.absolute_url(),
        title=obj.title,
        name=user.getProperty("fullname").decode("utf8"),
    )

    recipients = [portal.email_from_address]
    recipients.extend(_get_admin_recipients())
    for recipient in recipients:
        _send_email(recipient, portal.email_from_address, title, _generate_email(body, obj))
