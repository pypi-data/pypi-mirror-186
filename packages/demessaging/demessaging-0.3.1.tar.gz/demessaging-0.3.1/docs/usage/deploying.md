# Deploying Backend Modules
This is one of the strengths of DASF. You can deploy a backend module basically anywhere. The only requirement is, that the backend module is able to establish a connection to the used message broker instance.

```{admonition} Firewalls
:class: warning

This is especially useful for the deployment behind institutional firewalls. Since the backend module itself is establishing the connection and not the calling instance. So, as long as the firewall allows outward connections to the message broker instance the backend module can be used by all clients that are also able to connect to the message broker.
```