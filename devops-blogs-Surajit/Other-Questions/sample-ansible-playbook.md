Here's a complex Ansible playbook that covers multiple components, including tasks, roles, handlers, conditionals, loops, variables, and notifications. Each section will be explained in detail, providing a comprehensive overview of how a complex Ansible playbook works.

### Sample Complex Ansible Playbook

```yaml
---
# 1. Playbook definition with name and hosts
- name: Provision a web server with database
  hosts: webservers
  become: true
  vars:
    db_password: "secure_db_pass"
    app_user: "webapp"
    app_group: "webgroup"
    app_name: "myapp"

  # 2. Global variables
  vars_files:
    - vars/common_vars.yml

  pre_tasks:
    # 3. Pre-task to ensure system is up-to-date before running other tasks
    - name: Update apt cache and upgrade packages
      apt:
        update_cache: yes
        upgrade: dist
      when: ansible_os_family == 'Debian'

  # 4. Roles for separation of concerns
  roles:
    - role: nginx
    - role: postgresql
    - role: nodejs_app

  tasks:
    # 5. Task to create a user for the application
    - name: Ensure the app user exists
      user:
        name: "{{ app_user }}"
        group: "{{ app_group }}"
        state: present
        createhome: yes

    # 6. Task to copy application code
    - name: Copy application files to the server
      copy:
        src: /path/to/local/code/
        dest: /var/www/{{ app_name }}
      notify:
        - Restart Nginx
        - Restart Node.js App

    # 7. Task to install npm dependencies
    - name: Install npm dependencies
      npm:
        path: /var/www/{{ app_name }}
        state: present

    # 8. Task to configure PostgreSQL database
    - name: Ensure PostgreSQL database and user exist
      postgresql_db:
        name: "{{ app_name }}_db"
        login_user: postgres
        login_password: "{{ db_password }}"
      notify: Restart PostgreSQL

  handlers:
    # 9. Handler to restart Nginx
    - name: Restart Nginx
      service:
        name: nginx
        state: restarted

    # 10. Handler to restart Node.js App
    - name: Restart Node.js App
      service:
        name: nodejs
        state: restarted

    # 11. Handler to restart PostgreSQL
    - name: Restart PostgreSQL
      service:
        name: postgresql
        state: restarted

  post_tasks:
    # 12. Post-task to check application status
    - name: Check if the app is running
      uri:
        url: http://localhost:3000/health
        status_code: 200
      retries: 5
      delay: 10
      register: app_status

    - name: Print application status
      debug:
        msg: "Application is up and running: {{ app_status.status == 200 }}"

  # 13. Include custom playbook if certain conditions are met
  - name: Additional configuration for production environment
    include: production_setup.yml
    when: ansible_env == 'production'
```

### Detailed Explanation of Each Component

#### 1. **Playbook Definition**
```yaml
- name: Provision a web server with database
  hosts: webservers
  become: true
```
- **name**: A human-readable name for the playbook.
- **hosts**: Defines the group of hosts (or specific host) where the tasks will be executed. In this case, it's the `webservers` group.
- **become**: Elevates privileges to execute tasks with `sudo` (or root user) permissions.

#### 2. **Global Variables**
```yaml
vars:
  db_password: "secure_db_pass"
  app_user: "webapp"
  app_group: "webgroup"
  app_name: "myapp"
```
- Variables can be defined at the play level and are accessible throughout the playbook. These variables are used to store values like the database password, application user, group, and name, which are referenced later in the playbook.

```yaml
vars_files:
  - vars/common_vars.yml
```
- **vars_files**: Allows external files to be included that store additional variables. The `common_vars.yml` file can contain more specific configurations or secrets.

#### 3. **Pre-tasks**
```yaml
pre_tasks:
  - name: Update apt cache and upgrade packages
    apt:
      update_cache: yes
      upgrade: dist
    when: ansible_os_family == 'Debian'
```
- **Pre-tasks**: These tasks are executed before the main tasks. In this example, the system is updated before proceeding.
- **`when` condition**: Ensures this task runs only if the target system’s OS family is Debian-based.

#### 4. **Roles**
```yaml
roles:
  - role: nginx
  - role: postgresql
  - role: nodejs_app
```
- **Roles**: A role is a structured way of organizing playbooks into reusable components. Each role can contain tasks, variables, templates, and files that are specific to a particular function like setting up Nginx, PostgreSQL, or a Node.js app.

#### 5. **Tasks - Create a User**
```yaml
tasks:
  - name: Ensure the app user exists
    user:
      name: "{{ app_user }}"
      group: "{{ app_group }}"
      state: present
      createhome: yes
```
- **Tasks**: The core part of the playbook. Each task defines a specific action to be taken.
- The **user** module ensures the app user exists, with a home directory and correct group.

#### 6. **Tasks - Copy Files**
```yaml
- name: Copy application files to the server
  copy:
    src: /path/to/local/code/
    dest: /var/www/{{ app_name }}
  notify:
    - Restart Nginx
    - Restart Node.js App
```
- The **copy** module copies the application files to the server. It uses a variable (`{{ app_name }}`) to define the destination path.
- The **notify** directive triggers handlers (discussed later) to restart services after the task is complete.

#### 7. **Tasks - Install npm Dependencies**
```yaml
- name: Install npm dependencies
  npm:
    path: /var/www/{{ app_name }}
    state: present
```
- The **npm** module is used to install Node.js dependencies for the application. This ensures that all required packages are available for the app.

#### 8. **Tasks - Configure PostgreSQL**
```yaml
- name: Ensure PostgreSQL database and user exist
  postgresql_db:
    name: "{{ app_name }}_db"
    login_user: postgres
    login_password: "{{ db_password }}"
  notify: Restart PostgreSQL
```
- The **postgresql_db** module is used to ensure a database is created for the app.
- **notify** is used to trigger the restart of PostgreSQL after changes.

#### 9. **Handlers - Restart Nginx**
```yaml
handlers:
  - name: Restart Nginx
    service:
      name: nginx
      state: restarted
```
- **Handlers**: These are tasks that are triggered only when notified by other tasks. This handler restarts the Nginx service when the app files are copied.

#### 10. **Handlers - Restart Node.js App**
```yaml
- name: Restart Node.js App
  service:
    name: nodejs
    state: restarted
```
- This handler restarts the Node.js application after the application code is copied.

#### 11. **Handlers - Restart PostgreSQL**
```yaml
- name: Restart PostgreSQL
  service:
    name: postgresql
    state: restarted
```
- Similar to the other handlers, this restarts PostgreSQL when changes to the database configuration are made.

#### 12. **Post-tasks - Check Application Status**
```yaml
post_tasks:
  - name: Check if the app is running
    uri:
      url: http://localhost:3000/health
      status_code: 200
    retries: 5
    delay: 10
    register: app_status
```
- **Post-tasks**: These are executed after the main tasks are done.
- The **uri** module checks if the application is running by querying a `/health` endpoint. If the status code is 200, the app is considered running.
- **retries** and **delay** are used to retry the request in case of failure.

#### 13. **Conditional Task Execution**
```yaml
- name: Additional configuration for production environment
  include: production_setup.yml
  when: ansible_env == 'production'
```
- This task conditionally includes another playbook (`production_setup.yml`) only when the environment is production (`ansible_env == 'production'`).

### Summary of Key Components:
1. **Playbook Definition**: Defines the playbook name, hosts, and privileges.
2. **Global Variables and `vars_files`**: Store reusable data for tasks.
3. **Pre-tasks**: Tasks that run before the main tasks.
4. **Roles**: Organize playbooks into reusable components for specific tasks like Nginx, PostgreSQL, etc.
5. **Tasks**: The actual actions to be taken (creating users, installing packages, copying files

, etc.).
6. **Handlers**: Special tasks triggered by notifications to restart services.
7. **Post-tasks**: Tasks executed after the main tasks, such as checking the application status.
8. **Conditionals**: Execute certain tasks or include playbooks based on conditions (e.g., environment variables).


