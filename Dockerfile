FROM docker.somko.be/odoo/enterprise:13

USER root

COPY custom /mnt/repo/custom
COPY third /mnt/repo/third

USER odoo
