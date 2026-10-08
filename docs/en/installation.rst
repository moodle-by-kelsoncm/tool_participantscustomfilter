Installation
============

Step by Step
------------

1. Clone the repository into Moodle's administrative tools directory:

   .. code-block:: bash

      cd /path/to/moodle/admin/tool
      git clone https://github.com/moodle-by-kelsoncm/tool_participantscustomfilter.git participantscustomfilter

2. Run the upgrade script via the command line:

   .. code-block:: bash

      php admin/cli/upgrade.php --non-interactive
