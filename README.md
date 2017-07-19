README
======

This is a port of the Django REST Framework
[Quickstart](http://www.django-rest-framework.org/tutorial/quickstart/). using
MongDB as the database backend.

In searching for a way to use MongoDB as the database for Django I came across
a number of libraries and examples that did not quite come together for me.
This is my attempt to clarify the process and see the limitations of the
selected implementations.

# Packages
MongoEngine -_Object-Document Mapper, written in Python for working with
MongoDB_. This seems to underpin all the Django Mongo interaction
implementations.

[Django Rest
Framework Mongoengine](https://github.com/umutbozkurt/django-rest-framework-mongoengine)
- _provides mongoengine support for django-rest-framework_

# Overview
Django comes with its own ORM. This allows database entries to be interacted
with in Python using objects. This standard, relational database specific,
layer is replaced by MongoEngine. Therefore, the models defined are defined
using MongoEngine.

MongoEngine _uses a simple declarative API, similar to the Django ORM_ so the
transition here should be relatively straightforward. Instead of using
DjangoORM and its models we use MongoEngine and its models. At the time writing
MonogEngine has support for Django, but in a [unstable
state](https://github.com/MongoEngine/django-mongoengine). Regardless of this
I will be using it.

[Django REST Framework](http://www.django-rest-framework.org) provides
a _flexible toolkit for building Web APIs._ Simply, it allows Django models to
be exposed via a Web API.

Django Rest Framework Mongoengine _provides mongoengine support for
django-rest-framework_. Therefore, it exposes MongoEngine models via a Web API.


See `quickstart.md`
