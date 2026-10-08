Configuration & AMD Build
==========================

AMD JavaScript Compilation (Developers)
---------------------------------------

If you make any changes to the JavaScript source code inside `amd/src/`:

.. code-block:: bash

   cd /var/www/html
   npm install
   cd /var/www/html/admin/tool/participantscustomfilter/amd
   npx grunt amd -v --force

Purge Moodle's JS cache at **Site administration > Development > Purge caches**.
