# Notice: This template has only been tested
# under Python27 + GAE standard environment
#application: Py-Google-HW
#version: 1
runtime: python27
# threadsafe is required but can be either true or
# false. For some package, it should be true e.g. Flask
threadsafe: false
api_version: 1

handlers:
- url: /.*
  script: test.py