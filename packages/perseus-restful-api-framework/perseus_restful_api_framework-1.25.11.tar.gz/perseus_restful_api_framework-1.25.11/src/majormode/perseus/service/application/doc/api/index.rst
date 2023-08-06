===========
Application
===========

.. toctree::
   :hidden:

   delete_member
   get_applications
   post_application
   post_member
   put_application
   put_master
   put_member

------------
Introduction
------------

An application, also referred as a *client application*, is a Web
application, a desktop application, a mobile application, or any
other communication program, that needs to access, generally on
behalf of a end-user, services deployed on the server platform.

The team responsible for the development of a client application must
register this application against the server platform before this
application is allowed to access the platform's services.

.. note:: the current version of the platform doesn't force a team to define the scope of their client application, meaning that this team don't have to indicate which exact services of the platform their application to access to.  The current version of the platform allows the client application to access to all the existing services currently deployed.

The server platform generates an Application Programming Interface
(API) key, i.e., a string that is tied to the client application, and
a secret key.  Most of the platform services require the client
application to pass the API key within a HTTP request.  Such a HTTP
request has to be signed with the secret key associated to this API
key.

A development team is basically composed of members of different roles
that offer different privileges:

* Administrator: such a member can add or remove other members of
  the development team, define their role, specify the environment
  stage of a particular released version of the client application
  (e.g., sandbox or live).

* Developer: such a member can build and deploy the client
  application to the environment stage currently selected.

The user who registered the application against the platform is
promoted by default master administrator.  Such a user cannot be
removed from the development team.  There is only one master
administrator for the application at a given time.  A master
administrator can promote another administrator of the client
application as the new master administrator, himself becoming then a
simple administrator.

----------------------
HTTP Request Signature
----------------------


---------
Resources
---------

* :doc:`post_application`: register a new client application.

* :doc:`put_application`: update some modifiable properties of the
  specified client application.

* :doc:`post_member`: add a new member, such as a developer or an
  administrator, to manage the specified client application.

* :doc:`put_member`: update the role of a member of a given client
  application.

* :doc:`delete_member`: revoke the role of the specified user
  account as a member of a given client application.

* :doc:`put_master`: promote on behalf of the current master
  administrator another member, belonging to the development team of
  the specified application, who must have the role of administrator,
  as the new master administrator for this application.

* :doc:`get_applications`: retrieve extended information about the
  client applications that the end user on behalf of this function is
  called has access to, either as a developer, either as an
  administrator.
