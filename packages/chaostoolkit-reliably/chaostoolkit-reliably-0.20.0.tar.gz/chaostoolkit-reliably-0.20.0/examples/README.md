# Overview

A few dummy experiments that demonstrate how you can use Reliably and SLO to 
play nicely with your Chaos Toolkit experiments.

To make it simple, make sure you have [installed][reliablyinstall] the
`reliably` CLI and [logged in][reliablylogin] against Reliably.

[reliablyinstall]: https://reliably.com/docs/getting-started/install/
[reliablylogin]: https://reliably.com/docs/getting-started/login/

Once logged in you should see a a file at:

```
~/.config/reliably/config.yaml
```

This file is important as the extension will use it to authenticate.

These experiments do not focus on what they actually experiment on but are
templates on integrating against Reliably's service to benefit from SLO in
Chaos Engineering experiments.

Make sure to install the Chaos Toolkit requirements for these experiments:

```console
$ pip install -r requirements.txt
```

# Use SLO as a Steady-State

File: use-slo-as-steady-state.json

This experiment describes how you can use your SLO as a natural steady-state
hypothesis in order to indicate if the experiment deviated or not.

SLO are fantastic for this because they are grounded into the reality of your
system. They also have been discussed and agreed by the team already, so a
deviation from them can be immediatly understood by everyone.

# Use SLO as a safeguard

File: use-slo-as-experiment-safeguard.json

This experiment describes how you can use your SLO as a natural safeguard
to protect your system from experiments that may indeed harm it too extensively.

Your SLO are being checked regularly during the experiment and as soon as one
of them breaks its target, the safeguard mechanism interrupts the experiment.

# Run from the Chaos Toolkit Kubernetes operator

File: run-from-kubernetes-operator.yaml

This experiment only differs from the way it's executed. It runs from the
[Chaos Toolkit operator](https://chaostoolkit.org/deployment/k8s/operator/).

To run it:

* Ensure you have first a Kubernetes cluster with the operator deployed

* Now create the `chaostoolkit-run` namespace:

```console
$ kubectl create ns chaostoolkit-run
```

* Then create a configmap with your Reliably's configuration:

```console
$ kubectl -n chaostoolkit-run create secret generic \
    reliably-config \
    --from-file=$HOME/.config/reliably/config.yaml
```

* Now apply the resource to be run:

```console
$ kubectl apply -f examples/run-from-kubernetes-operator.yaml
```

* You can then look at the logs of the pod running the experiment:

```console
$ kubectl -n chaostoolkit-run logs -l app=chaostoolkit
```

