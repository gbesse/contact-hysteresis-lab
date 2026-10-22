# contact-hysteresis-lab

## Français

Comparer détecteurs de contact à hystérésis sous bruit et rebonds.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m contact_hysteresis_lab examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Simule un détecteur à deux seuils et durées de confirmation, avec maintien constant entre échantillons. Les confirmations peuvent arriver entre deux lectures ; les rebonds courts annulent le changement en attente. Compare au détecteur simple sur la même trace.

### Limites

Force non négative, temps dans une seule unité ; maintien constant déclaré, pas estimation d’un contact physique ni garantie sur bruit non observé. Sans capteur ou contrôleur natif.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Compare hysteresis contact detectors under noise and bounce.

Synthetic data; no network access or secret required.

```sh
python -m contact_hysteresis_lab examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Simulates dual thresholds and confirmation durations with zero-order hold between samples. Confirmations can occur between readings; short bounces cancel pending changes. Compares a plain threshold detector on the same trace.

### Limits

Nonnegative force, one time unit; declared zero-order hold, not a physical-contact estimator or guarantee against unobserved noise. No native sensor or controller.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Comparar detectores de contacto con histéresis bajo ruido y rebotes.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m contact_hysteresis_lab examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Simula dos umbrales y duraciones de confirmación con retención constante entre muestras. Confirmaciones pueden ocurrir entre lecturas; rebotes cortos cancelan cambios pendientes. Compara detector de umbral simple en la misma traza.

### Límites

Fuerza no negativa, una unidad temporal; retención constante declarada, no estimador de contacto físico ni garantía ante ruido no observado. Sin sensor ni controlador nativo.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://github.com/gazebosim/gz-sim
- https://github.com/gbesse/robot-contact-oracle
