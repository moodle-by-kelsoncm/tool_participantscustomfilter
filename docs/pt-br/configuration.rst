Configuração & Build AMD
========================

Compilação do JavaScript AMD (Desenvolvedores)
----------------------------------------------

Caso realize alterações no código-fonte JavaScript dentro de `amd/src/`:

.. code-block:: bash

   cd /var/www/html
   npm install
   cd /var/www/html/admin/tool/participantscustomfilter/amd
   npx grunt amd -v --force

Limpe o cache JS do Moodle em **Administração do site > Desenvolvimento > Limpar caches**.
