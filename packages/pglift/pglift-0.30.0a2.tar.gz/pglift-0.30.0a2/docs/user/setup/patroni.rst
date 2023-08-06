Patroni
=======

PostgreSQL high availability is achieved by using the `patroni` plugin of
pglift. This needs to be set up through a non-``null`` value for the
``patroni`` key in site settings:

.. code-block:: yaml
   :caption: settings.yaml

    patroni: {}

With the above settings, pglift assumes that an *open* etcd server is
available at ``127.0.0.1:2379``. It may be required to configure the etcd
hosts address:

.. code-block:: yaml
   :caption: settings.yaml

    patroni:
      etcd:
        hosts:
        - 192.168.60.21:2379
        - 192.168.60.21:2380

Security
--------

Via site settings, it's possible to secure communication between Patroni
and etcd via TLS.

The settings would look like the following:

.. code-block:: yaml
   :caption: settings.yaml

    patroni:
      etcd:
        protocol: https
        cacert: /path/to/cacert.crt
        cert: /path/to/client.crt
        key: /path/to/client.key

Those settings are actually copied to the etcd section in Patroni YAML
configuration file that pglift generates at instance creation.

Watchdog support
----------------

One can activate watchdog devices support via site settings. Please refer to
patroni `configuration
<https://patroni.readthedocs.io/en/latest/SETTINGS.html#watchdog>`_
and `watchdog <https://patroni.readthedocs.io/en/latest/watchdog.html>`_
documentation.

Here's an example of settings for watchdog:

.. code-block:: yaml
   :caption: settings.yaml

    patroni:
      […]
      watchdog:
        mode: required
        device: /dev/watchdog
        safety_margin: 5
