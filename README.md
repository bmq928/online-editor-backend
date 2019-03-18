#convention
* folder with underscore (_) define private module (just interact with each other or is utils)
* folder without underscore (api: controller, route)

#start


* create config/production.json
* create folder logs
* create folder project-storage  which container project
* build image
  e.x: docker build . -t online-editor-backend
* run container
  e.x: docker run -d --name online-editor-backend \
     -e USER_RELATED_ROOT_URL=''  # login url \
     -e PROJECT_RELATED_ROOT_URL='' # project \
     -v<logs-folder>:/app/logs \
     -v<project-store>:/storage \
     -p3001:3001 online-editor-backend