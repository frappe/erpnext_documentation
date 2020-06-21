FROM bitnami/node:12-prod

COPY .deploy/build/erpnext-docs-nginx/install_app.sh /install_app

RUN /install_app erpnext_documentation https://github.com/frappe/erpnext_documentation

FROM frappe/frappe-nginx:develop

COPY --from=0 /home/frappe/frappe-bench/sites/ /var/www/html/
COPY --from=0 /rsync /rsync
RUN echo -n "\nerpnext_documentation" >> /var/www/html/apps.txt

VOLUME [ "/assets" ]

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
