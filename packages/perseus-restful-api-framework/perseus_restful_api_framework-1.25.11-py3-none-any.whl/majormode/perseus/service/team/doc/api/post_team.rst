==============
``POST /team``
==============

--------
Synopsis
--------

Create a new team on behalf of a user.  This user becomes the agent of
this team, the master administrator.  He can delete the team.  He can
promote any administrator of the team to be the new agent of this
team.


---------------------
Request Header Fields
---------------------

.. include:: /_include/authenticated_session_header_fields.inc


------------------------
Request Query Parameters
------------------------

None


--------------------
Request Message Body
--------------------

The request must contain a JSON form containing the properties of the
team to create::

    {
      "administrator_acceptance_quorum"": float,
      "administrator_revocation_quorum": float,
      "description": string,
      "invitation_email": string,
      "invitation_url": string
      "name": string,
      "accept_admin_quorum": decimal,
      "revoke_admin_quorum": decimal
    }

where:

* ``administrator_acceptance_quorum`` (optional): minimum number of
  administrators of the team, expressed in percentage of the total
  number of administrators, that must accept a user to be granted the
  role of administrator so that decisions can be made properly.  If
  not defined, the default value is ``0.0``, in which case, only the
  agent of the team can grant the role of administrator to a member.

* ``administrator_revocation_quorum`` (optional): minimum number of
  administrators of the team, expressed in percentage of the total
  number of administrators, that must revoke a member from the team
  so that decisions can be made properly.  If not defined, the
  default value is ``0.0``, in which case only the agent of the team
  can revoke the role of administrator from a member.

* ``description`` (optional): a textual description of the team.

* ``invitation_email`` (optional): template of the letter to be sent
  by email to a user who is invited to join this team.  If no
  specific template is specified for this team, the platform provides
  a default template, such as, for instance::

    Dear %(recipient_name)s,

    %(sender_name)s has invited you to join the organization
    %(team_name)s. As a member, you can access a wealth of resources of
    this organization. If you have already registered an account and are
    interested in accepting this invitation, click the invitation code
    below:

    %(invitation_url)s

    If you have not registered an account, you will be taken through the
    registration process after clicking the invitation code above.

    Please contact your Team Administrator, %(sender_name)s with any
    questions. You have 30 days to respond. After 30 days, your invitation
    will expire.

    Best regards,

    %(team_name)s

  The template can contain the following placeholders -- using
  Python extended format codes, also known as pyformat parameter
  style -- that will be substituted with their corresponding values:

  * ``invitation_url``: Uniform Resource Locator (URL) that is
    provided as a link in the email the platform sends to the user
    that is invited to join the team.

  * ``invitation_code``: invitation code that is sent to the user
    that is invited to join the team.  It should be included in the
    invitation URL, such as for instance::

      http://www.example.com/team/invitation/%(invitation_code)s?accept=true

  * ``recipient_name``: name of the user that is invited to join
    the team.

  * ``sender_name``: name of the administrator of the team who
    invited the user to join the team.

  * ``team_name``: name of the team the user is invited to join.

* ``invitation_url`` (optional): Uniform Resource Locator (URL) that
  is provided as a link in the email the platform sends to a user who
  is invited to join the team.  When the user clicks on the link
  embedded in the email, the email reader application issues a HTTP
  GET request to this URL.

* ``name`` (required): name of the team.  This name MUST be unique
  among all the teams that have been registered so far against the
  platform.  Case is not sensitive.


---------------------
Response Message Body
---------------------

The platform returns the following JSON structure::

    {
      "creation_time": timestamp,
      "team_id": string
    }

where:

* ``creation_time`` (required): date and time when this team has
  been created.

* ``team_id`` (required): the identification of the team, unique
  among the platform.


----------
Exceptions
----------

The platform MAY raise the following exceptions to indicate that one
or several required conditions have not been respected:

* ``InvalidOperationException``: if the name of the team passed to
  this function is already used for an other team registered against
  the platform.
