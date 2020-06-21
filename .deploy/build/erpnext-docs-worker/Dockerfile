FROM frappe/frappe-worker:develop

RUN install_app erpnext_documentation https://github.com/frappe/erpnext_documentation

RUN chown -R frappe:frappe /home/frappe/frappe-bench/apps
