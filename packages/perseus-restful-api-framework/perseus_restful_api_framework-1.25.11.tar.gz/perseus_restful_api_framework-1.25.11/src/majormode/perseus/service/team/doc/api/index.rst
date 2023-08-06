====
Team
====

.. toctree::
   :hidden:

   delete_invitation
   delete_member
   delete_membership
   delete_team
   get_invite
   get_member
   get_members
   get_team
   get_teams
   post_invitation
   post_join
   post_team
   put_invitation
   put_master
   put_member

------------
Introduction
------------

A team represents a group of people having a common purpose or
interest, such as, for instance, an organization, an association, a
guild, an institute, a squad. etc.

A team is composed of members, who are users registered against the
platform.  A member has a specific role within the team.  There are
three possible roles that can be assigned to members: *agent*,
*administrator*, or *standard*.  Roles are used to assign certain
responsibilities to a member, such as inviting additional team
members.

* *Agent*: the *Agent* member is the user who has registered the
  team against the platform.  He is the de facto master administrator
  of the team.  He can delete the team.  He can promote any
  administrator of the team to be the new agent of this team.

* *Administrator*: an *Administrator* member can invite users to
  become member of the team, assign roles, and have access to the
  resources of this team.  A particular application, registered on
  behalf of the team, can provide other specific privileges to an
  *Administrator* member.  A team can have multiple administrators.

* *Standard*: a *Standard* member has access to the resources of the
  team.  A particular application, registered on behalf of the team,
  can provide other specific privileges to an *Standard* member.

When an administrator adds a user to the team, that user must confirm
the request before being listed as a member. The user will receive a
member request, and the user's name appears with a pending state in
the team settings until confirmation.

---------
Resources
---------

* :doc:`delete_member`: revoke the specified member from an team.

* :doc:`delete_member_request`: cancel member request sent to a user.

* :doc:`delete_team`:

* :doc:`get_invite`: return the list of the invitations to join a
  team that have been sent on behalf of a team to the specified user.

* :doc:`get_member`: return extended information about the account
  of a user who belongs to the specified team.

* :doc:`get_members`: return the list of the members of an team.



* :doc:`get_team`: return the list of the team that the user is
  member of.

* :doc:`get_teams`: return a list of teams which names match, even
  partially, the specified keywords.

* :doc:`get_member_request`: return the list of the member requests
  that have been sent to users on behalf of the specified team.



* :doc;`post_join`: submit a request on behalf of a user to join a
  team.  This join request has to be approved by one of the
  administrators of this team.




* :doc:`post_invite_acceptance`: accept on behalf of a user a member
  request that an administrator of an team sent to this user.

* :doc:`post_invite_declination`: decline on behalf of a user a
  member request that an administrator of an team sent to this user.

* :doc:`post_invite`: invite users to join a team.

* :doc:`post_team`: add a new team on behalf of a user who becomes
  then the de facto master administrator, alias the *Agent* member,
  for this team.

* :doc:`put_master`: promote on behalf of the current master
  administrator another member, member of the specified team, who
  must have the role of administrator, as the new master
  administrator for this team.

* :doc:`put_member`: update the role of the member of an team.
